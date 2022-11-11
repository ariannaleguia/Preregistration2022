#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on October 21, 2022, at 01:32
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.4')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'bounceV3'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'Group': '1',
    'Day': '1',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'bounceV1/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\bjoer\\Desktop\\mikulapleasegod-master\\mikulapleasegod-master\\bounceV3_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "setup" ---
# Run 'Begin Experiment' code from setupCode
horOrTilt = int(expInfo['Group'])
trialType = int(expInfo['Day'])
cursorColor = [-1,-1,-1]
tasksNum = 0
hitTotal = 0
hitCounter = 0
pointsTotal = 0
pointsCounter = 0
hitPercent = 2
trialRepeat = 1
trialReps = 50
if (trialType == 1):
    taskReps = 8
else:
    taskReps = 4

# --- Initialize components for Routine "instr" ---
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

# --- Initialize components for Routine "fix" ---
fixMouse = event.Mouse(win=win)
x, y = [None, None]
fixMouse.mouseClock = core.Clock()
fixCursor = visual.Rect(
    win=win, name='fixCursor',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-3.0, interpolate=True)
fixCircle = visual.Polygon(
    win=win, name='fixCircle',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1.000,0.004,1.000], fillColor=[-1.000,0.004,1.000],
    opacity=1, depth=-4.0, interpolate=True)
feedbackText = visual.TextStim(win=win, name='feedbackText',
    text=None,
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
fixText = visual.TextStim(win=win, name='fixText',
    text=None,
    font='Arial',
    pos=(0, 0.0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
fixArrow = visual.TextStim(win=win, name='fixArrow',
    text=None,
    font='Arial',
    pos=(0, -0.2), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
fixPoints = visual.TextStim(win=win, name='fixPoints',
    text=None,
    font='Arial',
    pos=(-0.4, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
fixHits = visual.TextStim(win=win, name='fixHits',
    text=None,
    font='Arial',
    pos=(0.4, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
fixRepeat = visual.TextStim(win=win, name='fixRepeat',
    text=None,
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "trial" ---
trialMouse = event.Mouse(win=win)
x, y = [None, None]
trialMouse.mouseClock = core.Clock()
trialWall = visual.Rect(
    win=win, name='trialWall',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(0, 0.3), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
trialCursor = visual.Rect(
    win=win, name='trialCursor',
    width=(1.0, 1.0)[0], height=(1.0, 1.0)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-4.0, interpolate=True)
trialCircle = visual.Polygon(
    win=win, name='trialCircle',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0], anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-5.0, interpolate=True)
trialHits = visual.TextStim(win=win, name='trialHits',
    text=None,
    font='Arial',
    pos=(0.4, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
trialPoints = visual.TextStim(win=win, name='trialPoints',
    text=None,
    font='Arial',
    pos=(-0.4, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
trialRepeat = visual.TextStim(win=win, name='trialRepeat',
    text=None,
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
sound_1 = sound.Sound('pong.wav', secs=0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)

# --- Initialize components for Routine "end" ---
endText = visual.TextStim(win=win, name='endText',
    text='This is the end of the experiment, thank you for your time.\n\nDO NOT close this tab just yet.\nPress ‘space’ and wait until the message box turns green to exit (it can take a few minutes) and return to the questionnaire.',
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
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "setup" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "setup" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setup" ---
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
tasks = data.TrialHandler(nReps=taskReps, method='sequential', 
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
    
    # --- Prepare to start Routine "instr" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instrCode
    if tasksNum > 0:
        hitPercent = hitCounter / trialReps
    # check how many repeated trials
    #if trialRepeat >= 4 and taskNum <= 3:
        #tasksNum = tasksNum + 1
        #trialRepeat = 1
    # check if over 60%
    #if hitPercent >= 0.6 or hitPercent <= 2:
        #tasksNum = tasksNum + 1
        #trialRepeat = 1
    #else:
        #trialRepeat = trialRepeat + 1
    
    tasksNumLeft = taskReps - tasksNum
    tasksNum = tasksNum + 1
    
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
    timerCount = 0
    pointsTotal = pointsTotal + pointsCounter
    hitTotal = hitTotal + hitCounter
    
    instrRepeat.text = "Block " + str(tasksNum) + " / " + str(taskReps)
    
    # values to change for ball speed
    if (trialType == 1):
        if tasksNum == 1:
            ballSpeed = 0.04
        else:
            ballSpeed = 0.04
    else:
        ballSpeed = 0.04
    
    #Determines what messages show up
    instrText.text = "Catch the ball for " + str(tasksNumLeft) + " blocks of " + str(trialReps) + " trials. Try your best to use the center of the paddle as it will allow you to get the most points.\nYou can take a short break now and press 'space' when ready to continue."
    
    if tasksNum == 1:
        instrStats.text = ""
    else:
        instrStats.text = "Hits: " + str(hitCounter) + " / " + str(trialReps) + "\nPoints: " + str(pointsCounter)
    
    # Determines whether trial starts on left or right
    trialArr = []
    for i in range(trialReps):
        if i % 2 == 0:
            trialArr.append(0)
        else:
            trialArr.append(1)
    
    alpha = []
    for i in range(int(trialReps/3.5)):
        alpha.append(70)
        alpha.append(75)
        alpha.append(80)
        alpha.append(85)
    
    shuffle(trialArr)
    shuffle(alpha)
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
    frameN = -1
    
    # --- Run Routine "instr" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrText.started')
            instrText.setAutoDraw(True)
        
        # *instrStats* updates
        if instrStats.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrStats.frameNStart = frameN  # exact frame index
            instrStats.tStart = t  # local t and not account for scr refresh
            instrStats.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrStats, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrStats.started')
            instrStats.setAutoDraw(True)
        
        # *instrRepeat* updates
        if instrRepeat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrRepeat.frameNStart = frameN  # exact frame index
            instrRepeat.tStart = t  # local t and not account for scr refresh
            instrRepeat.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrRepeat, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrRepeat.started')
            instrRepeat.setAutoDraw(True)
        
        # *instrResp* updates
        waitOnFlip = False
        if instrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrResp.frameNStart = frameN  # exact frame index
            instrResp.tStart = t  # local t and not account for scr refresh
            instrResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instrResp.started')
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr" ---
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from instrCode
    thisExp.addData('hitPercent', hitPercent)
    hitCounter = 0
    pointsCounter = 0
    hitPercent = 0
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=trialReps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('loopTemplate1.csv'),
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
        
        # --- Prepare to start Routine "fix" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from fixCode
        # initial variables
        bouncePointChoice = trialArr[trialsNum]
        homeX = -1.0
        homeY = -0.3
        trialFlag = 0
        fixFlag = 0
        pointsGiven = 0
        timerCount = 0
        
        # intial angle control for paddle position
        theta = (pi * (0 / 180))
        sinTheta = sin(theta)
        
        # paddle variables
        paddleX = 0.05
        paddleY = 0.0125
        fixCursor.vertices = [(-paddleX,-paddleY),(-paddleX,paddleY),(paddleX,paddleY),(paddleX,-paddleY)]
        cursorPosX = 0.0
        cursorPosY = (sqrt(((trialMouse.getPos()[0] - homeX)**2)+((trialMouse.getPos()[1] - homeY)**2))*(sinTheta) + homeY)
        
        # text control
        if trialsNum == 0:
            feedbackText.text = "Get ready!"
        else:
            feedbackText.text = str(hitOrMiss)
            
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
            
        # paddle color and points control
        if hitOrMiss == "hit" and interceptDelta <= 0.025 and interceptDelta >= -0.025 and trialsNum >= 1:
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
        fixHits.text = "Hits: " + str(hitCounter) + " / " + str(trialsNum)
        
        # markers for edges
        leftEdge = -0.45
        rightEdge = 0.45
        
        
        #number of repeats
        fixRepeat.text = "Block " + str(tasksNum) + " / " + str(taskReps)
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
        # keep track of which components have finished
        fixComponents = [fixMouse, fixCursor, fixCircle, feedbackText, fixText, fixArrow, fixPoints, fixHits, fixRepeat]
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
        frameN = -1
        
        # --- Run Routine "fix" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from fixCode
            cursorPosY = (sqrt(((trialMouse.getPos()[0] - homeX)**2)+((trialMouse.getPos()[1] - homeY)**2))*(sinTheta) + homeY)
            
            if bouncePointChoice == 0:
                if fixMouse.getPos()[0] <= leftEdge:
                    timerCount = timerCount + 1
                elif fixMouse.getPos()[0] > leftEdge and timerCount > 0:
                    timerCount = timerCount - 1
            else:
                if fixMouse.getPos()[0] >= rightEdge:
                    timerCount = timerCount + 1
                elif fixMouse.getPos()[0] < rightEdge and timerCount > 0:
                    timerCount = timerCount - 1
            
            if timerCount >= 120 and trialsNum == 0:
                continueRoutine = False
            elif timerCount >= 60:
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixMouse.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixCursor.started')
                fixCursor.setAutoDraw(True)
            if fixCursor.status == STARTED:  # only update if drawing
                fixCursor.setPos((cursorPosX, cursorPosY), log=False)
            
            # *fixCircle* updates
            if fixCircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixCircle.frameNStart = frameN  # exact frame index
                fixCircle.tStart = t  # local t and not account for scr refresh
                fixCircle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixCircle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixCircle.started')
                fixCircle.setAutoDraw(True)
            if fixCircle.status == STARTED:  # only update if drawing
                fixCircle.setPos((ballConnectX, ballConnectY), log=False)
            
            # *feedbackText* updates
            if feedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackText.frameNStart = frameN  # exact frame index
                feedbackText.tStart = t  # local t and not account for scr refresh
                feedbackText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbackText.started')
                feedbackText.setAutoDraw(True)
            
            # *fixText* updates
            if fixText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixText.frameNStart = frameN  # exact frame index
                fixText.tStart = t  # local t and not account for scr refresh
                fixText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixText.started')
                fixText.setAutoDraw(True)
            
            # *fixArrow* updates
            if fixArrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixArrow.frameNStart = frameN  # exact frame index
                fixArrow.tStart = t  # local t and not account for scr refresh
                fixArrow.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixArrow, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixArrow.started')
                fixArrow.setAutoDraw(True)
            
            # *fixPoints* updates
            if fixPoints.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixPoints.frameNStart = frameN  # exact frame index
                fixPoints.tStart = t  # local t and not account for scr refresh
                fixPoints.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixPoints, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixPoints.started')
                fixPoints.setAutoDraw(True)
            
            # *fixHits* updates
            if fixHits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixHits.frameNStart = frameN  # exact frame index
                fixHits.tStart = t  # local t and not account for scr refresh
                fixHits.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixHits, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixHits.started')
                fixHits.setAutoDraw(True)
            
            # *fixRepeat* updates
            if fixRepeat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixRepeat.frameNStart = frameN  # exact frame index
                fixRepeat.tStart = t  # local t and not account for scr refresh
                fixRepeat.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixRepeat, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixRepeat.started')
                fixRepeat.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fix" ---
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from fixCode
        thisExp.addData('pointsGiven', pointsGiven)
        # store data for trials (TrialHandler)
        trials.addData('fixMouse.x', fixMouse.x)
        trials.addData('fixMouse.y', fixMouse.y)
        trials.addData('fixMouse.leftButton', fixMouse.leftButton)
        trials.addData('fixMouse.midButton', fixMouse.midButton)
        trials.addData('fixMouse.rightButton', fixMouse.rightButton)
        trials.addData('fixMouse.time', fixMouse.time)
        # the Routine "fix" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from trialCode
        # controls paddle positioning
        homeX = -1.0
        homeY = -0.3
        
        # don't touch
        bounceDir = 0
        wallBounceX = 0
        wallBounceY = 0
        frameCounter = 0
        bounceCounter = 0
        connectCounter = 0
        
        trialPoints.text = "Points: " + str(pointsCounter)
        trialHits.text = "Hits: " + str(hitCounter) + " / " + str(trialsNum)
        trialRepeat.text = "Block " + str(tasksNum) + " / " + str(taskReps)
        
        # angle info
        perturbation = [(pi/20)*2]
        # alpha = [70, 75, 80, 85]
        if (trialType == 1):
            if horOrTilt == 1 and tasksNum >= 5:
                trialWall.ori = 0
            elif horOrTilt == 2 and bouncePointChoice == 0 and tasksNum >= 5:
                trialWall.ori = 9
            elif horOrTilt == 2 and bouncePointChoice == 1 and tasksNum >= 5:
                trialWall.ori = 351
        else:
            if horOrTilt == 1 and tasksNum <= 2:
                trialWall.ori = 0
            elif horOrTilt == 1 and tasksNum == 3 and bouncePointChoice == 0:
                trialWall.ori = 9
            elif horOrTilt == 1 and tasksNum == 3 and bouncePointChoice == 1:
                trialWall.ori = 351
            elif horOrTilt == 2 and tasksNum <= 2 and bouncePointChoice == 0:
                trialWall.ori = 9
            elif horOrTilt == 2 and tasksNum <= 2 and bouncePointChoice == 1:
                trialWall.ori = 351
            elif horOrTilt == 2 and tasksNum == 3:
                trialWall.ori = 0
            else:
                trialWall.ori = 0
            
        if tasksNum >= 5 and trialType == 1:
            pertChoice = perturbation[0]
        elif tasksNum <= 3 and trialType != 1:
            pertChoice = perturbation[0]
        else:
            pertChoice = 0
            
        if bouncePointChoice == 0:
            # randint max should equal len(alpha)
            alphaChoice = alpha[trialsNum]
            choice90 = 90
            choice180 = 180
        else:
            alphaChoice = -(alpha[trialsNum])
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
        trialsNum = trialsNum + 1
        hitOrMiss = "miss"
        
        # values to change for paddle size
        paddleX = 0.05
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
        sound_1.setSound('pong.wav', secs=0, hamming=True)
        sound_1.setVolume(1.0, log=False)
        # keep track of which components have finished
        trialComponents = [trialMouse, trialWall, trialCursor, trialCircle, trialHits, trialPoints, trialRepeat, sound_1]
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
        frameN = -1
        
        # --- Run Routine "trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from trialCode
            # check to end
            #if tasksNum >= 9:
                #continueRoutine = False
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
            else:
                bouncePathX = bouncePathX + launchLineXP*ballSpeed
                bouncePathY = bouncePathY - launchLineY*ballSpeed
                
            if bouncePathY <= -0.29 and (bounceDir == 1) and (trialFlag == 0):
                interceptBall = bouncePathX
                interceptPaddle = cursorPosX
                connectCounter = frameCounter
                trialFlag = 1
                
            if (bouncePathY >= bouncePointY) and (bounceDir == 0):
                bounceDir = 1
                bounceCounter = frameCounter
                wallBounceX = bouncePathX
                wallBounceY = bouncePathY
                
            frameCounter = frameCounter + 1
            
                
            
            # *trialMouse* updates
            if trialMouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialMouse.frameNStart = frameN  # exact frame index
                trialMouse.tStart = t  # local t and not account for scr refresh
                trialMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialMouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialMouse.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialWall.started')
                trialWall.setAutoDraw(True)
            
            # *trialCursor* updates
            if trialCursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialCursor.frameNStart = frameN  # exact frame index
                trialCursor.tStart = t  # local t and not account for scr refresh
                trialCursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialCursor, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialCursor.started')
                trialCursor.setAutoDraw(True)
            if trialCursor.status == STARTED:  # only update if drawing
                trialCursor.setPos((cursorPosX, cursorPosY), log=False)
            
            # *trialCircle* updates
            if trialCircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialCircle.frameNStart = frameN  # exact frame index
                trialCircle.tStart = t  # local t and not account for scr refresh
                trialCircle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialCircle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialCircle.started')
                trialCircle.setAutoDraw(True)
            if trialCircle.status == STARTED:  # only update if drawing
                trialCircle.setPos((bouncePathX, bouncePathY), log=False)
            
            # *trialHits* updates
            if trialHits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialHits.frameNStart = frameN  # exact frame index
                trialHits.tStart = t  # local t and not account for scr refresh
                trialHits.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialHits, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialHits.started')
                trialHits.setAutoDraw(True)
            
            # *trialPoints* updates
            if trialPoints.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialPoints.frameNStart = frameN  # exact frame index
                trialPoints.tStart = t  # local t and not account for scr refresh
                trialPoints.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialPoints, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialPoints.started')
                trialPoints.setAutoDraw(True)
            
            # *trialRepeat* updates
            if trialRepeat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialRepeat.frameNStart = frameN  # exact frame index
                trialRepeat.tStart = t  # local t and not account for scr refresh
                trialRepeat.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialRepeat, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trialRepeat.started')
                trialRepeat.setAutoDraw(True)
            # start/stop sound_1
            if sound_1.status == NOT_STARTED and tThisFlip >= 0.4-frameTolerance:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_1.started', tThisFlipGlobal)
                sound_1.play(when=win)  # sync with win flip
            if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_1.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_1.tStop = t  # not accounting for scr refresh
                    sound_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sound_1.stopped')
                    sound_1.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from trialCode
        thisExp.addData('bounceDirArr', bounceDirArr)
        thisExp.addData('ballPosX', ballPosX)
        thisExp.addData('ballPosY', ballPosY)
        thisExp.addData('paddlePosX', paddlePosX)
        thisExp.addData('paddlePosY', paddlePosY)
        thisExp.addData('alphaChoice', alphaChoice)
        pertChoice = (pertChoice/2)*(180/pi)
        thisExp.addData('pertChoice', pertChoice)
        thisExp.addData('horOrTilt', horOrTilt)
        thisExp.addData('hitOrMiss', hitOrMiss)
        thisExp.addData('trialType', trialType)
        thisExp.addData('trialsNum', trialsNum)
        thisExp.addData('tasksNum', tasksNum)
        thisExp.addData('trialRepeat', trialRepeat)
        thisExp.addData('ballSpeed', ballSpeed)
        interceptDelta = interceptBall - interceptPaddle
        thisExp.addData('interceptBall', interceptBall)
        thisExp.addData('interceptPaddle', interceptPaddle)
        thisExp.addData('interceptDelta', interceptDelta)
        thisExp.addData('wallBounceX', wallBounceX)
        thisExp.addData('wallBounceY', wallBounceY)
        if trialWall.ori == 0:
            wallOrient = "hor"
        else:
            wallOrient = "tilt"
        thisExp.addData('wallOrient', wallOrient)
        thisExp.addData('connectTime', trialMouse.time[connectCounter])
        thisExp.addData('bounceTime', trialMouse.time[bounceCounter])
        thisExp.addData('cumulativetime', globalClock.getTime())
        
        # store data for trials (TrialHandler)
        trials.addData('trialMouse.x', trialMouse.x)
        trials.addData('trialMouse.y', trialMouse.y)
        trials.addData('trialMouse.leftButton', trialMouse.leftButton)
        trials.addData('trialMouse.midButton', trialMouse.midButton)
        trials.addData('trialMouse.rightButton', trialMouse.rightButton)
        trials.addData('trialMouse.time', trialMouse.time)
        sound_1.stop()  # ensure sound has stopped at end of routine
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed trialReps repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed taskReps repeats of 'tasks'


# --- Prepare to start Routine "end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from endCode
endHits.text = "Total Hits: " + str(hitTotal + hitCounter) + " / " + str(tasksNum*trialReps)
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
frameN = -1

# --- Run Routine "end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endText.started')
        endText.setAutoDraw(True)
    
    # *endHits* updates
    if endHits.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endHits.frameNStart = frameN  # exact frame index
        endHits.tStart = t  # local t and not account for scr refresh
        endHits.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endHits, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endHits.started')
        endHits.setAutoDraw(True)
    
    # *endPoints* updates
    if endPoints.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endPoints.frameNStart = frameN  # exact frame index
        endPoints.tStart = t  # local t and not account for scr refresh
        endPoints.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endPoints, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endPoints.started')
        endPoints.setAutoDraw(True)
    
    # *endResp* updates
    waitOnFlip = False
    if endResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endResp.frameNStart = frameN  # exact frame index
        endResp.tStart = t  # local t and not account for scr refresh
        endResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endResp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endResp.started')
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
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
