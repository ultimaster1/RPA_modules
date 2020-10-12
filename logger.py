import threading, win32gui, win32process, psutil
import os
import logging
from pynput import keyboard
from pynput.mouse import Listener
import keyboard as kb
from datetime import datetime
import pandas as pd
import time


file = 'C:/Users/kir/Desktop/actions/log.txt'
logging.basicConfig(filename=file,
                    level='INFO',
                    format='%(asctime)s. %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logs = pd.DataFrame()
class user_press():
    def __init__(self):
        self.flag = True


    def on_press(self,key):
        try:
            if str(key) == 'Key.ctrl_l' or str(key) == 'Key.ctrl_r' or str(key) == 'Key.ctrl':
                self.flag = False
            if self.flag == True:
                press = 'PRESS {0}'.format(key.char)
                logging.info(str(press))
            else:
                pass
        except AttributeError:
            press = 'PRESS {0}'.format(key)
            logging.info(str(press))


    def on_release(self,key):
        release = 'RELEASE {0}'.format(key)
        print(release)
        if key == keyboard.Key.esc:
            logs.to_csv('logs.csv')
            return False


    def start_lis(self):
        with keyboard.Listener(
                on_press = self.on_press,
                on_release = self.on_release
        ) as listener:
            listener.join()


    def loop_special_keys(self):
        if kb.is_pressed('ctrl+c'):
            logging.info('ctrl + C')
            time.sleep(0.5)
            self.flag = True
        elif kb.is_pressed('ctrl+v'):
            logging.info('ctrl + V')
            time.sleep(0.5)
            self.flag = True
        elif kb.is_pressed('ctrl+x'):
            logging.info('ctrl + X')
            time.sleep(0.5)
            self.flag = True


    def on_click(self,x, y, button, pressed):
        logging.info('Mouse_clicked') if pressed else print('Released')


    def mouse(self):
        with Listener(
                on_click = self.on_click) as listener:
            listener.join()


class action_logger():
    def __init__(self):
        self.path = os.path.abspath(psutil.Process(win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[-1]).name())
        self.tempWindowName = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        logging.info('Exe_file ' + self.path + '|' + self.tempWindowName)


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
            logging.info('Exe_file ' + self.path + '|' + tempWindowName)


def loop(obj_1,obj_2):
    while True:
        obj_1.check()
        obj_2.loop_special_keys()
        time.sleep(0.001)


if __name__ == '__main__':
    A_L = action_logger()
    U_P = user_press()
    keyboard_th = threading.Thread(target = U_P.start_lis)
    mouse_th = threading.Thread(target=U_P.mouse)
    exe_and_spec = threading.Thread(target = loop, args = (A_L,U_P,))
    keyboard_th.start()
    exe_and_spec.start()
    mouse_th.start()


