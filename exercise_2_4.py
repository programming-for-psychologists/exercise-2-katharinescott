
#Pop up a box that accepts a first name, and check to make 
#sure that the name exists. If it doesn't, pop-up a 'Name 
#does not exist'error box

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines() 
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1] for name in names]

win = visual.Window([800,600],color="black", units='pix')
NameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])

while True:
    nameShown = random.choice(firstNames + lastNames) 
    NameStim.setText(nameShown) 
    NameStim.draw()
    win.flip()
    if nameShown in firstNames:
        event.waitKeys(keyList='f')
    if nameShown in lastNames:
        event.waitKeys(keyList='l')
    win.flip()
    core.wait(.15)