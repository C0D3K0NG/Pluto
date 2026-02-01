import speech_recognition as sr
import pyautogui
import pygetwindow as gw
import sys
import subprocess
import os
import time

# --- CONFIGURATION ---
# Replace these with the coordinates you found in Step 2
TARGET_X = 1845
TARGET_Y =405

def listen_command():
    # Initialize recognizer
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Adjusting for background noise... (Please wait)")
        r.adjust_for_ambient_noise(source, duration=1)
        print("\n--- PLUTO IS LISTENING ---")
        
        while True:
            try:
                # Listen for audio
                print("Waiting for command...")
                audio = r.listen(source, phrase_time_limit=5)
                
                # Convert speech to text
                command = r.recognize_google(audio).lower()
                print(f"Heard: '{command}'")
                
                # --- COMMAND LOGIC ---
                
                # 1. Wake word: "Open Pluto"
                # (In this script, the loop is always running, but we can use this 
                # to print a confirmation or reset state)
                if "open pluto" in command:
                  os.startfile(r"C:\\Program Files\\WindowsApps\\OpenAI.ChatGPT-Desktop_1.2025.328.0_x64__2p2nqsd0c76g0\\app\\ChatGPT.exe") 
                  print(">> Pluto Assistant is Ready/Active!")
                  time.sleep(5)
                  pyautogui.click(TARGET_X, 425)
                  
                # 2. Click specific coordinates: "Listen Pluto"
                elif "listen pluto" in command:
                    print(f">> Clicking at ({TARGET_X}, {TARGET_Y})...")
                    # Find and focus ChatGPT window before clicking
                    chatgpt_windows = gw.getWindowsWithTitle('ChatGPT')
                    if chatgpt_windows:
                        chatgpt_windows[0].activate()
                        time.sleep(0.3)  # Brief pause to ensure window is focused
                    pyautogui.click(TARGET_X, TARGET_Y)

                # 3. Click coordinates again: "Thanks Pluto"
                elif "thanks pluto" in command:
                    print(f">> You're welcome! Clicking again at ({TARGET_X}, {TARGET_Y})...")
                    # Find and focus ChatGPT window before clicking
                    chatgpt_windows = gw.getWindowsWithTitle('ChatGPT')
                    if chatgpt_windows:
                        chatgpt_windows[0].activate()
                        time.sleep(0.3)  # Brief pause to ensure window is focused
                    pyautogui.click(TARGET_X, TARGET_Y)

                # 4. Shut down: "Close Pluto"
                elif "close pluto" in command:
                    print(">> Closing Pluto Application. Goodbye!")
                    sys.exit() # Terminates the program

            except sr.UnknownValueError:
                # Speech was unintelligible
                pass
            except sr.RequestError:
                print("Could not request results; check your internet connection.")
            except KeyboardInterrupt:
                # Handle manual stop (Ctrl+C)
                print("\nStopping manually.")
                break

if __name__ == "__main__":
    listen_command()