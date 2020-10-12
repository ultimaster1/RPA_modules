import threading, win32gui, win32process, psutil
import os
import logging
from pynput import keyboard
from pynput.mouse import Listener
import keyboard as kb
import time
file = 'C:/Users/kir/Desktop/actions/log.txt'
logging.basicConfig(filename=file,
                    level='INFO',
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def loop_special_keys():
    if kb.is_pressed('ctrl+c'):
        logging.info('ctrl + C')
        time.sleep(1)
    elif kb.is_pressed('ctrl+v'):
        logging.info('ctrl + V')
        time.sleep(1)
    elif kb.is_pressed('ctrl+x'):
        logging.info('ctrl + X')
        time.sleep(1)


def on_press(key):
    try:
        if str(key) == 'Key.ctrl_l' or str(key) == 'Key.ctrl_r' or str(key) == 'Key.ctrl':
            pass
        else:
            press = 'PRESS {0}'.format(key.char)
            logging.info(str(press))
    except AttributeError:
        press = 'PRESS {0}'.format(key)
        logging.info(str(press))


def on_click(x, y, button, pressed):
    logging.info('Mouse is clicked') if pressed else print('Released')

# Collect events until released
def mouse():
    with Listener(
            on_click=on_click) as listener:
        listener.join()


def on_release(key):
    release = 'RELEASE {0}'.format(key)
    # logging.info(release)
    print(release)
    if key == keyboard.Key.esc:
        return False


def start_lis():
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
        ) as listener:
        listener.join()


class action_logger():
    def __init__(self):
        self.path = os.path.abspath(psutil.Process(win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[-1]).name())
        self.tempWindowName = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        logging.info(self.path + '|' + self.tempWindowName)


    def check(self):
        try:
            tempWindowName = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            path = os.path.abspath(psutil.Process(win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[-1]).name())
        except:
            path = self.path
            tempWindowName = self.tempWindowName
        if self.path != path or tempWindowName != self.tempWindowName:
            self.path = path
            self.tempWindowName = tempWindowName
            logging.info(self.path + '|' + tempWindowName)


def loop(obj):
    while True:
        obj.check()
        loop_special_keys()
        time.sleep(0.001)


if __name__ == '__main__':
    A_L = action_logger()
    keyboard_th = threading.Thread(target = start_lis)
    mouse_th = threading.Thread(target=mouse)
    exe_and_spec = threading.Thread(target = loop, args = (A_L,))
    keyboard_th.start()
    exe_and_spec.start()
    mouse_th.start()


