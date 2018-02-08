import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines() 
firstNames = [name.split(' ')[0] for name in names]

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
cross = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])

while True:
    cross.draw()
    win.flip()
    core.wait(.50)
    nameShown = random.choice(firstNames) #set text to a random name. to get things to randomize you have to import the random module. random.choice expects a list as an argument. 
    firstNameStim.setText(nameShown) 
    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        break