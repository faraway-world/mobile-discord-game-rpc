# Mobile Discord Game RPC 🎮 + 💬

A minimal Python app with a GUI to show your current mobile game on Discord using Rich Presence.

![image.alt](https://github.com/faraway-world/mobile-discord-game-rpc/blob/834e024eb9593a8c19ace5ea4e8d3c7c51492ca0/Screenshot_20250613_131221.png)
## Features

- Black-and-white aesthetic GUI
- Click to select game — no manual editing
- Shows game icon and name on Discord
- 
![image.alt](https://github.com/faraway-world/mobile-discord-game-rpc/blob/834e024eb9593a8c19ace5ea4e8d3c7c51492ca0/Screenshot_20250613_131230.png)

## Setup

1. Clone or download this repo
2. Create and activate a Python virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install pypresence
    ```
4. Replace dummy `CLIENT_ID` and `games` dictionary in `rpc_gui.py` with your actual values.

## Usage

```bash
python3 rpc_gui.py
```

Select a game from the GUI to start Rich Presence!
![image.alt](https://github.com/faraway-world/mobile-discord-game-rpc/blob/003c09334303f00798afee113284fce9d001a7e3/Screenshot_20250613_131444.jpg)
## Notes

Requires the Discord desktop app to be running.

Tested on Linux with Python 3.12+

---

## ⚠️ Linux Users

If you're using Linux, make sure you have the **.deb version of the Discord desktop app** installed.  
Flatpak, Snap, or web versions **won't work** with Rich Presence due to IPC restrictions.
