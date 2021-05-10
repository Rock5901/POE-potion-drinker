# POE-potion-drinker
Automation for potions in path of exile

Made by Rock :)

---------------------------------

You need Python 3.9.0 to use this script. You can install python from this link. (https://www.python.org/downloads/release/python-390/)
You also need AutoHotKey to use the .ahk scripts included in this folder. (https://www.autohotkey.com/)

---------------------------------

1. Run ModuleInstaller.ahk to install the required python modules for the script to function
2. Run PotionDrinkerStart.ahk to run the python file
3. Enjoy.

---------------------------------
Disabling Certain Potion SLots:

1. Edit PotionDrinker.py in notepad or any text editor
2. find Potion1.start() or any PotionNUMBER.start() that you want to diable
3. delete/comment the line " Potion1.start() "
4. This will prevent the thread from starting and the potion will never be touched.

---------------------------------

Keybinds:
Up-arrow = Pause  
Down-arrow = Exit Script
