import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines() 
#r means open for reading. Ensures that you don't override it. 
#read it in to 'names' which will become a list of strings where each line of the file is a string.
firstNames = [name.split(' ')[0] for name in names]
#list comprehension. This is identical to the longer bit of code below. 
#Rather than writing a list, iterating over names, and appending to names, you just do this in one line.
#splits by the character defined and write the values into the list. Then you can grab just the first, second, last, etc value 

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
#this is a text stimulus now. 
while True:
    nameShown = random.choice(firstNames) #set text to a random name. to get things to randomize you have to import the random module. random.choice expects a list as an argument. 
    firstNameStim.setText(nameShown) 
    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        break