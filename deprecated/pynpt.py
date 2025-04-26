from pynput.keyboard import Key, Listener
from pynput import keyboard
import time
import string

class keytimer:
    previous_key = None
    previous_press_time = 0
    previous_release_time = 0
    key = None
    press_time = 0
    release_time = 0

    def gaptime(a,b):
        c = (a-b)*1000
        c = round(c,3)
        return c

def on_press(key):
    if isinstance(key,keyboard.KeyCode) and (key.char.isalnum() or key.char in string.punctuation):
        if(keytimer.key != None):
            keytimer.previous_key,keytimer.key = keytimer.key,key
            keytimer.previous_press_time,keytimer.press_time = keytimer.press_time,time.time()
        else:
            keytimer.key = key
            keytimer.press_time = time.time()
        print("两键间隔")
        print(keytimer.gaptime(keytimer.press_time,keytimer.previous_release_time))
        print("两键时间")
        print(keytimer.gaptime(keytimer.press_time,keytimer.previous_press_time))

def on_release(key):
    if isinstance(key, keyboard.KeyCode) and (key.char.isalnum() or key.char in string.punctuation):
        if(keytimer.key != None):
            keytimer.previous_key,keytimer.key = keytimer.key,key
            keytimer.previous_release_time,keytimer.release_time = keytimer.release_time,time.time()
        else:
            keytimer.key = key
            keytimer.release_time = time.time()



def main():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()
    # while True:
    #     print(keytimer.gaptime(keytimer.first_press,keytimer.second_press))
    #     print(keytimer.gaptime(keytimer.first_release,keytimer.second_release))


main()