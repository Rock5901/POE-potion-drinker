from PIL import ImageGrab
from PIL import Image
from PIL import ImageFile
import sys
import autoit
import keyboard
import mouse
import time
import win32gui
import threading
import os



global pause 
pause = False
def MenuAndChat():
    image2 = ImageGrab.grab(bbox = (0, 0, 1920, 1080))
    rgb_im2 = image2.convert('RGB')
    chatR, chatG, chatB = rgb_im2.getpixel((630, 400))
    escapeR, escapeG, escapeB = rgb_im2.getpixel((904, 311))

    if chatR == 77 and  chatG == 5 and chatB == 1: # checks in chat is open
        return 'chatFalse'
    elif escapeR == 152 and escapeG == 108 and escapeB == 61: # checks if escape menu is open
        return 'menuFalse'


def Potion(xCord, yCord, potSlot):
    global pause
    while True:
        if pause == True:
                image = ImageGrab.grab(bbox = (300, 965, 540, 1080))
                rgb_im = image.convert('RGB')
                potionR, potionG, potionB = rgb_im.getpixel((xCord, yCord))

                if potionR == 249 and potionG == 215 and potionB == 153:
                    pass
                else:
                    poe = win32gui.FindWindow(None, 'Path Of Exile')
                    win32gui.SetForegroundWindow(poe)
                    #print('sending keystroke')
                    keyboard.send(str(potSlot))
                    image = ImageGrab.grab(bbox = (300, 965, 540, 1080))
                    rgb_im = image.convert('RGB')
                    potionR, potionG, potionB = rgb_im.getpixel((xCord, yCord))
                    if potionR == 249 and potionG == 215 and potionB == 153:
                        pass
                    else:
                        time.sleep(1)
        else:
            time.sleep(1)


def HotkeyChecker():
    while True:
        if keyboard.is_pressed('down'):
            print('quitting script')
            os._exit(1)
            time.sleep(1)
        if keyboard.is_pressed('up'):
            global pause
            if pause == True:
                print('pausing script')
                pause = False
            else:
                print('unpausing script')
                pause = True
            time.sleep(1)

        time.sleep(0.1)


if __name__ == '__main__':
    Hotkey = threading.Thread(target=HotkeyChecker, daemon=True)
    Potion1 = threading.Thread(target=Potion, daemon=True, args=(17, 108, 1))
    Potion2 = threading.Thread(target=Potion, daemon=True, args=(63, 108, 2))
    Potion3 = threading.Thread(target=Potion, daemon=True, args=(110, 108, 3))
    Potion4 = threading.Thread(target=Potion, daemon=True, args=(157, 108, 4))
    Potion5 = threading.Thread(target=Potion, daemon=True, args=(204, 108, 5))


    if not Hotkey.is_alive():
        print('starting hotkey')
        Hotkey.start()
    if not Potion1.is_alive():
        print('starting potion1')
        Potion1.start()
    if not Potion2.is_alive():
        print('starting potion2')
        Potion2.start()
    if not Potion3.is_alive():
        print('starting potion3')
        Potion3.start()
    if not Potion4.is_alive():
        print('starting potion4')
        Potion4.start()
    if not Potion5.is_alive():
        print('starting potion5')
        Potion5.start()
    while True:
        time.sleep(10000)











