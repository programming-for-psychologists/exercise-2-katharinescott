#Extend the task by requiring the subject to respond by 
#pressing a spacebar (the key is called 'space'), as quickly 
#as possible anytime the name on the screen matches the name 
#you entered into the box (so if I enter 'Gary' I would have to 
#press 'space' anytime the name 'Gary' shows up. If the participant 
#presses 'space' to the wrong name (false alarm), or misses the name 
#(a miss), show a red X.

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

nameEntered = False
while not nameEntered:
    gui.DlgFromDict(userVar)
    if userVar['Name'] not in firstNames: 
        popupError('Name does not exist')
    else:
        print userVar['Name']
        nameEntered=True

win = visual.Window([800,600],color="black", units='pix')
NameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
correct = visual.TextStim(win,text="O", height=40,color="green",pos=[0,0])
wrong = visual.TextStim(win,text="X",height=40,color="red",pos=[0,0])

while nameEntered:
    nameShown = random.choice(firstNames) 
    NameStim.setText(nameShown) 
    NameStim.draw()
    win.flip()
    if nameShown == userVar['Name']:
        correctAnswer = ['space']
    else:
        correctAnswer = None    
    answer = event.waitKeys(maxWait=.75, keyList='space')
    if answer != correctAnswer:
        wrong.draw()
        win.flip()
        core.wait(.5)
