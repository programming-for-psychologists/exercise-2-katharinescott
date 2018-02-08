#Output the response times (in ms, e.g., 453 for 453 ms) 
#and accuracy (1 for correct, 0 for incorrect) to a file 
#output.txt. Output one line per trial: each line should 
#contain the accuracy (1 or 0) and the response time 
#(in milliseconds). See the python documentation for 
#examples of how to write to a file. Ask for help if you 
#are stuck.

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

fileName=userVar['Name']
file =str(fileName)+'.txt'
dataFile=open(file,'w')

while nameEntered:
    nameShown = random.choice(firstNames) 
    NameStim.setText(nameShown) 
    NameStim.draw()
    win.flip()
    if nameShown == userVar['Name']:
        correctAnswer = ['space']
    else:
        correctAnswer = None    
    answer = event.waitKeys(maxWait=1, keyList=['space'])
    if answer != correctAnswer:
        wrong.draw()
        win.flip()
        core.wait(.5)
        rt=str(time.getTime())
        hit ='0'
    else:
        rt=str(time.getTime())
        hit ='1'
    if event.getKeys('q'):
        break
    data=('\t'.join([hit,rt])+'\n')
    dataFile.write(data)
    time.reset()


