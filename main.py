import speech_recognition as sr
import pyautogui
import pygetwindow as gw
import sys
import subprocess
import os
import time
import winsound
import logging
import threading
from datetime import datetime

# Try to import keyboard library, provide fallback if not installed
try:
    import keyboard
    KEYBOARD_AVAILABLE = True
except ImportError:
    KEYBOARD_AVAILABLE = False
    print("Note: 'keyboard' library not installed. Hotkey support disabled.")
    print("Install with: pip install keyboard")

# --- CONFIGURATION ---
# Replace these with the coordinates you found in Step 2
TARGET_X = 1845
TARGET_Y = 405

# 4. Configurable Commands Dictionary
# Easily customize your wake words and commands here
COMMANDS = {
    "open": ["open pluto", "start pluto", "launch pluto", "hey pluto"],
    "listen": ["listen pluto", "pluto listen", "record pluto"],
    "thanks": ["thanks pluto", "thank you pluto", "stop pluto", "pluto stop"],
    "close": ["close pluto", "quit pluto", "exit pluto", "goodbye pluto"]
}

# ChatGPT executable path
CHATGPT_PATH = r"C:\Program Files\WindowsApps\OpenAI.ChatGPT-Desktop_1.2025.328.0_x64__2p2nqsd0c76g0\app\ChatGPT.exe"

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

# Sound file mapping - customize these filenames
SOUND_FILES = {
    "success": "success.wav",
    "error": "error.wav", 
    "ready": "ready.wav",
    "listening": "listening.wav",
    "goodbye": "goodbye.wav"
}

# Try to import playsound library
try:
    from playsound import playsound
    PLAYSOUND_AVAILABLE = True
except ImportError:
    PLAYSOUND_AVAILABLE = False
    print("Note: 'playsound' library not installed. Using system beeps.")
    print("Install with: pip install playsound")

# --- HELPER FUNCTIONS ---

def play_sound(sound_type="success"):
    """5. Sound Effects - Play custom sounds or fallback to beeps"""
    
    # Try to play custom sound file first
    if PLAYSOUND_AVAILABLE:
        sound_file = os.path.join(SOUNDS_DIR, SOUND_FILES.get(sound_type, ""))
        if os.path.exists(sound_file):
            try:
                playsound(sound_file, block=False)
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
    play_sound("listening")
    focus_chatgpt_window()
    pyautogui.click(TARGET_X, TARGET_Y)
    log_command("hotkey/voice", "listen - clicked microphone")

def execute_thanks():
    """Execute thanks command action"""
    print(f">> You're welcome! Clicking again at ({TARGET_X}, {TARGET_Y})...")
    play_sound("success")
    focus_chatgpt_window()
    pyautogui.click(TARGET_X, TARGET_Y)
    log_command("hotkey/voice", "thanks - stopped recording")

def execute_quit():
    """Execute quit command action"""
    print(">> Closing Pluto Application. Goodbye!")
    play_sound("goodbye")
    log_command("hotkey/voice", "close - application terminated")
    close_chatgpt_window()
    os._exit(0)

# 7. Hotkey Override Setup
def setup_hotkeys():
    """Setup keyboard shortcuts as backup input method"""
    if not KEYBOARD_AVAILABLE:
        return
    
    try:
        # Ctrl+Shift+L = Listen Pluto
        keyboard.add_hotkey('ctrl+shift+l', execute_listen, suppress=True)
        # Ctrl+Shift+T = Thanks Pluto  
        keyboard.add_hotkey('ctrl+shift+t', execute_thanks, suppress=True)
        # Ctrl+Shift+Q = Quit Pluto
        keyboard.add_hotkey('ctrl+shift+q', execute_quit, suppress=True)
        
        logger.info("Hotkeys registered: Ctrl+Shift+L (Listen), Ctrl+Shift+T (Thanks), Ctrl+Shift+Q (Quit)")
    except Exception as e:
        logger.error(f"Failed to setup hotkeys: {e}")

def listen_command():
    # Initialize recognizer
    r = sr.Recognizer()
    
    # Setup hotkeys in background
    setup_hotkeys()
    
    with sr.Microphone() as source:
        print("Adjusting for background noise... (Please wait)")
        r.adjust_for_ambient_noise(source, duration=1)
        play_sound("ready")
        print("\n--- PLUTO IS LISTENING ---")
        logger.info("Pluto started and ready for commands")
        
        if KEYBOARD_AVAILABLE:
            print("Hotkeys: Ctrl+Shift+L (Listen) | Ctrl+Shift+T (Thanks) | Ctrl+Shift+Q (Quit)")
        
        while True:
            try:
                # Listen for audio
                print("Waiting for command...")
                audio = r.listen(source, phrase_time_limit=5)
                
                # Convert speech to text
                command = r.recognize_google(audio).lower()
                print(f"Heard: '{command}'")
                
                # --- COMMAND LOGIC (using configurable commands) ---
                
                # 1. Wake word: "Open Pluto" (and variants)
                if match_command(command, "open"):
                    try:
                        play_sound("success")
                        os.startfile(CHATGPT_PATH) 
                        print(">> Pluto Assistant is Ready/Active!")
                        log_command(command, "open - launched ChatGPT")
                        time.sleep(5)
                        pyautogui.click(TARGET_X, 425)
                    except FileNotFoundError:
                        play_sound("error")
                        logger.error(f"ChatGPT not found at: {CHATGPT_PATH}")
                        print(">> ERROR: ChatGPT not found! Check CHATGPT_PATH in config.")
                    except OSError as e:
                        play_sound("error")
                        logger.error(f"Failed to launch ChatGPT: {e}")
                        print(f">> ERROR: Could not launch ChatGPT - {e}")
                  
                # 2. Click specific coordinates: "Listen Pluto" (and variants)
                elif match_command(command, "listen"):
                    print(f">> Clicking at ({TARGET_X}, {TARGET_Y})...")
                    play_sound("listening")
                    focus_chatgpt_window()
                    pyautogui.click(TARGET_X, TARGET_Y)
                    log_command(command, "listen - clicked microphone")

                # 3. Click coordinates again: "Thanks Pluto" (and variants)
                elif match_command(command, "thanks"):
                    print(f">> You're welcome! Clicking again at ({TARGET_X}, {TARGET_Y})...")
                    play_sound("success")
                    focus_chatgpt_window()
                    pyautogui.click(TARGET_X, TARGET_Y)
                    log_command(command, "thanks - stopped recording")

                # 4. Shut down: "Close Pluto" (and variants)
                elif match_command(command, "close"):
                    print(">> Closing Pluto Application. Goodbye!")
                    play_sound("goodbye")
                    log_command(command, "close - application terminated")
                    close_chatgpt_window()
                    sys.exit()

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