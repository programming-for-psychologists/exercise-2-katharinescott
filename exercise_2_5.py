#Now let's implement some feedback. Let's allow either a 
#'f' or 'l' response for each trial. If the response is correct, 
#show a green 'O' before the start of the next trial. If the response 
#is wrong, show a red 'X' (you can use textStim objects for feedback). 
#Show the feedback for 500 ms. Note: we have someone in a class whose 
#last name is a common first name. If this were an experiment, how might 
#his affect responses?


import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines() 
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1] for name in names]

win = visual.Window([800,600],color="black", units='pix')
NameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
correct = visual.TextStim(win,text="O", height=40,color="green",pos=[0,0])
wrong = visual.TextStim(win,text="X",height=40,color="red",pos=[0,0])
answers = ['f','l']

while True:
    nameShown = random.choice(firstNames + lastNames) 
    NameStim.setText(nameShown) 
    NameStim.draw()
    win.flip()
    if nameShown in firstNames:
    	correctAnswer = ['f']
    if nameShown in lastNames:
    	correctAnswer = (['l'])
    answer = event.waitKeys(keyList=answers)
    if answer == correctAnswer:
    	correct.draw()
    else:
    	wrong.draw()
    win.flip()
    core.wait(.5)
    if event.getKeys(['q']):
        break