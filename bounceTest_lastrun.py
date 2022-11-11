#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.9),
    on January 25, 2021, at 20:13
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020.2.9')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.9'
expName = 'bounceTest'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'ballSpeedPar': '0.05', 'wallType': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Vu\\Downloads\\Work\\squashcatch\\bounceTest_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()
cursorColor = [-1,-1,-1]
tasksNum = 0
hitTotal = 0
hitCounter = 0
pointsTotal = 0
pointsCounter = 0
hitPercent = -1
trialRepeat = 0
horOrTilt = int(expInfo['wallType'])

# Initialize components for Routine "instr"
instrClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instrStats = visual.TextStim(win=win, name='instrStats',
    text=None,
    font='Arial',
    pos=(0.0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instrRepeat = visual.TextStim(win=win, name='instrRepeat',
    text=None,
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
instrResp = keyboard.Keyboard()

# Initialize components for Routine "fix"
fixClock = core.Clock()
fixMouse = event.Mouse(win=win)
x, y = [None, None]
fixMouse.mouseClock = core.Clock()
fixCursor = visual.Rect(
    win=win, name='fixCursor',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
fixCircle = visual.Polygon(
    win=win, name='fixCircle',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,0.004,1.000], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
feedbackText = visual.TextStim(win=win, name='feedbackText',
    text=None,
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
fixText = visual.TextStim(win=win, name='fixText',
    text=None,
    font='Arial',
    pos=(0, 0.0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
fixArrow = visual.TextStim(win=win, name='fixArrow',
    text=None,
    font='Arial',
    pos=(0, -0.2), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
fixPoints = visual.TextStim(win=win, name='fixPoints',
    text=None,
    font='Arial',
    pos=(-0.4, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
fixHits = visual.TextStim(win=win, name='fixHits',
    text=None,
    font='Arial',
    pos=(0.4, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
fixSkip = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialMouse = event.Mouse(win=win)
x, y = [None, None]
trialMouse.mouseClock = core.Clock()
trialWall = visual.Rect(
    win=win, name='trialWall',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(0, 0.3),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
trialCursor = visual.Rect(
    win=win, name='trialCursor',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
trialCircle = visual.Polygon(
    win=win, name='trialCircle',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
trialHits = visual.TextStim(win=win, name='trialHits',
    text=None,
    font='Arial',
    pos=(0.4, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
trialPoints = visual.TextStim(win=win, name='trialPoints',
    text=None,
    font='Arial',
    pos=(-0.4, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
trialSkip = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='This is the end of the experiment. Thank you for your time. Please remember to return to the questionnaire to carry on with the study. Press ‘space’ to exit.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
endHits = visual.TextStim(win=win, name='endHits',
    text=None,
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
endPoints = visual.TextStim(win=win, name='endPoints',
    text=None,
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
endResp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
tasks = data.TrialHandler(nReps=40, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='tasks')
thisExp.addLoop(tasks)  # add the loop to the experiment
thisTask = tasks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
if thisTask != None:
    for paramName in thisTask:
        exec('{} = thisTask[paramName]'.format(paramName))

for thisTask in tasks:
    currentLoop = tasks
    # abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
    if thisTask != None:
        for paramName in thisTask:
            exec('{} = thisTask[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    # check how many repeated trials
    if trialRepeat == 4:
        tasksNum = tasksNum + 1
        trialRepeat = 1
    # check if over 60%
    if hitPercent >= 60 or hitPercent == -1:
        tasksNum = tasksNum + 1
        trialRepeat = trialRepeat + 1
    # check if over max number of blocks
    if tasksNum >= 9:
        continueRoutine = False
    # initial variables
    trialsType = 0
    trialsNum = 0
    ballConnectX = 1.5
    ballConnectY = 1.5
    hitOrMiss = "null"
    cursorColor = [-1,-1,-1]
    interceptBall = 0
    interceptPaddle = 0
    interceptDelta = 0
    pointsTotal = pointsTotal + pointsCounter
    hitTotal = hitTotal + hitCounter
    
    instrRepeat.text = "Repeats: " + str(trialRepeat)
    
    # values to change for ball speed
    if tasksNum == 1:
        ballSpeed = 0.03
    elif tasksNum == 2:
        ballSpeed = 0.04
    else:
         ballSpeed = 0.05
    
    #Determines what messages show up
    if tasksNum == 1:
        instrText.text = "Catch the ball for 50 trials. There is a break period from when you catch/miss the ball to when the trial starts again. First is a practice block. Press 'space' to to continue."
        instrStats.text = ""
    else:
        instrText.text = "Again, catch the ball for 50 trials. There is a break period from when you catch/miss the ball to when the trial starts again. Next up are real trial blocks. Press 'space' to to continue."
        instrStats.text = "Hits: " + str(hitCounter) + " / 50\nPoints: " + str(pointsCounter)
    
    # Determines whether trial starts on left or right
    trialArr = []
    for i in range(50):
        if i % 2 == 0:
            trialArr.append(0)
        else:
            trialArr.append(1)
    
    shuffle(trialArr)
    instrResp.keys = []
    instrResp.rt = []
    _instrResp_allKeys = []
    # keep track of which components have finished
    instrComponents = [instrText, instrStats, instrRepeat, instrResp]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrText* updates
        if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrText.frameNStart = frameN  # exact frame index
            instrText.tStart = t  # local t and not account for scr refresh
            instrText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
            instrText.setAutoDraw(True)
        
        # *instrStats* updates
        if instrStats.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrStats.frameNStart = frameN  # exact frame index
            instrStats.tStart = t  # local t and not account for scr refresh
            instrStats.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrStats, 'tStartRefresh')  # time at next scr refresh
            instrStats.setAutoDraw(True)
        
        # *instrRepeat* updates
        if instrRepeat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrRepeat.frameNStart = frameN  # exact frame index
            instrRepeat.tStart = t  # local t and not account for scr refresh
            instrRepeat.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrRepeat, 'tStartRefresh')  # time at next scr refresh
            instrRepeat.setAutoDraw(True)
        if instrRepeat.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instrRepeat.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                instrRepeat.tStop = t  # not accounting for scr refresh
                instrRepeat.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instrRepeat, 'tStopRefresh')  # time at next scr refresh
                instrRepeat.setAutoDraw(False)
        
        # *instrResp* updates
        waitOnFlip = False
        if instrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrResp.frameNStart = frameN  # exact frame index
            instrResp.tStart = t  # local t and not account for scr refresh
            instrResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrResp, 'tStartRefresh')  # time at next scr refresh
            instrResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instrResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instrResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instrResp.status == STARTED and not waitOnFlip:
            theseKeys = instrResp.getKeys(keyList=['space'], waitRelease=False)
            _instrResp_allKeys.extend(theseKeys)
            if len(_instrResp_allKeys):
                instrResp.keys = _instrResp_allKeys[-1].name  # just the last key pressed
                instrResp.rt = _instrResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    hitCounter = 0
    pointsCounter = 0
    hitPercent = 0
    tasks.addData('instrText.started', instrText.tStartRefresh)
    tasks.addData('instrText.stopped', instrText.tStopRefresh)
    tasks.addData('instrStats.started', instrStats.tStartRefresh)
    tasks.addData('instrStats.stopped', instrStats.tStopRefresh)
    tasks.addData('instrRepeat.started', instrRepeat.tStartRefresh)
    tasks.addData('instrRepeat.stopped', instrRepeat.tStopRefresh)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=50, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fix"-------
        continueRoutine = True
        # update component parameters for each repeat
        # check to end
        if tasksNum >= 9:
            continueRoutine = False
        # initial variables
        bouncePointChoice = trialArr[trialsNum]
        homeX = -1.0
        homeY = -0.3
        trialFlag = 0
        fixFlag = 0
        pointsGiven = 0
        
        timerCount = 0
        
        # intial angle control
        theta = (pi * (0 / 180))
        sinTheta = sin(theta)
        
        # paddle variables
        paddleX = 0.075
        paddleY = 0.0125
        fixCursor.vertices = [(-paddleX,-paddleY),(-paddleX,paddleY),(paddleX,paddleY),(paddleX,-paddleY)]
        cursorPosX = trialMouse.getPos()[0]
        cursorPosY = (sqrt(((trialMouse.getPos()[0] - homeX)**2)+((trialMouse.getPos()[1] - homeY)**2))*(sinTheta) + homeY)
        
        # text control
        if trialsNum == 0:
            feedbackText.text = "Get ready!"
        else:
            feedbackText.text = hitOrMiss + "    Off-midpaddle-by: " + str(round(interceptDelta, 4))
            
        if bouncePointChoice == 0 and tasksNum == 1:
            fixText.text = "Move left for 1 second to start."
            fixArrow.text = "<="
        elif bouncePointChoice == 1 and tasksNum == 1:
            fixText.text = "Move right for 1 second to start."
            fixArrow.text = "=>"
        elif bouncePointChoice == 0:
            fixText.text = ""
            fixArrow.text = "<="
        else:
            fixText.text = ""
            fixArrow.text = "=>"
            
        # paddle color andd points control
        if hitOrMiss == "hit" and interceptDelta <= 0.025 and interceptDelta > -0.03 and trialsNum >= 1:
            cursorColor = [-1,1.0,-1]
            pointsCounter = pointsCounter + 10
            pointsGiven = 10
        elif hitOrMiss == "hit" and trialsNum >= 1:
            cursorColor = [1.000,0.004,-1.000]
            pointsCounter = pointsCounter + 5
            pointsGiven = 5
        elif hitOrMiss == "miss" and trialsNum >= 1:
            cursorColor = [1.0,-1,-1]
            pointsGiven = 0
        else:
            cursorColor = [-1.0,-1.0,-1.0]
        
        # hit/point counters
        fixPoints.text = "Points: " + str(pointsCounter)
        fixHits.text = "Hits: " + str(hitCounter)
        
        # markers for edges
        leftEdge = -0.45
        rightEdge = 0.45
        
        
        
        
        # setup some python lists for storing info about the fixMouse
        fixMouse.x = []
        fixMouse.y = []
        fixMouse.leftButton = []
        fixMouse.midButton = []
        fixMouse.rightButton = []
        fixMouse.time = []
        gotValidClick = False  # until a click is received
        fixMouse.mouseClock.reset()
        fixCursor.setFillColor(cursorColor)
        fixCursor.setLineColor(cursorColor)
        fixSkip.keys = []
        fixSkip.rt = []
        _fixSkip_allKeys = []
        # keep track of which components have finished
        fixComponents = [fixMouse, fixCursor, fixCircle, feedbackText, fixText, fixArrow, fixPoints, fixHits, fixSkip]
        for thisComponent in fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix"-------
        while continueRoutine:
            # get current time
            t = fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            cursorPosX = trialMouse.getPos()[0]
            cursorPosY = (sqrt(((trialMouse.getPos()[0] - homeX)**2)+((trialMouse.getPos()[1] - homeY)**2))*(sinTheta) + homeY)
            
            if bouncePointChoice == 0:
                if fixMouse.getPos()[0] <= leftEdge:
                    timerCount = timerCount + 1
                    if timerCount == 60:
                        continueRoutine = False
            else:
                if fixMouse.getPos()[0] >= rightEdge:
                    timerCount = timerCount + 1
                    if timerCount == 60:
                        continueRoutine = False
                        
            if fixFlag == 0:
                ballConnectX = ballConnectX + 0.0001
                fixFlag = 1
            else:
                ballConnectX = ballConnectX - 0.0001
                fixFlag = 0
            # *fixMouse* updates
            if fixMouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixMouse.frameNStart = frameN  # exact frame index
                fixMouse.tStart = t  # local t and not account for scr refresh
                fixMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixMouse, 'tStartRefresh')  # time at next scr refresh
                fixMouse.status = STARTED
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if fixMouse.status == STARTED:  # only update if started and not finished!
                x, y = fixMouse.getPos()
                fixMouse.x.append(x)
                fixMouse.y.append(y)
                buttons = fixMouse.getPressed()
                fixMouse.leftButton.append(buttons[0])
                fixMouse.midButton.append(buttons[1])
                fixMouse.rightButton.append(buttons[2])
                fixMouse.time.append(fixMouse.mouseClock.getTime())
            
            # *fixCursor* updates
            if fixCursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixCursor.frameNStart = frameN  # exact frame index
                fixCursor.tStart = t  # local t and not account for scr refresh
                fixCursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixCursor, 'tStartRefresh')  # time at next scr refresh
                fixCursor.setAutoDraw(True)
            if fixCursor.status == STARTED:  # only update if drawing
                fixCursor.setPos((cursorPosX, cursorPosY))
            
            # *fixCircle* updates
            if fixCircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixCircle.frameNStart = frameN  # exact frame index
                fixCircle.tStart = t  # local t and not account for scr refresh
                fixCircle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixCircle, 'tStartRefresh')  # time at next scr refresh
                fixCircle.setAutoDraw(True)
            if fixCircle.status == STARTED:  # only update if drawing
                fixCircle.setPos((ballConnectX, ballConnectY))
            
            # *feedbackText* updates
            if feedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackText.frameNStart = frameN  # exact frame index
                feedbackText.tStart = t  # local t and not account for scr refresh
                feedbackText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackText, 'tStartRefresh')  # time at next scr refresh
                feedbackText.setAutoDraw(True)
            
            # *fixText* updates
            if fixText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixText.frameNStart = frameN  # exact frame index
                fixText.tStart = t  # local t and not account for scr refresh
                fixText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixText, 'tStartRefresh')  # time at next scr refresh
                fixText.setAutoDraw(True)
            
            # *fixArrow* updates
            if fixArrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixArrow.frameNStart = frameN  # exact frame index
                fixArrow.tStart = t  # local t and not account for scr refresh
                fixArrow.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixArrow, 'tStartRefresh')  # time at next scr refresh
                fixArrow.setAutoDraw(True)
            
            # *fixPoints* updates
            if fixPoints.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixPoints.frameNStart = frameN  # exact frame index
                fixPoints.tStart = t  # local t and not account for scr refresh
                fixPoints.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixPoints, 'tStartRefresh')  # time at next scr refresh
                fixPoints.setAutoDraw(True)
            
            # *fixHits* updates
            if fixHits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixHits.frameNStart = frameN  # exact frame index
                fixHits.tStart = t  # local t and not account for scr refresh
                fixHits.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixHits, 'tStartRefresh')  # time at next scr refresh
                fixHits.setAutoDraw(True)
            
            # *fixSkip* updates
            waitOnFlip = False
            if fixSkip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixSkip.frameNStart = frameN  # exact frame index
                fixSkip.tStart = t  # local t and not account for scr refresh
                fixSkip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixSkip, 'tStartRefresh')  # time at next scr refresh
                fixSkip.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(fixSkip.clock.reset)  # t=0 on next screen flip
            if fixSkip.status == STARTED and not waitOnFlip:
                theseKeys = fixSkip.getKeys(keyList=['s', 'k', 'space'], waitRelease=False)
                _fixSkip_allKeys.extend(theseKeys)
                if len(_fixSkip_allKeys):
                    fixSkip.keys = _fixSkip_allKeys[-1].name  # just the last key pressed
                    fixSkip.rt = _fixSkip_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix"-------
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('pointsGiven', pointsGiven)
        # store data for trials (TrialHandler)
        trials.addData('fixMouse.x', fixMouse.x)
        trials.addData('fixMouse.y', fixMouse.y)
        trials.addData('fixMouse.leftButton', fixMouse.leftButton)
        trials.addData('fixMouse.midButton', fixMouse.midButton)
        trials.addData('fixMouse.rightButton', fixMouse.rightButton)
        trials.addData('fixMouse.time', fixMouse.time)
        trials.addData('fixMouse.started', fixMouse.tStartRefresh)
        trials.addData('fixMouse.stopped', fixMouse.tStopRefresh)
        trials.addData('fixCursor.started', fixCursor.tStartRefresh)
        trials.addData('fixCursor.stopped', fixCursor.tStopRefresh)
        trials.addData('fixCircle.started', fixCircle.tStartRefresh)
        trials.addData('fixCircle.stopped', fixCircle.tStopRefresh)
        trials.addData('feedbackText.started', feedbackText.tStartRefresh)
        trials.addData('feedbackText.stopped', feedbackText.tStopRefresh)
        trials.addData('fixText.started', fixText.tStartRefresh)
        trials.addData('fixText.stopped', fixText.tStopRefresh)
        trials.addData('fixArrow.started', fixArrow.tStartRefresh)
        trials.addData('fixArrow.stopped', fixArrow.tStopRefresh)
        trials.addData('fixPoints.started', fixPoints.tStartRefresh)
        trials.addData('fixPoints.stopped', fixPoints.tStopRefresh)
        trials.addData('fixHits.started', fixHits.tStartRefresh)
        trials.addData('fixHits.stopped', fixHits.tStopRefresh)
        # the Routine "fix" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        # check to end
        if tasksNum >= 9:
            continueRoutine = False
        
        # controls paddle positioning
        homeX = -1.0
        homeY = -0.3
        
        # don't touch
        bounceDir = 0
        wallBounceX = 0
        wallBounceY = 0
        
        trialPoints.text = "Points: " + str(pointsCounter)
        trialHits.text = "Hits: " + str(hitCounter)
        
        # angle info
        perturbation = [(pi/20)*2]
        alpha = [70, 75, 80, 85]
            
        if horOrTilt == 1 and tasksNum >= 5:
            trialWall.ori = 0
        elif horOrTilt == 2 and bouncePointChoice == 0 and tasksNum >= 5:
            trialWall.ori = 9
        elif horOrTilt == 2 and bouncePointChoice == 1 and tasksNum >= 5:
            trialWall.ori = 351
            
        if tasksNum >= 5:
            pertChoice = perturbation[0]
            
        if bouncePointChoice == 0:
            # randint max should equal len(alpha)
            alphaChoice = alpha[0+randint(0, 4)]
            choice90 = 90
            choice180 = 180
        else:
            alphaChoice = -(alpha[0+randint(0, 4)])
            choice90 = -90
            choice180 = -180
            pertChoice = -(pertChoice)
        
        theta = (pi * (0 / 180))
        cosTheta = cos(theta)
        sinTheta = sin(theta)
        
        alphaRad = pi * (alphaChoice/180)
        tanAlpha = tan(alphaRad)
        
        betaChoice = choice180 - (choice90 + alphaChoice)
        betaRad = pi * (betaChoice/180)
        tanBeta = tan(betaRad + pertChoice)
        
        # X bounce point is always 0.0
        bouncePointX = 0.0
        # Y bounce point is always 0.3
        bouncePointY = 0.3
        launchLineX = 0.6/(tanAlpha)
        # Y launch line is always 0.6
        launchLineY = 0.6
        bouncePathX = bouncePointX - launchLineX
        # Y starting position is always -0.5
        bouncePathY = -0.3
        
        launchLineXP = 0.6 * tanBeta
        
        # arrays to store info
        bounceDirArr = []
        ballPosX = []
        ballPosY = []
        paddlePosX = []
        paddlePosY = []
        
        # other things to keep track of
        trialsType = 0
        trialsNum = trialsNum + 1
        hitOrMiss = "miss"
        
        # values to change for paddle size
        paddleX = 0.075
        paddleY = 0.0125
        trialCursor.vertices = [(-paddleX,-paddleY),(-paddleX,paddleY),(paddleX,paddleY),(paddleX,-paddleY)]
        # values to change for wall size
        wallX = 0.5
        wallY = 0.0125
        trialWall.vertices = [(-wallX,-wallY),(-wallX,wallY),(wallX,wallY),(wallX,-wallY)]
        
        # initial calculations for mouse
        cursorPosX = trialMouse.getPos()[0]
        cursorPosY = (sqrt(((trialMouse.getPos()[0] - homeX)**2)+((trialMouse.getPos()[1] - homeY)**2))*(sinTheta) + homeY)
        # setup some python lists for storing info about the trialMouse
        trialMouse.x = []
        trialMouse.y = []
        trialMouse.leftButton = []
        trialMouse.midButton = []
        trialMouse.rightButton = []
        trialMouse.time = []
        gotValidClick = False  # until a click is received
        trialMouse.mouseClock.reset()
        trialSkip.keys = []
        trialSkip.rt = []
        _trialSkip_allKeys = []
        # keep track of which components have finished
        trialComponents = [trialMouse, trialWall, trialCursor, trialCircle, trialHits, trialPoints, trialSkip]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if event.getKeys() != []:
                hitCounter = hitCounter + 1
            cursorPosX = trialMouse.getPos()[0]
            cursorPosY = (sqrt(((trialMouse.getPos()[0] - homeX)**2)+((trialMouse.getPos()[1] - homeY)**2))*(sinTheta) + homeY)
            
            bounceDirArr.append(bounceDir)
            ballPosX.append(bouncePathX)
            ballPosY.append(bouncePathY)
            paddlePosX.append(cursorPosX)
            paddlePosY.append(cursorPosY)
            
            if ((bouncePathX >= cursorPosX - paddleX) and (bouncePathY >= cursorPosY - paddleY) and  (bouncePathX <= cursorPosX + paddleX) and (bouncePathY <= cursorPosY + paddleY)) and (bounceDir == 1):
                hitOrMiss = "hit"
                hitCounter = hitCounter + 1
                ballConnectX = bouncePathX;
                ballConnectY = bouncePathY;
                continueRoutine = False
            elif (bouncePathX <= -1.0) or (bouncePathY <= -1.0) or (bouncePathX >= 1.0) or (bouncePathY >= 1.0):
                hitOrMiss = "miss"
                ballConnectX = bouncePathX;
                ballConnectY = bouncePathY;
                continueRoutine = False
            
            if (bounceDir == 0):
                bouncePathX = bouncePathX + launchLineX*ballSpeed
                bouncePathY = bouncePathY + launchLineY*ballSpeed
            elif (bounceDir == 1) and tasksNum <= 4:
                bouncePathX = bouncePathX + launchLineX*ballSpeed
                bouncePathY = bouncePathY - launchLineY*ballSpeed
            elif (bounceDir == 1) and tasksNum >= 5:
                bouncePathX = bouncePathX + launchLineXP*ballSpeed
                bouncePathY = bouncePathY - launchLineY*ballSpeed
                
            if bouncePathY <= -0.29 and (bounceDir == 1) and (trialFlag == 0):
                interceptBall = bouncePathX
                interceptPaddle = cursorPosX
                trialFlag = 1
                
            if (bouncePathY >= bouncePointY) and (bounceDir == 0):
                bounceDir = 1
                wallBounceX = bouncePathX
                wallBounceY = bouncePathY
            
                
            
            # *trialMouse* updates
            if trialMouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialMouse.frameNStart = frameN  # exact frame index
                trialMouse.tStart = t  # local t and not account for scr refresh
                trialMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialMouse, 'tStartRefresh')  # time at next scr refresh
                trialMouse.status = STARTED
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if trialMouse.status == STARTED:  # only update if started and not finished!
                x, y = trialMouse.getPos()
                trialMouse.x.append(x)
                trialMouse.y.append(y)
                buttons = trialMouse.getPressed()
                trialMouse.leftButton.append(buttons[0])
                trialMouse.midButton.append(buttons[1])
                trialMouse.rightButton.append(buttons[2])
                trialMouse.time.append(trialMouse.mouseClock.getTime())
            
            # *trialWall* updates
            if trialWall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialWall.frameNStart = frameN  # exact frame index
                trialWall.tStart = t  # local t and not account for scr refresh
                trialWall.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialWall, 'tStartRefresh')  # time at next scr refresh
                trialWall.setAutoDraw(True)
            
            # *trialCursor* updates
            if trialCursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialCursor.frameNStart = frameN  # exact frame index
                trialCursor.tStart = t  # local t and not account for scr refresh
                trialCursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialCursor, 'tStartRefresh')  # time at next scr refresh
                trialCursor.setAutoDraw(True)
            if trialCursor.status == STARTED:  # only update if drawing
                trialCursor.setPos((cursorPosX, cursorPosY))
            
            # *trialCircle* updates
            if trialCircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialCircle.frameNStart = frameN  # exact frame index
                trialCircle.tStart = t  # local t and not account for scr refresh
                trialCircle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialCircle, 'tStartRefresh')  # time at next scr refresh
                trialCircle.setAutoDraw(True)
            if trialCircle.status == STARTED:  # only update if drawing
                trialCircle.setPos((bouncePathX, bouncePathY))
            
            # *trialHits* updates
            if trialHits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialHits.frameNStart = frameN  # exact frame index
                trialHits.tStart = t  # local t and not account for scr refresh
                trialHits.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialHits, 'tStartRefresh')  # time at next scr refresh
                trialHits.setAutoDraw(True)
            
            # *trialPoints* updates
            if trialPoints.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialPoints.frameNStart = frameN  # exact frame index
                trialPoints.tStart = t  # local t and not account for scr refresh
                trialPoints.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialPoints, 'tStartRefresh')  # time at next scr refresh
                trialPoints.setAutoDraw(True)
            
            # *trialSkip* updates
            waitOnFlip = False
            if trialSkip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialSkip.frameNStart = frameN  # exact frame index
                trialSkip.tStart = t  # local t and not account for scr refresh
                trialSkip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialSkip, 'tStartRefresh')  # time at next scr refresh
                trialSkip.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trialSkip.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trialSkip.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trialSkip.status == STARTED and not waitOnFlip:
                theseKeys = trialSkip.getKeys(keyList=['s', 'k', 'space'], waitRelease=False)
                _trialSkip_allKeys.extend(theseKeys)
                if len(_trialSkip_allKeys):
                    trialSkip.keys = _trialSkip_allKeys[-1].name  # just the last key pressed
                    trialSkip.rt = _trialSkip_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('bounceDirArr', bounceDirArr)
        thisExp.addData('ballPosX', ballPosX)
        thisExp.addData('ballPosY', ballPosY)
        thisExp.addData('paddlePosX', paddlePosX)
        thisExp.addData('paddlePosY', paddlePosY)
        thisExp.addData('alphaChoice', alphaChoice)
        thisExp.addData('pertChoice', pertChoice)
        thisExp.addData('horOrTilt', horOrTilt)
        thisExp.addData('hitOrMiss', hitOrMiss)
        thisExp.addData('trialsType', trialsType)
        thisExp.addData('trialsNum', trialsNum)
        thisExp.addData('tasksNum', tasksNum)
        interceptDelta = interceptBall - interceptPaddle
        thisExp.addData('interceptBall', interceptBall)
        thisExp.addData('interceptPaddle', interceptPaddle)
        thisExp.addData('interceptDelta', interceptDelta)
        thisExp.addData('wallBounceX', wallBounceX)
        thisExp.addData('wallBounceY', wallBounceY)
        thisExp.addData('cumulativetime', globalClock.getTime())
        hitPercent = hitCounter / 50
        
        # store data for trials (TrialHandler)
        trials.addData('trialMouse.x', trialMouse.x)
        trials.addData('trialMouse.y', trialMouse.y)
        trials.addData('trialMouse.leftButton', trialMouse.leftButton)
        trials.addData('trialMouse.midButton', trialMouse.midButton)
        trials.addData('trialMouse.rightButton', trialMouse.rightButton)
        trials.addData('trialMouse.time', trialMouse.time)
        trials.addData('trialMouse.started', trialMouse.tStartRefresh)
        trials.addData('trialMouse.stopped', trialMouse.tStopRefresh)
        trials.addData('trialWall.started', trialWall.tStartRefresh)
        trials.addData('trialWall.stopped', trialWall.tStopRefresh)
        trials.addData('trialCursor.started', trialCursor.tStartRefresh)
        trials.addData('trialCursor.stopped', trialCursor.tStopRefresh)
        trials.addData('trialCircle.started', trialCircle.tStartRefresh)
        trials.addData('trialCircle.stopped', trialCircle.tStopRefresh)
        trials.addData('trialHits.started', trialHits.tStartRefresh)
        trials.addData('trialHits.stopped', trialHits.tStopRefresh)
        trials.addData('trialPoints.started', trialPoints.tStartRefresh)
        trials.addData('trialPoints.stopped', trialPoints.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 50 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 40 repeats of 'tasks'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
endHits.text = "Total Hits: " + str(hitTotal + hitCounter) + " / 80"
endPoints.text = "Total Points: " + str(pointsTotal + pointsCounter)
endResp.keys = []
endResp.rt = []
_endResp_allKeys = []
# keep track of which components have finished
endComponents = [endText, endHits, endPoints, endResp]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    
    # *endHits* updates
    if endHits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endHits.frameNStart = frameN  # exact frame index
        endHits.tStart = t  # local t and not account for scr refresh
        endHits.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endHits, 'tStartRefresh')  # time at next scr refresh
        endHits.setAutoDraw(True)
    
    # *endPoints* updates
    if endPoints.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endPoints.frameNStart = frameN  # exact frame index
        endPoints.tStart = t  # local t and not account for scr refresh
        endPoints.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endPoints, 'tStartRefresh')  # time at next scr refresh
        endPoints.setAutoDraw(True)
    
    # *endResp* updates
    waitOnFlip = False
    if endResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endResp.frameNStart = frameN  # exact frame index
        endResp.tStart = t  # local t and not account for scr refresh
        endResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endResp, 'tStartRefresh')  # time at next scr refresh
        endResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endResp.status == STARTED and not waitOnFlip:
        theseKeys = endResp.getKeys(keyList=['space'], waitRelease=False)
        _endResp_allKeys.extend(theseKeys)
        if len(_endResp_allKeys):
            endResp.keys = _endResp_allKeys[-1].name  # just the last key pressed
            endResp.rt = _endResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endText.started', endText.tStartRefresh)
thisExp.addData('endText.stopped', endText.tStopRefresh)
thisExp.addData('endHits.started', endHits.tStartRefresh)
thisExp.addData('endHits.stopped', endHits.tStopRefresh)
thisExp.addData('endPoints.started', endPoints.tStartRefresh)
thisExp.addData('endPoints.stopped', endPoints.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
