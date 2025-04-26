from pynput.keyboard import Key, Listener
from pynput import keyboard
import time
import sys
import pymysql
import os
import string

class StopListener(Exception): pass

try:
    conn = pymysql.connect(host='192.168.19.134'
                                ,port=3306
                                ,user='Raiden'
                                ,passwd='raiden'
                                ,database='Raiden')
except:
    print('连接错误')
    sys.exit(1)

presskey = None  # Initialize presskey
new_press = False  # Initialize new_press
selected_table = None

with open('selected_table.txt','r')as f:
    selected_table = f.read().strip()
    print(selected_table)

os.remove('selected_table.txt')

def on_press(key):
    global press_time
    global diff_time
    global previous_time
    global presskey
    global RtoP_time
    global new_press
    if isinstance(key,keyboard.KeyCode) and (key.char.isalnum() or key.char in string.punctuation):
        presskey = key
        press_time = time.time()
        diff_time =press_time - previous_time
        previous_time = press_time
        RtoP_time = time.time() - release_time2
        new_press = True  # Set new_press to True when a key is pressed
    elif key == Key.enter:
        raise StopListener

    if new_press and selected_table:  # Only store data when a new key is pressed and a table is selected
        try:
            with conn.cursor() as cursor:
                sql = f"INSERT INTO {selected_table} (password_key, PtoP, RtoP) VALUES (%s, %s, %s)"
                cursor.execute(sql, (str(presskey), round(diff_time * 1000, 3), round(RtoP_time * 1000 , 3)))
            conn.commit()
            print("conn can be used")
        except Exception as e:
            print(f"Failed to store data: {e}")

    # ... existing code ...


def on_release(key):
    global release_time
    global release_time2
    global diff_time2
    global PtoR_time
    if isinstance(key, keyboard.KeyCode) and (key.char.isalnum() or key.char in string.punctuation):
        release_time = time.time()
        diff_time2 = release_time-release_time2
        release_time2 = release_time
        PtoR_time = time.time()-press_time

previous_time = time.time()
release_time2 = time.time()

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    if new_press:  # Only print when a new key is pressed
        print(presskey,diff_time,RtoP_time)
        with open('showdata.txt','a') as f:
            print(presskey,'P-P:',round(diff_time * 1000,3),'R-P:',round(RtoP_time * 1000 , 3),end='\n',file=f)
        new_press = False  # Reset new_press to False after printing
    if not listener.running:
        break
conn.close()
