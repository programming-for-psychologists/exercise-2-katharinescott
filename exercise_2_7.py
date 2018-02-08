
#Pop up a box that accepts a first name, and check to make 
#sure that the name exists. If it doesn't, pop-up a 'Name 
#does not exist'error box

import time
import sys
import random
from psychopy import visual,event,core,gui

def popupError(text):
    errorDlg = gui.Dlg(title="Error",pos=(200,400))
    errorDlg.addText('Error: '+text,color='Red')
    errorDlg.show()

names = open('names.txt', 'r').readlines() 
firstNames = [name.split(' ')[0] for name in names]
userVar = {'Name': 'Enter your name'}


nameentered = False
while not nameentered:
    gui.DlgFromDict(userVar)
    if userVar['Name'] not in firstNames: 
        popupError('Name does not exist')
    else:
        print userVar['Name']
        nameentered=True
