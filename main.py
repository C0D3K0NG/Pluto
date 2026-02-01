import sys
import os

# Suppress stderr to hide external library error messages (ChatGPT, comtypes, etc.)
import ctypes
if sys.platform == 'win32':
    # Redirect stderr to null on Windows
    sys.stderr = open(os.devnull, 'w')

import speech_recognition as sr
import pyautogui
import pygetwindow as gw
import subprocess
import time
import winsound
import logging
import threading
from datetime import datetime

# Color output support
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR_SUCCESS = Fore.GREEN
    COLOR_ERROR = Fore.RED
    COLOR_INFO = Fore.CYAN
    COLOR_WARNING = Fore.YELLOW
    COLOR_COMMAND = Fore.MAGENTA
    COLOR_RESET = Style.RESET_ALL
except ImportError:
    # Fallback if colorama not installed
    COLOR_SUCCESS = COLOR_ERROR = COLOR_INFO = COLOR_WARNING = COLOR_COMMAND = COLOR_RESET = ""

# Try to import keyboard library, provide fallback if not installed
try:
    import keyboard
    KEYBOARD_AVAILABLE = True
except ImportError:
    KEYBOARD_AVAILABLE = False
    print("Note: 'keyboard' library not installed. Hotkey support disabled.")
    print("Install with: pip install keyboard")

# Try to import text-to-speech library
try:
    import pyttsx3
    TTS_ENGINE = pyttsx3.init()
    TTS_ENGINE.setProperty('rate', 175)  # Speed of speech
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("Note: 'pyttsx3' library not installed. Voice feedback disabled.")
    print("Install with: pip install pyttsx3")

def speak(text):
    """Speak text using text-to-speech (non-blocking)"""
    if TTS_AVAILABLE:
        def _speak():
            TTS_ENGINE.say(text)
            TTS_ENGINE.runAndWait()
        threading.Thread(target=_speak, daemon=True).start()

# Try to import system tray library
try:
    import pystray
    from PIL import Image, ImageDraw
    TRAY_AVAILABLE = True
except ImportError:
    TRAY_AVAILABLE = False
    print("Note: 'pystray' library not installed. System tray disabled.")
    print("Install with: pip install pystray pillow")

def create_tray_icon():
    """Load or create icon for the system tray"""
    # Try to load custom icon from assets folder
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "pluto_icon.png")
    if os.path.exists(icon_path):
        try:
            return Image.open(icon_path)
        except Exception:
            pass
    
    # Fallback: Create a simple circle icon
    size = 64
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse([4, 4, size-4, size-4], fill='#4A90D9', outline='#2E5A8B', width=2)
    draw.text((size//3, size//5), "P", fill='white')
    return image

# --- AUTO-START CONFIGURATION ---
import winreg

def is_autostart_enabled():
    """Check if Pluto is set to auto-start with Windows"""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                             r"Software\Microsoft\Windows\CurrentVersion\Run", 
                             0, winreg.KEY_READ)
        winreg.QueryValueEx(key, "PlutoAssistant")
        winreg.CloseKey(key)
        return True
    except WindowsError:
        return False

def enable_autostart():
    """Add Pluto to Windows startup"""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Microsoft\Windows\CurrentVersion\Run",
                             0, winreg.KEY_SET_VALUE)
        script_path = os.path.abspath(__file__)
        # Use pythonw.exe for silent startup (no console window)
        python_path = sys.executable.replace('python.exe', 'pythonw.exe')
        command = f'"{python_path}" "{script_path}"'
        winreg.SetValueEx(key, "PlutoAssistant", 0, winreg.REG_SZ, command)
        winreg.CloseKey(key)
        logger.info("Auto-start enabled")
        return True
    except WindowsError as e:
        logger.error(f"Failed to enable auto-start: {e}")
        return False

def disable_autostart():
    """Remove Pluto from Windows startup"""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Microsoft\Windows\CurrentVersion\Run",
                             0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, "PlutoAssistant")
        winreg.CloseKey(key)
        logger.info("Auto-start disabled")
        return True
    except WindowsError as e:
        logger.error(f"Failed to disable auto-start: {e}")
        return False

# --- CONFIGURATION ---
# Load config from config.json or use defaults
import json

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

def load_config():
    """Load configuration from config.json with fallback defaults"""
    defaults = {
        "target_coordinates": {"x": 1845, "y": 405},
        "chatgpt_path": r"C:\Program Files\WindowsApps\OpenAI.ChatGPT-Desktop_1.2025.328.0_x64__2p2nqsd0c76g0\app\ChatGPT.exe",
        "commands": {
            "open": ["open pluto", "start pluto", "launch pluto", "hey pluto"],
            "listen": ["listen pluto", "pluto listen", "record pluto"],
            "thanks": ["thanks pluto", "thank you pluto", "stop pluto", "pluto stop"],
            "close": ["close pluto", "quit pluto", "exit pluto", "goodbye pluto"],
            "sleep": ["sleep pluto", "pause pluto", "pluto sleep"],
            "wake": ["wake up pluto", "wake pluto", "pluto wake up"]
        },
        "sound_files": {
            "success": "success.wav",
            "error": "error.wav",
            "ready": "ready.wav",
            "listening": "listening.wav",
            "goodbye": "goodbye.wav"
        },
        "hotkeys": {
            "listen": "ctrl+shift+l",
            "thanks": "ctrl+shift+t",
            "quit": "ctrl+shift+q"
        }
    }
    
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
            # Merge with defaults (in case new fields added)
            for key in defaults:
                if key not in config:
                    config[key] = defaults[key]
            print("Loaded config from config.json")
            return config
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not load config.json - {e}")
    
    return defaults

# Load configuration
CONFIG = load_config()
TARGET_X = CONFIG["target_coordinates"]["x"]
TARGET_Y = CONFIG["target_coordinates"]["y"]
COMMANDS = CONFIG["commands"]
CHATGPT_PATH = CONFIG["chatgpt_path"]
SOUND_FILES = CONFIG["sound_files"]
HOTKEYS = CONFIG["hotkeys"]

# Pause/Sleep state
PAUSED = False

# 6. Logging Setup
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pluto_log.txt")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # Also print to console
    ]
)
logger = logging.getLogger("Pluto")

# --- SOUND CONFIGURATION ---
# Path to sounds folder - place your .wav files here
SOUNDS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")

# Try to import playsound library
try:
    from playsound import playsound
    PLAYSOUND_AVAILABLE = True
except ImportError:
    PLAYSOUND_AVAILABLE = False
    print("Note: 'playsound' library not installed. Using system beeps.")
    print("Install with: pip install playsound")

# --- HELPER FUNCTIONS ---

def _play_sound_sync(sound_type):
    """Internal: Synchronous sound playback"""
    # Try to play custom sound file first
    if PLAYSOUND_AVAILABLE:
        sound_file = os.path.join(SOUNDS_DIR, SOUND_FILES.get(sound_type, ""))
        if os.path.exists(sound_file):
            try:
                playsound(sound_file, block=True)
                return
            except Exception as e:
                logger.warning(f"Could not play sound file: {e}")
    
    # Fallback to system beeps
    try:
        if sound_type == "success":
            winsound.Beep(800, 150)
            winsound.Beep(1000, 150)
        elif sound_type == "error":
            winsound.Beep(400, 200)
            winsound.Beep(300, 200)
        elif sound_type == "ready":
            for _ in range(3):
                winsound.Beep(600, 100)
                time.sleep(0.05)
        elif sound_type == "listening":
            winsound.Beep(1200, 100)
        elif sound_type == "goodbye":
            winsound.Beep(800, 150)
            winsound.Beep(600, 150)
            winsound.Beep(400, 200)
    except Exception as e:
        logger.warning(f"Could not play sound: {e}")

def play_sound(sound_type="success"):
    """Play sounds in background thread to avoid blocking voice recognition"""
    sound_thread = threading.Thread(target=_play_sound_sync, args=(sound_type,), daemon=True)
    sound_thread.start()

def log_command(command, action):
    """6. Logging - Log all commands with timestamps"""
    logger.info(f"Command: '{command}' -> Action: {action}")

def match_command(spoken_text, command_type):
    """4. Check if spoken text matches any configured command variant"""
    for phrase in COMMANDS.get(command_type, []):
        if phrase in spoken_text:
            return True
    return False

def focus_chatgpt_window():
    """Helper to find and focus ChatGPT window"""
    chatgpt_windows = gw.getWindowsWithTitle('ChatGPT')
    if chatgpt_windows:
        chatgpt_windows[0].activate()
        time.sleep(0.3)
        return True
    logger.warning("ChatGPT window not found!")
    return False

def close_chatgpt_window():
    """Helper to find and close ChatGPT window"""
    chatgpt_windows = gw.getWindowsWithTitle('ChatGPT')
    if chatgpt_windows:
        chatgpt_windows[0].close()
        logger.info("ChatGPT window closed")
        return True
    logger.warning("ChatGPT window not found to close!")
    return False

def execute_listen():
    """Execute listen command action"""
    print(f">> Clicking at ({TARGET_X}, {TARGET_Y})...")
    speak("Listening")
    play_sound("listening")
    focus_chatgpt_window()
    pyautogui.click(TARGET_X, TARGET_Y)
    log_command("hotkey/voice", "listen - clicked microphone")

def execute_thanks():
    """Execute thanks command action"""
    print(f">> You're welcome! Clicking again at ({TARGET_X}, {TARGET_Y})...")
    speak("You're welcome")
    play_sound("success")
    focus_chatgpt_window()
    pyautogui.click(TARGET_X, TARGET_Y)
    log_command("hotkey/voice", "thanks - stopped recording")

def execute_quit():
    """Execute quit command action"""
    print(">> Closing Pluto Application. Goodbye!")
    speak("Goodbye")
    play_sound("goodbye")
    log_command("hotkey/voice", "close - application terminated")
    time.sleep(1)  # Wait for speech to finish
    close_chatgpt_window()
    os._exit(0)

# 7. Hotkey Override Setup
def setup_hotkeys():
    """Setup keyboard shortcuts as backup input method (configurable via config.json)"""
    if not KEYBOARD_AVAILABLE:
        return
    
    try:
        keyboard.add_hotkey(HOTKEYS["listen"], execute_listen, suppress=True)
        keyboard.add_hotkey(HOTKEYS["thanks"], execute_thanks, suppress=True)
        keyboard.add_hotkey(HOTKEYS["quit"], execute_quit, suppress=True)
        
        logger.info(f"Hotkeys registered: {HOTKEYS['listen']} (Listen), {HOTKEYS['thanks']} (Thanks), {HOTKEYS['quit']} (Quit)")
    except Exception as e:
        logger.error(f"Failed to setup hotkeys: {e}")

# System tray icon setup
def setup_tray():
    """Setup system tray icon with menu"""
    if not TRAY_AVAILABLE:
        return None
    
    def on_listen(icon, item):
        execute_listen()
    
    def on_thanks(icon, item):
        execute_thanks()
    
    def on_sleep_wake(icon, item):
        global PAUSED
        if PAUSED:
            PAUSED = False
            play_sound("ready")
            speak("Pluto is awake")
            logger.info("Woke up via tray menu")
        else:
            PAUSED = True
            play_sound("goodbye")
            speak("Going to sleep")
            logger.info("Paused via tray menu")
    
    def on_quit(icon, item):
        icon.stop()
        execute_quit()
    
    def get_sleep_text(item):
        return "Wake Up" if PAUSED else "Sleep"
    
    def on_autostart_toggle(icon, item):
        if is_autostart_enabled():
            disable_autostart()
            speak("Auto-start disabled")
        else:
            enable_autostart()
            speak("Auto-start enabled")
    
    def get_autostart_checked(item):
        return is_autostart_enabled()
    
    menu = pystray.Menu(
        pystray.MenuItem("Listen", on_listen),
        pystray.MenuItem("Thanks", on_thanks),
        pystray.MenuItem(get_sleep_text, on_sleep_wake),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Start with Windows", on_autostart_toggle, checked=get_autostart_checked),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem("Quit Pluto", on_quit)
    )
    
    icon = pystray.Icon("Pluto", create_tray_icon(), "Pluto Voice Assistant", menu)
    
    # Run tray icon in background thread
    tray_thread = threading.Thread(target=icon.run, daemon=True)
    tray_thread.start()
    logger.info("System tray icon started")
    return icon

def listen_command():
    global PAUSED  # Declare global at function start
    # Initialize recognizer
    r = sr.Recognizer()
    
    # Setup hotkeys in background
    setup_hotkeys()
    
    # Setup system tray icon
    tray_icon = setup_tray()
    
    with sr.Microphone() as source:
        print(f"{COLOR_INFO}Adjusting for background noise... (Please wait){COLOR_RESET}")
        r.adjust_for_ambient_noise(source, duration=1)
        play_sound("ready")
        print(f"\n{COLOR_SUCCESS}╔══════════════════════════════════════╗{COLOR_RESET}")
        print(f"{COLOR_SUCCESS}║       🎤 PLUTO IS LISTENING 🎤       ║{COLOR_RESET}")
        print(f"{COLOR_SUCCESS}╚══════════════════════════════════════╝{COLOR_RESET}\n")
        logger.info("Pluto started and ready for commands")
        
        if KEYBOARD_AVAILABLE:
            print(f"{COLOR_INFO}Hotkeys: {COLOR_COMMAND}Ctrl+Shift+L{COLOR_INFO} (Listen) | {COLOR_COMMAND}Ctrl+Shift+T{COLOR_INFO} (Thanks) | {COLOR_COMMAND}Ctrl+Shift+Q{COLOR_INFO} (Quit){COLOR_RESET}")
        
        while True:
            try:
                # Listen for audio
                print(f"{COLOR_INFO}Waiting for command...{COLOR_RESET}")
                audio = r.listen(source, phrase_time_limit=5)
                
                # Convert speech to text
                command = r.recognize_google(audio).lower()
                print(f"{COLOR_COMMAND}Heard: '{command}'{COLOR_RESET}")
                
                # --- COMMAND LOGIC (using configurable commands) ---
                
                # Check if paused - only respond to wake and close commands
                if PAUSED:
                    if match_command(command, "wake"):
                        PAUSED = False
                        play_sound("ready")
                        print(f"{COLOR_SUCCESS}>> Pluto is awake and listening!{COLOR_RESET}")
                        log_command(command, "wake - resumed listening")
                    elif match_command(command, "close"):
                        print(f"{COLOR_WARNING}>> Closing Pluto Application. Goodbye!{COLOR_RESET}")
                        play_sound("goodbye")
                        log_command(command, "close - application terminated")
                        close_chatgpt_window()
                        sys.exit()
                    else:
                        print(f"{COLOR_WARNING}>> (Sleeping) Ignoring: '{command}'{COLOR_RESET}")
                    continue
                
                # 1. Wake word: "Open Pluto" (and variants)
                if match_command(command, "open"):
                    try:
                        play_sound("success")
                        os.startfile(CHATGPT_PATH) 
                        print(f"{COLOR_SUCCESS}>> Pluto Assistant is Ready/Active!{COLOR_RESET}")
                        log_command(command, "open - launched ChatGPT")
                        time.sleep(3)
                        # Resize ChatGPT window to small corner
                        chatgpt_windows = gw.getWindowsWithTitle('ChatGPT')
                        if chatgpt_windows:
                            win = chatgpt_windows[0]
                            # Get screen size
                            screen_width, screen_height = pyautogui.size()
                            # Set window size (400x600) and position (bottom-right corner)
                            win_width, win_height = 400, 400
                            win.resizeTo(win_width, win_height)
                            win.moveTo(screen_width - win_width - 10, screen_height - win_height - 50)
                            win.activate()
                            logger.info("ChatGPT window resized to corner")
                        time.sleep(2)
                        pyautogui.click(TARGET_X, 1041)
                    except FileNotFoundError:
                        play_sound("error")
                        logger.error(f"ChatGPT not found at: {CHATGPT_PATH}")
                        print(f"{COLOR_ERROR}>> ERROR: ChatGPT not found! Check CHATGPT_PATH in config.{COLOR_RESET}")
                    except OSError as e:
                        play_sound("error")
                        logger.error(f"Failed to launch ChatGPT: {e}")
                        print(f"{COLOR_ERROR}>> ERROR: Could not launch ChatGPT - {e}{COLOR_RESET}")
                  
                # 2. Click specific coordinates: "Listen Pluto" (and variants)
                elif match_command(command, "listen"):
                    print(f"{COLOR_SUCCESS}>> Clicking at ({TARGET_X}, {TARGET_Y})...{COLOR_RESET}")
                    play_sound("listening")
                    focus_chatgpt_window()
                    pyautogui.click(TARGET_X, TARGET_Y)
                    log_command(command, "listen - clicked microphone")

                # 3. Click coordinates again: "Thanks Pluto" (and variants)
                elif match_command(command, "thanks"):
                    print(f"{COLOR_SUCCESS}>> You're welcome! Clicking again at ({TARGET_X}, {TARGET_Y})...{COLOR_RESET}")
                    play_sound("success")
                    focus_chatgpt_window()
                    pyautogui.click(TARGET_X, TARGET_Y)
                    log_command(command, "thanks - stopped recording")

                # 4. Shut down: "Close Pluto" (and variants)
                elif match_command(command, "close"):
                    print(f"{COLOR_WARNING}>> Closing Pluto Application. Goodbye!{COLOR_RESET}")
                    play_sound("goodbye")
                    log_command(command, "close - application terminated")
                    close_chatgpt_window()
                    sys.exit()

                # 5. Sleep: "Sleep Pluto" (and variants)
                elif match_command(command, "sleep"):
                    PAUSED = True
                    play_sound("goodbye")
                    print(f"{COLOR_WARNING}>> Pluto is now sleeping. Say 'Wake up Pluto' to resume.{COLOR_RESET}")
                    log_command(command, "sleep - paused listening")

            except sr.UnknownValueError:
                # Speech was unintelligible
                pass
            except sr.RequestError:
                play_sound("error")
                logger.error("Could not request results; check your internet connection.")
            except KeyboardInterrupt:
                # Handle manual stop (Ctrl+C)
                play_sound("goodbye")
                logger.info("Stopping manually via Ctrl+C")
                break

if __name__ == "__main__":
    listen_command()