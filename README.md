# Pluto

**Voice-Controlled ChatGPT Assistant for Windows**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

A hands-free voice assistant that controls the ChatGPT desktop application using voice commands, keyboard shortcuts, and a system tray interface.

---

## Features

<table>
  <tr>
    <td align="center" width="80"><img src="assets/microphone.png" width="40" alt="Voice"><br><b>Voice Commands</b></td>
    <td>Control ChatGPT with natural speech recognition</td>
  </tr>
  <tr>
    <td align="center"><img src="assets/keyboard.png" width="40" alt="Keyboard"><br><b>Hotkeys</b></td>
    <td>Keyboard shortcuts as backup input method</td>
  </tr>
  <tr>
    <td align="center"><img src="assets/speech.png" width="40" alt="Speech"><br><b>Voice Feedback</b></td>
    <td>Pluto speaks responses back to you</td>
  </tr>
  <tr>
    <td align="center"><img src="assets/sleep.png" width="40" alt="Sleep"><br><b>Sleep Mode</b></td>
    <td>Pause and resume voice recognition</td>
  </tr>
  <tr>
    <td align="center"><img src="assets/settings.png" width="40" alt="Settings"><br><b>Configurable</b></td>
    <td>Customize commands and settings via config.json</td>
  </tr>
  <tr>
    <td align="center"><img src="assets/rocket.png" width="40" alt="Startup"><br><b>Auto-Start</b></td>
    <td>Optional launch with Windows startup</td>
  </tr>
</table>

---

## Voice Commands

| Command | Action |
|---------|--------|
| "Open Pluto" / "Hey Pluto" | Launch ChatGPT application |
| "Listen Pluto" | Start voice recording in ChatGPT |
| "Thanks Pluto" / "Stop Pluto" | Stop recording |
| "Sleep Pluto" / "Pause Pluto" | Pause voice recognition |
| "Wake up Pluto" | Resume voice recognition |
| "Close Pluto" / "Goodbye Pluto" | Exit Pluto and close ChatGPT |

---

## Keyboard Shortcuts

| Hotkey | Action |
|--------|--------|
| `Ctrl+Shift+L` | Start ChatGPT voice recording |
| `Ctrl+Shift+T` | Stop recording |
| `Ctrl+Shift+Q` | Quit Pluto |

---

## System Tray

Right-click the system tray icon for quick access:

- **Listen** — Start voice recording
- **Thanks** — Stop recording
- **Sleep / Wake** — Toggle pause mode
- **Start with Windows** — Enable/disable auto-start
- **Quit Pluto** — Exit application

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/C0D3K0NG/Pluto.git
cd Pluto
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure (optional)

Edit `config.json` to customize settings for your system.

### 4. Run

```bash
python main.py
```

---

## Configuration

Edit `config.json` to customize:

```json
{
    "target_coordinates": {"x": 1845, "y": 405},
    "chatgpt_path": "C:\\Path\\To\\ChatGPT.exe",
    "commands": {
        "open": ["open pluto", "hey pluto"],
        "listen": ["listen pluto"],
        "thanks": ["thanks pluto", "stop pluto"],
        "sleep": ["sleep pluto", "pause pluto"],
        "wake": ["wake up pluto"],
        "close": ["close pluto", "goodbye pluto"]
    },
    "hotkeys": {
        "listen": "ctrl+shift+l",
        "thanks": "ctrl+shift+t",
        "quit": "ctrl+shift+q"
    }
}
```

---

## Custom Sounds

Place `.wav` files in the `sounds/` folder:

| File | Purpose |
|------|---------|
| `success.wav` | Command executed successfully |
| `error.wav` | Error occurred |
| `ready.wav` | Pluto started |
| `listening.wav` | Recording started |
| `goodbye.wav` | Pluto closing |

---

## Project Structure

```
Pluto/
├── main.py           # Main application
├── config.json       # Configuration file
├── requirements.txt  # Python dependencies
├── assets/           # Icons and images
├── sounds/           # Custom sound files (optional)
└── pluto_log.txt     # Command log (auto-generated)
```

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License

[MIT License](LICENSE) — feel free to use and modify.
