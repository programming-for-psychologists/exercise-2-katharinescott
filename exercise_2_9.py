#See if you can figure out how to compute the response times, 
#measured from #the onset of the name, to the response 
#(Use psychopy timers)

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
        nameEntered=True

win = visual.Window([800,600],color="black", units='pix')
NameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
correct = visual.TextStim(win,text="O", height=40,color="green",pos=[0,0])
wrong = visual.TextStim(win,text="X",height=40,color="red",pos=[0,0])

time=core.Clock()

while nameEntered:
    nameShown = random.choice(firstNames) 
    NameStim.setText(nameShown) 
    NameStim.draw()
    win.flip()
    time.reset()
    answer = event.waitKeys(maxWait=1, keyList=['space'])
    if nameShown == userVar['Name']:
        correctAnswer = ['space']
    else:
        correctAnswer = None    
    if answer:
        rt = time.getTime()
    if answer != correctAnswer:
        wrong.draw()
        win.flip()
        core.wait(.5)

    if event.getKeys('q'):
    	break


