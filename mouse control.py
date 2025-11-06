# mouse_to_logtxt.py
from datetime import datetime
from pynput import mouse

LOGFILE = "log.txt"
X_OFFSET, Y_OFFSET = 1, 2  # map (0,0) -> (5,10)

def ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def w(s):
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(f"{ts()} {s}\n")

def on_move(x, y):
    w(f"MOVE {int(x+X_OFFSET)} {int(y+Y_OFFSET)} CURS({x},{y})")

def on_click(x, y, button, pressed):
    w(f"CLICK {'P' if pressed else 'R'} {button} {int(x+X_OFFSET)} {int(y+Y_OFFSET)}")

def on_scroll(x, y, dx, dy):
    w(f"SCROLL {dx},{dy} {int(x+X_OFFSET)} {int(y+Y_OFFSET)}")

if __name__ == "__main__":
    with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as l:
        l.join()
