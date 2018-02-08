#Do something new. Compare response times to first and 
#last names, measure effect of font face, etc.

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

time=core.Clock()

dataFile=open('file.txt','w')

while True:
    nameShown = random.choice(firstNames + lastNames) 
    NameStim.setText(nameShown) 
    NameStim.draw()
    win.flip()
    if nameShown in firstNames:
    	correctAnswer = ['f']
    if nameShown in lastNames:
    	correctAnswer = (['l'])
    answer = event.waitKeys(maxWait=1)
    if answer != correctAnswer:
    	wrong.draw()
    	rt=str(time.getTime())
    	hit='0'
    else:
    	correct.draw()
    	rt=str(time.getTime())
    	hit='1'
    win.flip()
    core.wait(.5)
    if event.getKeys(['q']):
        break
    data=('\t'.join([hit,rt])+'\n')
    dataFile.write(data)
    time.reset()    