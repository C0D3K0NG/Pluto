<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A90D9,100:2E5A8B&height=200&section=header&text=Pluto&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Voice-Controlled%20ChatGPT%20Assistant&descAlignY=55&descSize=20" width="100%"/>

<!-- Typing Animation -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=4A90D9&center=true&vCenter=true&random=false&width=600&lines=Control+ChatGPT+with+your+voice;Hands-free+productivity;Built+for+Windows" alt="Typing SVG" />
</a>

<br><br>

<!-- Badges with Animation -->
<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
<img src="https://img.shields.io/github/stars/C0D3K0NG/Pluto?style=for-the-badge&color=yellow" alt="Stars">

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

## 🎤 Voice Commands

| Command | Action |
|:-------:|:------:|
| **"Open Pluto"** / **"Hey Pluto"** | Launch ChatGPT |
| **"Listen Pluto"** | Start recording |
| **"Thanks Pluto"** / **"Stop Pluto"** | Stop recording |
| **"Sleep Pluto"** | Pause listening |
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

Right-click the system tray icon for quick access:

**Listen** → Start recording &nbsp;|&nbsp;
**Thanks** → Stop recording &nbsp;|&nbsp;
**Sleep/Wake** → Toggle pause<br>
**Start with Windows** → Auto-start toggle &nbsp;|&nbsp;
**Quit** → Exit

<br>

---

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

Edit `config.json` to customize your setup:

```json
{
    "target_coordinates": {"x": 1845, "y": 405},
    "chatgpt_path": "C:\\Path\\To\\ChatGPT.exe",
    "commands": {
        "open": ["open pluto", "hey pluto"],
        "listen": ["listen pluto"],
        "thanks": ["thanks pluto", "stop pluto"],
        "sleep": ["sleep pluto"],
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

<br>

---

## 🔊 Custom Sounds

Place `.wav` files in the `sounds/` folder:

| File | Purpose |
|:----:|:-------:|
| `success.wav` | Command success |
| `error.wav` | Error occurred |
| `ready.wav` | Pluto started |
| `listening.wav` | Recording started |
| `goodbye.wav` | Pluto closing |

<br>

---

## 📁 Project Structure

```
Pluto/
├── main.py           # Main application
├── config.json       # Configuration
├── requirements.txt  # Dependencies
├── assets/           # Icons
├── sounds/           # Sound files
└── pluto_log.txt     # Command log
```

<br>

---

## 🤝 Contributing

Pull requests welcome!<br>
For major changes, please open an issue first.

<br>

---

## 📄 License

**MIT License** — feel free to use and modify!

<br>

<!-- Animated Footer -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A90D9,100:2E5A8B&height=120&section=footer" width="100%"/>

</div>
