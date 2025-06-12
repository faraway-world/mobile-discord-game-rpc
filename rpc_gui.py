import tkinter as tk
from tkinter import messagebox
from pypresence import Presence
import time
import threading

# Replace with your actual Discord Application Client ID
CLIENT_ID = "YOUR_CLIENT_ID_HERE"

# Replace with your actual game names and asset keys
games = {
    "Game 1": "game1_asset_key",
    "Game 2": "game2_asset_key",
    "Game 3": "game3_asset_key"
}

rpc = None
connected = False

def start_presence(game_name, asset_key):
    global rpc, connected
    try:
        if not connected:
            rpc = Presence(CLIENT_ID)
            rpc.connect()
            connected = True

        rpc.update(
            details=f"Playing {game_name}",
            large_image=asset_key,
            large_text=game_name,
            start=int(time.time())
        )
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update RPC:\n{e}")

def stop_presence():
    global rpc, connected
    try:
        if rpc and connected:
            rpc.clear()
            rpc.close()
            connected = False
    except Exception as e:
        messagebox.showerror("Error", f"Failed to clear RPC:\n{e}")

def on_game_select(game_name):
    asset_key = games[game_name]
    threading.Thread(target=start_presence, args=(game_name, asset_key), daemon=True).start()

def on_close():
    stop_presence()
    root.destroy()

root = tk.Tk()
root.title("Mobile Game RPC")
root.configure(bg="black")
root.geometry("300x400")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_close)

label = tk.Label(root, text="Select Game", fg="white", bg="black", font=("Helvetica", 16))
label.pack(pady=10)

for game in games:
    btn = tk.Button(
        root, text=game, fg="white", bg="black", activebackground="white", activeforeground="black",
        font=("Helvetica", 12), relief="ridge", borderwidth=2,
        command=lambda g=game: on_game_select(g)
    )
    btn.pack(fill="x", padx=30, pady=8)

exit_btn = tk.Button(root, text="Exit", command=on_close, fg="white", bg="black", font=("Helvetica", 12))
exit_btn.pack(pady=20)

root.mainloop()
