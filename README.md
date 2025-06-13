# Mobile Discord Game RPC 🎮 + 💬

A minimal Python app with a GUI to show your current mobile game on Discord using Rich Presence.

![image.alt](https://github.com/faraway-world/mobile-discord-game-rpc/blob/834e024eb9593a8c19ace5ea4e8d3c7c51492ca0/Screenshot_20250613_131221.png)
## Features

- Black-and-white aesthetic GUI
- Click to select game — no manual editing
- Shows game icon and name on Discord
  
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

![image.alt](https://github.com/faraway-world/mobile-discord-game-rpc/blob/bfa6f679d7ed31f9cbfaadab8eeb74a5ef45379d/Screenshot_20250613_131444(1).png)

## Notes

Requires the Discord desktop app to be running.

Tested on Linux with Python 3.12+

---

## ⚠️ Linux Users

If you're using Linux, make sure you have the **.deb version of the Discord desktop app** installed.  
Flatpak, Snap, or web versions **won't work** with Rich Presence due to IPC restrictions.
