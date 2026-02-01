<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A90D9,100:2E5A8B&height=200&section=header&text=Pluto&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Voice-Controlled%20ChatGPT%20Assistant&descAlignY=55&descSize=20" width="100%"/>

<!-- Logo -->
<img src="assets/pluto_icon.png" width="180" alt="Pluto Logo"/>

<br>

<!-- Typing Animation -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=4A90D9&center=true&vCenter=true&random=false&width=600&lines=Control+ChatGPT+with+your+voice;Hands-free+productivity;Built+for+Windows" alt="Typing SVG" />
</a>

<br><br>

<!-- Badges -->
<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">

<br><br>

A hands-free voice assistant that controls the ChatGPT desktop application<br>
using voice commands, keyboard shortcuts, and a system tray interface.

<br>

---

## ✨ Features

<table>
  <tr>
    <td align="center" width="180" height="140">
      <img src="assets/microphone.png" height="48" alt="Voice"><br>
      <b>Voice Commands</b><br>
      <sub>Natural speech recognition</sub>
    </td>
    <td align="center" width="180" height="140">
      <img src="assets/keyboard.png" height="48" alt="Keyboard"><br>
      <b>Hotkeys</b><br>
      <sub>Keyboard shortcuts</sub>
    </td>
    <td align="center" width="180" height="140">
      <img src="assets/speech.png" height="48" alt="Speech"><br>
      <b>Voice Feedback</b><br>
      <sub>Pluto speaks back</sub>
    </td>
  </tr>
  <tr>
    <td align="center" height="140">
      <img src="assets/sleep.png" height="48" alt="Sleep"><br>
      <b>Sleep Mode</b><br>
      <sub>Pause & resume</sub>
    </td>
    <td align="center" height="140">
      <img src="assets/settings.png" height="48" alt="Settings"><br>
      <b>Configurable</b><br>
      <sub>Custom settings</sub>
    </td>
    <td align="center" height="140">
      <img src="assets/rocket.png" height="48" alt="Startup"><br>
      <b>Auto-Start</b><br>
      <sub>Launch with Windows</sub>
    </td>
  </tr>
</table>

<br>

---

## 📋 Features Added

</div>

### 1. Voice Command Recognition
- Uses Google Speech Recognition for accurate voice detection
- Supports multiple command variants (e.g., "Open Pluto", "Hey Pluto", "Launch Pluto")
- Continuous listening with ambient noise adjustment

### 2. ChatGPT Window Integration  
- Automatically finds and focuses the ChatGPT desktop window
- Clicks precise coordinates to control voice recording
- Closes ChatGPT window on exit

### 3. Keyboard Hotkey Support
- Global hotkeys work from any application
- Configurable key combinations via `config.json`
- Default: `Ctrl+Shift+L` (Listen), `Ctrl+Shift+T` (Thanks), `Ctrl+Shift+Q` (Quit)

### 4. Voice Feedback (Text-to-Speech)
- Pluto speaks responses back using `pyttsx3`
- Confirms commands like "Listening", "You're welcome", "Goodbye"
- Non-blocking threaded playback

### 5. Sound Effects
- Audio cues for all actions (success, error, ready, goodbye)
- Custom `.wav` files supported in `sounds/` folder
- Falls back to system beeps if files missing

### 6. Sleep/Wake Mode
- Pause listening with "Sleep Pluto" or "Pause Pluto"
- Resume with "Wake up Pluto"
- Ignores all commands except wake/close when sleeping

### 7. System Tray Icon
- Minimizes to system tray with custom icon
- Right-click menu for quick access to all functions
- Shows current sleep/wake state

### 8. Auto-Start on Windows Boot
- Toggle via system tray menu
- Adds to Windows Registry Run key
- Starts Pluto automatically on login

### 9. Configuration File (`config.json`)
- Customize click coordinates, ChatGPT path
- Define command phrases and hotkeys
- Add/modify sound file mappings

### 10. Logging
- All commands logged to `pluto_log.txt`
- Timestamps and action details
- Useful for debugging and usage tracking

---

<div align="center">

## 🎤 Voice Commands

| Command | Action |
|:-------:|:------:|
| **"Open Pluto"** / **"Hey Pluto"** | Launch ChatGPT |
| **"Listen Pluto"** | Start recording |
| **"Thanks Pluto"** / **"Stop Pluto"** | Stop recording |
| **"Sleep Pluto"** / **"Pause Pluto"** | Pause listening |
| **"Wake up Pluto"** | Resume listening |
| **"Close Pluto"** / **"Goodbye Pluto"** | Exit Pluto |

<br>

---

## ⌨️ Keyboard Shortcuts

| Hotkey | Action |
|:------:|:------:|
| `Ctrl+Shift+L` | Start recording |
| `Ctrl+Shift+T` | Stop recording |
| `Ctrl+Shift+Q` | Quit Pluto |

<br>

---

## 🖥️ System Tray Menu

</div>

Right-click the Pluto tray icon:

| Option | Description |
|--------|-------------|
| **Listen** | Start voice recording in ChatGPT |
| **Thanks** | Stop voice recording |
| **Sleep / Wake Up** | Toggle pause mode (dynamic label) |
| **Start with Windows** | Enable/disable auto-start (checkbox) |
| **Quit Pluto** | Exit application and close ChatGPT |

---

<div align="center">

## 📖 Use Cases

</div>

### Use Case 1: Hands-Free ChatGPT Conversations
> **Scenario:** You want to have a voice conversation with ChatGPT while cooking or exercising.

1. Say **"Open Pluto"** → ChatGPT launches
2. Say **"Listen Pluto"** → ChatGPT starts recording your voice
3. Speak your question to ChatGPT
4. Say **"Thanks Pluto"** → Stops recording, ChatGPT processes your question

### Use Case 2: Productivity While Multitasking
> **Scenario:** You're coding and need to ask ChatGPT a quick question without switching windows.

1. Press **`Ctrl+Shift+L`** → ChatGPT activates and starts recording
2. Speak your question
3. Press **`Ctrl+Shift+T`** → Recording stops
4. Continue coding while waiting for ChatGPT's response

### Use Case 3: Temporary Pause During Meetings
> **Scenario:** You're in a meeting and don't want Pluto listening to everything.

1. Say **"Sleep Pluto"** → Pluto stops processing commands
2. Have your meeting
3. Say **"Wake up Pluto"** → Pluto resumes listening
4. Or use the system tray menu: Right-click → Sleep/Wake

### Use Case 4: Background Running with Auto-Start
> **Scenario:** You want Pluto always available when using your computer.

1. Right-click Pluto tray icon → **"Start with Windows"** ✓
2. Restart your computer
3. Pluto automatically starts and runs in background
4. Use voice commands anytime!

### Use Case 5: Custom Command Phrases
> **Scenario:** You prefer saying "Hey Assistant" instead of "Hey Pluto".

1. Open `config.json`
2. Edit the commands section:
   ```json
   "commands": {
       "open": ["hey assistant", "start assistant"],
       ...
   }
   ```
3. Restart Pluto
4. Use your custom phrases!

---

<div align="center">

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/C0D3K0NG/Pluto.git
cd Pluto

# Install dependencies
pip install -r requirements.txt

# Run Pluto
python main.py
```

<br>

---

## ⚙️ Configuration

</div>

Edit `config.json` to customize:

```json
{
    "target_coordinates": {"x": 1845, "y": 405},
    "chatgpt_path": "C:\\Path\\To\\ChatGPT.exe",
    "commands": {
        "open": ["open pluto", "hey pluto", "start pluto"],
        "listen": ["listen pluto", "pluto listen"],
        "thanks": ["thanks pluto", "stop pluto"],
        "sleep": ["sleep pluto", "pause pluto"],
        "wake": ["wake up pluto", "wake pluto"],
        "close": ["close pluto", "goodbye pluto"]
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
```

<div align="center">

### Key Configuration Options

| Setting | Description |
|---------|-------------|
| `target_coordinates` | X/Y position of ChatGPT's mic button |
| `chatgpt_path` | Full path to ChatGPT.exe |
| `commands` | Voice command phrase variants |
| `sound_files` | Custom sound effect filenames |
| `hotkeys` | Keyboard shortcut combinations |

<br>

---

## 🔊 Custom Sounds

</div>

Place `.wav` files in the `sounds/` folder:

| File | Trigger |
|------|---------|
| `success.wav` | Command executed successfully |
| `error.wav` | Error occurred |
| `ready.wav` | Pluto startup complete |
| `listening.wav` | Voice recording started |
| `goodbye.wav` | Pluto shutting down |

---

<div align="center">

## 📁 Project Structure

```
Pluto/
├── main.py              # Main application
├── config.json          # Configuration settings
├── requirements.txt     # Python dependencies
├── assets/              # Icons and images
│   ├── pluto_icon.png   # System tray icon
│   ├── microphone.png   # Feature icons
│   └── ...
├── sounds/              # Custom sound files (optional)
└── pluto_log.txt        # Command history log
```

<br>

---

## 🛠️ Dependencies

| Package | Purpose |
|---------|---------|
| `SpeechRecognition` | Voice command detection |
| `PyAutoGUI` | Mouse click automation |
| `PyGetWindow` | Window focus management |
| `keyboard` | Global hotkey support |
| `pyttsx3` | Text-to-speech feedback |
| `pystray` + `pillow` | System tray icon |
| `playsound` | Custom sound effects |

<br>

---

## 🔧 Troubleshooting

</div>

| Issue | Solution |
|-------|----------|
| "Microphone not detected" | Check Windows sound settings, ensure mic is enabled |
| "ChatGPT not found" | Update `chatgpt_path` in config.json |
| "Clicks in wrong location" | Adjust `target_coordinates` for your screen |
| "Hotkeys don't work" | Run as Administrator, or check for conflicts |
| "playsound install fails" | Use `pip install playsound==1.2.2` |

---

<div align="center">

## 🤝 Contributing

Pull requests welcome!<br>
For major changes, please open an issue first.

<br>

## 📄 License

**MIT License** — feel free to use and modify!

<br>

<!-- Animated Footer -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A90D9,100:2E5A8B&height=120&section=footer" width="100%"/>

</div>
