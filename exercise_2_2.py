import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines() 
lastNames = [name.split(' ')[1] for name in names]


win = visual.Window([800,600],color="black", units='pix')
lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
while True:
    nameShown = random.choice(lastNames) #set text to a random name. to get things to randomize you have to import the random module. random.choice expects a list as an argument. 
    lastNameStim.setText(nameShown) 
    lastNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        break