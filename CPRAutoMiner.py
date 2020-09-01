#CPRAutoMiner.py

from PIL import ImageGrab
import pyautogui 
import time
import random 

time.sleep(5)
missclick=None

def moving_actions(): #Determine a random area on screen and use PyAutoGui to click
    x=random.randint(470,1000)
    y=random.randint(545,730)
    pyautogui.moveTo(x,y)
    pyautogui.click()
    return

def check_screen(): #Use PIL to check screen if another character was clicked on 
    global missclick
    image=ImageGrab.grab()
    (r,g,b,a)=image.getpixel((565,195))
    if (r,g,b,a)==(0,123,208,255): #If a blue character card pops up click out of it
        pyautogui.click(610,210)
        missclick=True
    else:
        missclick=False
    return
    

def mining_action(): #Finish character action by mining 
    time.sleep(2)
    pyautogui.press("d")
    time.sleep(12)
    return


def main():
    while True:
        moving_actions()
        check_screen()
        if missclick==True: #restart loop if another character was clicked on
            continue
        mining_action()
    
main()
