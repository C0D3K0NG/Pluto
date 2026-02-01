# 🚀 Pluto - Voice-Controlled ChatGPT Assistant

A hands-free voice assistant that controls the ChatGPT desktop app using voice commands and keyboard shortcuts.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- 🎤 **Voice Commands** - Control ChatGPT with natural speech
- ⌨️ **Hotkey Support** - Keyboard shortcuts as backup
- 🔊 **Sound Feedback** - Audio cues for all actions
- ⚙️ **Configurable** - Customize commands, hotkeys via `config.json`
- 📝 **Logging** - All commands saved to `pluto_log.txt`

## 📋 Voice Commands

| Command | Action |
|---------|--------|
| "Open Pluto" / "Hey Pluto" | Launch ChatGPT app |
| "Listen Pluto" | Start voice recording in ChatGPT |
| "Thanks Pluto" / "Stop Pluto" | Stop recording |
| "Close Pluto" / "Goodbye Pluto" | Exit Pluto & close ChatGPT |

## ⌨️ Keyboard Shortcuts

| Hotkey | Action |
|--------|--------|
| `Ctrl+Shift+L` | Start ChatGPT voice recording |
| `Ctrl+Shift+T` | Stop recording |
| `Ctrl+Shift+Q` | Quit Pluto |

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/C0D3K0NG/Pluto.git
   cd Pluto
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure** (optional)
   - Edit `config.json` to customize:
     - Click coordinates for your screen
     - ChatGPT executable path
     - Voice command phrases
     - Keyboard hotkeys

4. **Run**
   ```bash
   python main.py
   ```

## ⚙️ Configuration

Edit `config.json` to customize:

```json
{
    "target_coordinates": {"x": 1845, "y": 405},
    "chatgpt_path": "C:\\Path\\To\\ChatGPT.exe",
    "commands": {
        "open": ["open pluto", "hey pluto"],
        "listen": ["listen pluto"],
        "thanks": ["thanks pluto", "stop pluto"],
        "close": ["close pluto", "goodbye pluto"]
    },
    "hotkeys": {
        "listen": "ctrl+shift+l",
        "thanks": "ctrl+shift+t",
        "quit": "ctrl+shift+q"
    }
}
```

## 🔊 Custom Sounds

Place `.wav` files in the `sounds/` folder:
- `success.wav` - Command success
- `error.wav` - Error occurred
- `ready.wav` - Pluto started
- `listening.wav` - Recording started
- `goodbye.wav` - Pluto closing

## 📁 Project Structure

```
Pluto/
├── main.py           # Main application
├── config.json       # Configuration file
├── requirements.txt  # Python dependencies
├── sounds/           # Custom sound files (optional)
└── pluto_log.txt     # Command log (auto-generated)
```

## 🤝 Contributing

Pull requests welcome! For major changes, please open an issue first.

## 📄 License

MIT License - feel free to use and modify!
