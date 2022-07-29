import pyautogui, time
from pynput.keyboard import Listener
from threading import Thread, Lock

KeyBuffer = []
lock = Lock()

def KeyListener():

    def on_press(key):
        lock.acquire()
        KeyBuffer.append(key)
        lock.release()

    with Listener(on_press=on_press) as listener:
         listener.join()


MOVE_STYLE = pyautogui.easeInElastic
pyautogui.FAILSAFE = False

Unknown = 2
X = [100,1000]
Y = [100,1000]

print("Press Ctrl+C to stop...")

try:
    # Get cursor position
    pos = pyautogui.position()
    while True:
        for x in X:
            for y in Y:
                # Do sleep before the first cursoe move
                time.sleep(50)
                pos_cur = pyautogui.position()
                lock.acquire()
                if len(KeyBuffer) == 0:
                    lock.release()
                    if pos_cur == pos:
                        pyautogui.moveTo(x, y, Unknown, MOVE_STYLE)
                else:
                    lock.release()
                    pass
                pos = pyautogui.position()
except KeyboardInterrupt:
    print("\nGood Bye!")
