/***************** 
 * Bouncev3 Test *
 *****************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'bounceV3';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(setupRoutineBegin());
flowScheduler.add(setupRoutineEachFrame());
flowScheduler.add(setupRoutineEnd());
const SoundOrNotLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(SoundOrNotLoopBegin(SoundOrNotLoopScheduler));
flowScheduler.add(SoundOrNotLoopScheduler);
flowScheduler.add(SoundOrNotLoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'pong.wav', 'path': 'pong.wav'},
    {'name': 'loopTemplate1.csv', 'path': 'loopTemplate1.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `bounceV1/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var setupClock;
var thisExp;
var win;
var event;
var shuffle;
var random;
var tan;
var randint;
var trialType;
var cursorColor;
var tasksNum;
var hitTotal;
var hitCounter;
var pointsTotal;
var pointsCounter;
var hitPercent;
var trialRepeat;
var trialReps;
var nConditions;
var taskReps;
var instrClock;
var instrText;
var instrStats;
var instrRepeat;
var instrResp;
var fixClock;
var fixMouse;
var fixCursor;
var fixCircle;
var feedbackText;
var fixText;
var fixArrow;
var fixPoints;
var fixHits;
var fixRepeat;
var trialClock;
var trialMouse;
var trialWall;
var trialCursor;
var trialCircle;
var trialHits;
var trialPoints;
var sound_1;
var endClock;
var endText;
var endHits;
var endPoints;
var endResp;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "setup"
  setupClock = new util.Clock();
  // Code to fix reference errors in JS
  thisExp = psychoJS.experiment;
  win = psychoJS.window;
  event = psychoJS.eventManager;
  Array.prototype.append = [].push;
  shuffle = util.shuffle;
  document.documentElement.style.cursor = 'none';
  random = Math.random;
  tan = Math.tan;
  randint = function(min, maxplusone) {
    return Math.floor(Math.random() * (maxplusone - min) ) + min;
  }
  
  // Run 'Begin Experiment' code from setupCode
  trialType = 2;
  cursorColor = [(- 1), (- 1), (- 1)];
  tasksNum = 0;
  hitTotal = 0;
  hitCounter = 0;
  pointsTotal = 0;
  pointsCounter = 0;
  hitPercent = 2;
  trialRepeat = 1;
  trialReps = 16;
  nConditions = 4;
  if ((trialType === 1)) {
      taskReps = (8 * nConditions);
  } else {
      taskReps = (4 * nConditions);
  }
  
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  instrText = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  instrStats = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrStats',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  instrRepeat = new visual.TextStim({
    win: psychoJS.window,
    name: 'instrRepeat',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  instrResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fix"
  fixClock = new util.Clock();
  fixMouse = new core.Mouse({
    win: psychoJS.window,
  });
  fixMouse.mouseClock = new util.Clock();
  fixCursor = new visual.Rect ({
    win: psychoJS.window, name: 'fixCursor', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  fixCircle = new visual.Polygon ({
    win: psychoJS.window, name: 'fixCircle', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.004, 1.0]),
    fillColor: new util.Color([(- 1.0), 0.004, 1.0]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  feedbackText = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbackText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  fixText = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  fixArrow = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixArrow',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.15,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  fixPoints = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixPoints',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.4), (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  fixHits = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixHits',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  fixRepeat = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixRepeat',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  trialMouse = new core.Mouse({
    win: psychoJS.window,
  });
  trialMouse.mouseClock = new util.Clock();
  trialWall = new visual.Rect ({
    win: psychoJS.window, name: 'trialWall', 
    width: [1, 1][0], height: [1, 1][1],
    ori: 0, pos: [0, 0.3],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  trialCursor = new visual.Rect ({
    win: psychoJS.window, name: 'trialCursor', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  trialCircle = new visual.Polygon ({
    win: psychoJS.window, name: 'trialCircle', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  trialHits = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialHits',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  trialPoints = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialPoints',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.4), (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  trialRepeat = new visual.TextStim({
    win: psychoJS.window,
    name: 'trialRepeat',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  sound_1 = new sound.Sound({
    win: psychoJS.window,
    value: 'pong.wav',
    secs: 0.5,
    });
  sound_1.setVolume(1.0);
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  endText = new visual.TextStim({
    win: psychoJS.window,
    name: 'endText',
    text: 'This is the end of the experiment, thank you for your time.\n\nDO NOT close this tab just yet.\nPress ‘space’ and wait until the message box turns green to exit (it can take a few minutes) and return to the questionnaire.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  endHits = new visual.TextStim({
    win: psychoJS.window,
    name: 'endHits',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  endPoints = new visual.TextStim({
    win: psychoJS.window,
    name: 'endPoints',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  endResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var getBrowserId;
var setupComponents;
function setupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'setup' ---
    t = 0;
    setupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    var sUsrAg
    var nIdx
    getBrowserId = function() {
        var browsers = ["MSIE", "Firefox", "Safari", "Chrome", "Opera"];
        sUsrAg = window.navigator.userAgent,
        nIdx = browsers.length - 1;
        for (nIdx; nIdx > -1 && sUsrAg.indexOf(browsers [nIdx]) === -1; nIdx--);
    
      return browsers[nIdx];
    }
    
    psychoJS.experiment.addData("Browser", getBrowserId())
    // keep track of which components have finished
    setupComponents = [];
    
    for (const thisComponent of setupComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function setupRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'setup' ---
    // get current time
    t = setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of setupComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function setupRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'setup' ---
    for (const thisComponent of setupComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var SoundOrNot;
function SoundOrNotLoopBegin(SoundOrNotLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    SoundOrNot = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'loopTemplate1.csv',
      seed: undefined, name: 'SoundOrNot'
    });
    psychoJS.experiment.addLoop(SoundOrNot); // add the loop to the experiment
    currentLoop = SoundOrNot;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisSoundOrNot of SoundOrNot) {
      snapshot = SoundOrNot.getSnapshot();
      SoundOrNotLoopScheduler.add(importConditions(snapshot));
      const tasksLoopScheduler = new Scheduler(psychoJS);
      SoundOrNotLoopScheduler.add(tasksLoopBegin(tasksLoopScheduler, snapshot));
      SoundOrNotLoopScheduler.add(tasksLoopScheduler);
      SoundOrNotLoopScheduler.add(tasksLoopEnd);
      SoundOrNotLoopScheduler.add(SoundOrNotLoopEndIteration(SoundOrNotLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var tasks;
function tasksLoopBegin(tasksLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    tasks = new TrialHandler({
      psychoJS: psychoJS,
      nReps: taskReps/4, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'tasks'
    });
    psychoJS.experiment.addLoop(tasks); // add the loop to the experiment
    currentLoop = tasks;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTask of tasks) {
      snapshot = tasks.getSnapshot();
      tasksLoopScheduler.add(importConditions(snapshot));
      tasksLoopScheduler.add(instrRoutineBegin(snapshot));
      tasksLoopScheduler.add(instrRoutineEachFrame());
      tasksLoopScheduler.add(instrRoutineEnd(snapshot));
      const trialsLoopScheduler = new Scheduler(psychoJS);
      tasksLoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      tasksLoopScheduler.add(trialsLoopScheduler);
      tasksLoopScheduler.add(trialsLoopEnd);
      tasksLoopScheduler.add(tasksLoopEndIteration(tasksLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: trialReps, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(fixRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixRoutineEachFrame());
      trialsLoopScheduler.add(fixRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function tasksLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(tasks);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function tasksLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function SoundOrNotLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(SoundOrNot);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function SoundOrNotLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var tasksNumLeft;
var trialsType;
var trialsNum;
var ballConnectX;
var ballConnectY;
var hitOrMiss;
var interceptBall;
var interceptPaddle;
var interceptDelta;
var timerCount;
var ballSpeed;
var trialArr;
var alpha;
var _instrResp_allKeys;
var instrComponents;
function instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr' ---
    t = 0;
    instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from instrCode
    if ((tasksNum > 0)) {
        hitPercent = (hitCounter / trialReps);
    }
    tasksNumLeft = (taskReps - tasksNum);
    tasksNum = (tasksNum + 1);
    trialsType = 0;
    trialsNum = 0;
    ballConnectX = 1.5;
    ballConnectY = 1.5;
    hitOrMiss = "null";
    cursorColor = [(- 1), (- 1), (- 1)];
    interceptBall = 0;
    interceptPaddle = 0;
    interceptDelta = 0;
    timerCount = 0;
    pointsTotal = (pointsTotal + pointsCounter);
    hitTotal = (hitTotal + hitCounter);
    instrRepeat.text = ((("Block " + tasksNum.toString()) + " / ") + taskReps.toString());
    if ((trialType === 1)) {
        if ((tasksNum === 1)) {
            ballSpeed = 0.04;
        } else {
            ballSpeed = 0.04;
        }
    } else {
        ballSpeed = 0.04;
    }
    instrText.text = (((("Catch the ball for " + tasksNumLeft.toString()) + " blocks of ") + trialReps.toString()) + " trials. Try your best to use the center of the paddle as it will allow you to get the most points.\nYou can take a short break now and press 'space' when ready to continue.");
    if ((tasksNum === 1)) {
        instrStats.text = "";
    } else {
        instrStats.text = ((((("Hits: " + hitCounter.toString()) + " / ") + trialReps.toString()) + "\nPoints: ") + pointsCounter.toString());
    }
    trialArr = [];
    for (var i, _pj_c = 0, _pj_a = util.range(trialReps), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        if (((i % 2) === 0)) {
            trialArr.push(0);
        } else {
            trialArr.push(1);
        }
    }
    alpha = [];
    for (var i, _pj_c = 0, _pj_a = util.range(Number.parseInt((trialReps / 3.5))), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        alpha.push(70);
        alpha.push(75);
        alpha.push(80);
        alpha.push(85);
    }
    util.shuffle(trialArr);
    util.shuffle(alpha);
    
    instrResp.keys = undefined;
    instrResp.rt = undefined;
    _instrResp_allKeys = [];
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(instrText);
    instrComponents.push(instrStats);
    instrComponents.push(instrRepeat);
    instrComponents.push(instrResp);
    
    for (const thisComponent of instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr' ---
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instrText* updates
    if (t >= 0.0 && instrText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrText.tStart = t;  // (not accounting for frame time here)
      instrText.frameNStart = frameN;  // exact frame index
      
      instrText.setAutoDraw(true);
    }

    
    // *instrStats* updates
    if (t >= 0.0 && instrStats.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrStats.tStart = t;  // (not accounting for frame time here)
      instrStats.frameNStart = frameN;  // exact frame index
      
      instrStats.setAutoDraw(true);
    }

    
    // *instrRepeat* updates
    if (t >= 0.0 && instrRepeat.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrRepeat.tStart = t;  // (not accounting for frame time here)
      instrRepeat.frameNStart = frameN;  // exact frame index
      
      instrRepeat.setAutoDraw(true);
    }

    
    // *instrResp* updates
    if (t >= 0.0 && instrResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instrResp.tStart = t;  // (not accounting for frame time here)
      instrResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instrResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instrResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instrResp.clearEvents(); });
    }

    if (instrResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instrResp.getKeys({keyList: ['space'], waitRelease: false});
      _instrResp_allKeys = _instrResp_allKeys.concat(theseKeys);
      if (_instrResp_allKeys.length > 0) {
        instrResp.keys = _instrResp_allKeys[_instrResp_allKeys.length - 1].name;  // just the last key pressed
        instrResp.rt = _instrResp_allKeys[_instrResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr' ---
    for (const thisComponent of instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from instrCode
    thisExp.addData("hitPercent", hitPercent);
    hitCounter = 0;
    pointsCounter = 0;
    hitPercent = 0;
    
    instrResp.stop();
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var bouncePointChoice;
var homeX;
var homeY;
var trialFlag;
var fixFlag;
var pointsGiven;
var theta;
var sinTheta;
var paddleX;
var paddleY;
var cursorPosX;
var cursorPosY;
var leftEdge;
var rightEdge;
var gotValidClick;
var fixComponents;
function fixRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fix' ---
    t = 0;
    fixClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from fixCode
    bouncePointChoice = trialArr[trialsNum];
    homeX = (- 1.0);
    homeY = (- 0.3);
    trialFlag = 0;
    fixFlag = 0;
    pointsGiven = 0;
    timerCount = 0;
    theta = (pi * (0 / 180));
    sinTheta = Math.sin(theta);
    paddleX = 0.05;
    paddleY = 0.0125;
    fixCursor.vertices = [[(- paddleX), (- paddleY)], [(- paddleX), paddleY], [paddleX, paddleY], [paddleX, (- paddleY)]];
    cursorPosX = 0.0;
    cursorPosY = ((sqrt((Math.pow((trialMouse.getPos()[0] - homeX), 2) + Math.pow((trialMouse.getPos()[1] - homeY), 2))) * sinTheta) + homeY);
    if ((trialsNum === 0)) {
        feedbackText.text = "Get ready!";
    } else {
        feedbackText.text = hitOrMiss.toString();
    }
    if (((bouncePointChoice === 0) && (tasksNum === 1))) {
        fixText.text = "Move left for 1 second to start.";
        fixArrow.text = "<=";
    } else {
        if (((bouncePointChoice === 1) && (tasksNum === 1))) {
            fixText.text = "Move right for 1 second to start.";
            fixArrow.text = "=>";
        } else {
            if ((bouncePointChoice === 0)) {
                fixText.text = "";
                fixArrow.text = "<=";
            } else {
                fixText.text = "";
                fixArrow.text = "=>";
            }
        }
    }
    if (((((hitOrMiss === "hit") && (interceptDelta <= 0.025)) && (interceptDelta >= (- 0.025))) && (trialsNum >= 1))) {
        cursorColor = [(- 1), 1.0, (- 1)];
        pointsCounter = (pointsCounter + 10);
        pointsGiven = 10;
    } else {
        if (((hitOrMiss === "hit") && (trialsNum >= 1))) {
            cursorColor = [1.0, 0.004, (- 1.0)];
            pointsCounter = (pointsCounter + 5);
            pointsGiven = 5;
        } else {
            if (((hitOrMiss === "miss") && (trialsNum >= 1))) {
                cursorColor = [1.0, (- 1), (- 1)];
                pointsGiven = 0;
            } else {
                cursorColor = [(- 1.0), (- 1.0), (- 1.0)];
            }
        }
    }
    fixPoints.text = ("Points: " + pointsCounter.toString());
    fixHits.text = ((("Hits: " + hitCounter.toString()) + " / ") + trialsNum.toString());
    leftEdge = (- 0.45);
    rightEdge = 0.45;
    fixRepeat.text = ((("Block " + tasksNum.toString()) + " / ") + taskReps.toString());
    
    // setup some python lists for storing info about the fixMouse
    // current position of the mouse:
    fixMouse.x = [];
    fixMouse.y = [];
    fixMouse.leftButton = [];
    fixMouse.midButton = [];
    fixMouse.rightButton = [];
    fixMouse.time = [];
    gotValidClick = false; // until a click is received
    fixMouse.mouseClock.reset();
    fixCursor.setFillColor(new util.Color(cursorColor));
    fixCursor.setLineColor(new util.Color(cursorColor));
    // keep track of which components have finished
    fixComponents = [];
    fixComponents.push(fixMouse);
    fixComponents.push(fixCursor);
    fixComponents.push(fixCircle);
    fixComponents.push(feedbackText);
    fixComponents.push(fixText);
    fixComponents.push(fixArrow);
    fixComponents.push(fixPoints);
    fixComponents.push(fixHits);
    fixComponents.push(fixRepeat);
    
    for (const thisComponent of fixComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var screen_width;
var screen_height;
var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function fixRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fix' ---
    // get current time
    t = fixClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    screen_width = window.innerWidth;
    screen_height = window.innerHeight 
    
    if (screen_width > screen_height) {
        cursorPosX = trialMouse.getPos()[0] * (screen_height / screen_width);
    } else {
        cursorPosX = trialMouse.getPos()[0];
    }
    // Run 'Each Frame' code from fixCode
    cursorPosY = ((Math.sqrt((Math.pow((trialMouse.getPos()[0] - homeX), 2) + Math.pow((trialMouse.getPos()[1] - homeY), 2))) * sinTheta) + homeY);
    if ((bouncePointChoice === 0)) {
        if ((fixMouse.getPos()[0] <= leftEdge)) {
            timerCount = (timerCount + 1);
        } else {
            if (((fixMouse.getPos()[0] > leftEdge) && (timerCount > 0))) {
                timerCount = (timerCount - 1);
            }
        }
    } else {
        if ((fixMouse.getPos()[0] >= rightEdge)) {
            timerCount = (timerCount + 1);
        } else {
            if (((fixMouse.getPos()[0] < rightEdge) && (timerCount > 0))) {
                timerCount = (timerCount - 1);
            }
        }
    }
    if (((timerCount >= 120) && (trialsNum === 0))) {
        continueRoutine = false;
    } else {
        if ((timerCount >= 60)) {
            continueRoutine = false;
        }
    }
    if ((fixFlag === 0)) {
        ballConnectX = (ballConnectX + 0.0001);
        fixFlag = 1;
    } else {
        ballConnectX = (ballConnectX - 0.0001);
        fixFlag = 0;
    }
    
    // *fixMouse* updates
    if (t >= 0.0 && fixMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixMouse.tStart = t;  // (not accounting for frame time here)
      fixMouse.frameNStart = frameN;  // exact frame index
      
      fixMouse.status = PsychoJS.Status.STARTED;
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (fixMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = fixMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = fixMouse.getPos();
          fixMouse.x.push(_mouseXYs[0]);
          fixMouse.y.push(_mouseXYs[1]);
          fixMouse.leftButton.push(_mouseButtons[0]);
          fixMouse.midButton.push(_mouseButtons[1]);
          fixMouse.rightButton.push(_mouseButtons[2]);
          fixMouse.time.push(fixMouse.mouseClock.getTime());
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *fixCursor* updates
    if (t >= 0.0 && fixCursor.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixCursor.tStart = t;  // (not accounting for frame time here)
      fixCursor.frameNStart = frameN;  // exact frame index
      
      fixCursor.setAutoDraw(true);
    }

    
    if (fixCursor.status === PsychoJS.Status.STARTED){ // only update if being drawn
      fixCursor.setPos([cursorPosX, cursorPosY], false);
    }
    
    // *fixCircle* updates
    if (t >= 0.0 && fixCircle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixCircle.tStart = t;  // (not accounting for frame time here)
      fixCircle.frameNStart = frameN;  // exact frame index
      
      fixCircle.setAutoDraw(true);
    }

    
    if (fixCircle.status === PsychoJS.Status.STARTED){ // only update if being drawn
      fixCircle.setPos([ballConnectX, ballConnectY], false);
    }
    
    // *feedbackText* updates
    if (t >= 0.0 && feedbackText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedbackText.tStart = t;  // (not accounting for frame time here)
      feedbackText.frameNStart = frameN;  // exact frame index
      
      feedbackText.setAutoDraw(true);
    }

    
    // *fixText* updates
    if (t >= 0.0 && fixText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixText.tStart = t;  // (not accounting for frame time here)
      fixText.frameNStart = frameN;  // exact frame index
      
      fixText.setAutoDraw(true);
    }

    
    // *fixArrow* updates
    if (t >= 0.0 && fixArrow.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixArrow.tStart = t;  // (not accounting for frame time here)
      fixArrow.frameNStart = frameN;  // exact frame index
      
      fixArrow.setAutoDraw(true);
    }

    
    // *fixPoints* updates
    if (t >= 0.0 && fixPoints.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixPoints.tStart = t;  // (not accounting for frame time here)
      fixPoints.frameNStart = frameN;  // exact frame index
      
      fixPoints.setAutoDraw(true);
    }

    
    // *fixHits* updates
    if (t >= 0.0 && fixHits.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixHits.tStart = t;  // (not accounting for frame time here)
      fixHits.frameNStart = frameN;  // exact frame index
      
      fixHits.setAutoDraw(true);
    }

    
    // *fixRepeat* updates
    if (t >= 0.0 && fixRepeat.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixRepeat.tStart = t;  // (not accounting for frame time here)
      fixRepeat.frameNStart = frameN;  // exact frame index
      
      fixRepeat.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fixComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fix' ---
    for (const thisComponent of fixComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from fixCode
    thisExp.addData("pointsGiven", pointsGiven);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('fixMouse.x', fixMouse.x);
    psychoJS.experiment.addData('fixMouse.y', fixMouse.y);
    psychoJS.experiment.addData('fixMouse.leftButton', fixMouse.leftButton);
    psychoJS.experiment.addData('fixMouse.midButton', fixMouse.midButton);
    psychoJS.experiment.addData('fixMouse.rightButton', fixMouse.rightButton);
    psychoJS.experiment.addData('fixMouse.time', fixMouse.time);
    
    // the Routine "fix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var bounceDir;
var wallBounceX;
var wallBounceY;
var frameCounter;
var bounceCounter;
var connectCounter;
var perturbation;
var pertChoice;
var alphaChoice;
var choice90;
var choice180;
var cosTheta;
var alphaRad;
var tanAlpha;
var betaChoice;
var betaRad;
var tanBeta;
var bouncePointX;
var bouncePointY;
var launchLineX;
var launchLineY;
var bouncePathX;
var bouncePathY;
var launchLineXP;
var bounceDirArr;
var ballPosX;
var ballPosY;
var paddlePosX;
var paddlePosY;
var wallX;
var wallY;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from trialCode
    homeX = (- 1.0);
    homeY = (- 0.3);
    bounceDir = 0;
    wallBounceX = 0;
    wallBounceY = 0;
    frameCounter = 0;
    bounceCounter = 0;
    connectCounter = 0;
    trialPoints.text = ("Points: " + pointsCounter.toString());
    trialHits.text = ((("Hits: " + hitCounter.toString()) + " / ") + trialsNum.toString());
    trialRepeat.text = ((("Block " + tasksNum.toString()) + " / ") + taskReps.toString());
    perturbation = [((pi / 20) * 2)];
    if ((trialType === 1)) {
        if (((horOrTilt === 1) && (tasksNum >= 5))) {
            trialWall.ori = 0;
        } else {
            if ((((horOrTilt === 2) && (bouncePointChoice === 0)) && (tasksNum >= 5))) {
                trialWall.ori = 9;
            } else {
                if ((((horOrTilt === 2) && (bouncePointChoice === 1)) && (tasksNum >= 5))) {
                    trialWall.ori = 351;
                }
            }
        }
    } else {
        if ((horOrTilt === 1)) {
            trialWall.ori = 0;
        } else {
            if (((horOrTilt === 2) && (bouncePointChoice === 1))) {
                trialWall.ori = 351;
            } else {
                if (((horOrTilt === 2) && (bouncePointChoice === 0))) {
                    trialWall.ori = 9;
                }
            }
        }
    }
    pertChoice = perturbation[0];
    if ((bouncePointChoice === 0)) {
        alphaChoice = alpha[trialsNum];
        choice90 = 90;
        choice180 = 180;
    } else {
        alphaChoice = (- alpha[trialsNum]);
        choice90 = (- 90);
        choice180 = (- 180);
        pertChoice = (- pertChoice);
    }
    theta = (pi * (0 / 180));
    cosTheta = Math.cos(theta);
    sinTheta = Math.sin(theta);
    alphaRad = (pi * (alphaChoice / 180));
    tanAlpha = Math.tan(alphaRad);
    betaChoice = (choice180 - (choice90 + alphaChoice));
    betaRad = (pi * (betaChoice / 180));
    tanBeta = Math.tan((betaRad + pertChoice));
    bouncePointX = 0.0;
    bouncePointY = 0.3;
    launchLineX = (0.6 / tanAlpha);
    launchLineY = 0.6;
    bouncePathX = (bouncePointX - launchLineX);
    bouncePathY = (- 0.3);
    launchLineXP = (0.6 * tanBeta);
    bounceDirArr = [];
    ballPosX = [];
    ballPosY = [];
    paddlePosX = [];
    paddlePosY = [];
    trialsNum = (trialsNum + 1);
    hitOrMiss = "miss";
    paddleX = 0.05;
    paddleY = 0.0125;
    trialCursor.vertices = [[(- paddleX), (- paddleY)], [(- paddleX), paddleY], [paddleX, paddleY], [paddleX, (- paddleY)]];
    wallX = 0.5;
    wallY = 0.0125;
    trialWall.vertices = [[(- wallX), (- wallY)], [(- wallX), wallY], [wallX, wallY], [wallX, (- wallY)]];
    cursorPosX = trialMouse.getPos()[0];
    cursorPosY = ((Math.sqrt((Math.pow((trialMouse.getPos()[0] - homeX), 2) + Math.pow((trialMouse.getPos()[1] - homeY), 2))) * sinTheta) + homeY);
    
    // setup some python lists for storing info about the trialMouse
    // current position of the mouse:
    trialMouse.x = [];
    trialMouse.y = [];
    trialMouse.leftButton = [];
    trialMouse.midButton = [];
    trialMouse.rightButton = [];
    trialMouse.time = [];
    gotValidClick = false; // until a click is received
    trialMouse.mouseClock.reset();
    sound_1.secs=0.5;
    sound_1.setVolume(1.0);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(trialMouse);
    trialComponents.push(trialWall);
    trialComponents.push(trialCursor);
    trialComponents.push(trialCircle);
    trialComponents.push(trialHits);
    trialComponents.push(trialPoints);
    trialComponents.push(trialRepeat);
    trialComponents.push(sound_1);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    screen_width = window.innerWidth;
    screen_height = window.innerHeight 
    
    if (screen_width > screen_height) {
        cursorPosX = trialMouse.getPos()[0] * (screen_height / screen_width);
    } else {
        cursorPosX = trialMouse.getPos()[0];
    }
    // Run 'Each Frame' code from trialCode
    cursorPosY = ((sqrt((Math.pow((trialMouse.getPos()[0] - homeX), 2) + Math.pow((trialMouse.getPos()[1] - homeY), 2))) * sinTheta) + homeY);
    bounceDirArr.append(bounceDir);
    ballPosX.append(bouncePathX);
    ballPosY.append(bouncePathY);
    paddlePosX.append(cursorPosX);
    paddlePosY.append(cursorPosY);
    if ((((((bouncePathX >= (cursorPosX - paddleX)) && (bouncePathY >= (cursorPosY - paddleY))) && (bouncePathX <= (cursorPosX + paddleX))) && (bouncePathY <= (cursorPosY + paddleY))) && (bounceDir === 1))) {
        hitOrMiss = "hit";
        hitCounter = (hitCounter + 1);
        ballConnectX = bouncePathX;
        ballConnectY = bouncePathY;
        continueRoutine = false;
    } else {
        if (((((bouncePathX <= (- 1.0)) || (bouncePathY <= (- 1.0))) || (bouncePathX >= 1.0)) || (bouncePathY >= 1.0))) {
            hitOrMiss = "miss";
            ballConnectX = bouncePathX;
            ballConnectY = bouncePathY;
            continueRoutine = false;
        }
    }
    if ((bounceDir === 0)) {
        bouncePathX = (bouncePathX + (launchLineX * ballSpeed));
        bouncePathY = (bouncePathY + (launchLineY * ballSpeed));
    } else {
        bouncePathX = (bouncePathX + (launchLineXP * ballSpeed));
        bouncePathY = (bouncePathY - (launchLineY * ballSpeed));
    }
    if ((((bouncePathY <= (- 0.29)) && (bounceDir === 1)) && (trialFlag === 0))) {
        interceptBall = bouncePathX;
        interceptPaddle = cursorPosX;
        connectCounter = frameCounter;
        trialFlag = 1;
    }
    if (((bouncePathY >= bouncePointY) && (bounceDir === 0))) {
        bounceDir = 1;
        bounceCounter = frameCounter;
        wallBounceX = bouncePathX;
        wallBounceY = bouncePathY;
    }
    frameCounter = (frameCounter + 1);
    
    // *trialMouse* updates
    if (t >= 0.0 && trialMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialMouse.tStart = t;  // (not accounting for frame time here)
      trialMouse.frameNStart = frameN;  // exact frame index
      
      trialMouse.status = PsychoJS.Status.STARTED;
      prevButtonState = trialMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (trialMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = trialMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = trialMouse.getPos();
          trialMouse.x.push(_mouseXYs[0]);
          trialMouse.y.push(_mouseXYs[1]);
          trialMouse.leftButton.push(_mouseButtons[0]);
          trialMouse.midButton.push(_mouseButtons[1]);
          trialMouse.rightButton.push(_mouseButtons[2]);
          trialMouse.time.push(trialMouse.mouseClock.getTime());
          // abort routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *trialWall* updates
    if (t >= 0.0 && trialWall.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialWall.tStart = t;  // (not accounting for frame time here)
      trialWall.frameNStart = frameN;  // exact frame index
      
      trialWall.setAutoDraw(true);
    }

    
    // *trialCursor* updates
    if (t >= 0.0 && trialCursor.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialCursor.tStart = t;  // (not accounting for frame time here)
      trialCursor.frameNStart = frameN;  // exact frame index
      
      trialCursor.setAutoDraw(true);
    }

    
    if (trialCursor.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialCursor.setPos([cursorPosX, cursorPosY], false);
    }
    
    // *trialCircle* updates
    if (t >= 0.0 && trialCircle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialCircle.tStart = t;  // (not accounting for frame time here)
      trialCircle.frameNStart = frameN;  // exact frame index
      
      trialCircle.setAutoDraw(true);
    }

    
    if (trialCircle.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialCircle.setPos([bouncePathX, bouncePathY], false);
    }
    
    // *trialHits* updates
    if (t >= 0.0 && trialHits.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialHits.tStart = t;  // (not accounting for frame time here)
      trialHits.frameNStart = frameN;  // exact frame index
      
      trialHits.setAutoDraw(true);
    }

    
    // *trialPoints* updates
    if (t >= 0.0 && trialPoints.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialPoints.tStart = t;  // (not accounting for frame time here)
      trialPoints.frameNStart = frameN;  // exact frame index
      
      trialPoints.setAutoDraw(true);
    }

    
    // *trialRepeat* updates
    if (t >= 0.0 && trialRepeat.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialRepeat.tStart = t;  // (not accounting for frame time here)
      trialRepeat.frameNStart = frameN;  // exact frame index
      
      trialRepeat.setAutoDraw(true);
    }

    // start/stop sound_1
    if (t >= Sound && sound_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_1.tStart = t;  // (not accounting for frame time here)
      sound_1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_1.play(); });  // screen flip
      sound_1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = Sound + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.5 > 0.5) {
        sound_1.stop();  // stop the sound (if longer than duration)
      }
      sound_1.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var wallOrient;
function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from trialCode
    thisExp.addData("bounceDirArr", bounceDirArr);
    thisExp.addData("ballPosX", ballPosX);
    thisExp.addData("ballPosY", ballPosY);
    thisExp.addData("paddlePosX", paddlePosX);
    thisExp.addData("paddlePosY", paddlePosY);
    thisExp.addData("alphaChoice", alphaChoice);
    pertChoice = ((pertChoice / 2) * (180 / pi));
    thisExp.addData("pertChoice", pertChoice);
    thisExp.addData("horOrTilt", horOrTilt);
    thisExp.addData("hitOrMiss", hitOrMiss);
    thisExp.addData("trialType", trialType);
    thisExp.addData("trialsNum", trialsNum);
    thisExp.addData("tasksNum", tasksNum);
    thisExp.addData("trialRepeat", trialRepeat);
    thisExp.addData("ballSpeed", ballSpeed);
    interceptDelta = (interceptBall - interceptPaddle);
    thisExp.addData("interceptBall", interceptBall);
    thisExp.addData("interceptPaddle", interceptPaddle);
    thisExp.addData("interceptDelta", interceptDelta);
    thisExp.addData("wallBounceX", wallBounceX);
    thisExp.addData("wallBounceY", wallBounceY);
    if ((trialWall.ori === 0)) {
        wallOrient = "hor";
    } else {
        wallOrient = "tilt";
    }
    thisExp.addData("wallOrient", wallOrient);
    thisExp.addData("connectTime", trialMouse.time[connectCounter]);
    thisExp.addData("bounceTime", trialMouse.time[bounceCounter]);
    thisExp.addData("cumulativetime", globalClock.getTime());
    
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('trialMouse.x', trialMouse.x);
    psychoJS.experiment.addData('trialMouse.y', trialMouse.y);
    psychoJS.experiment.addData('trialMouse.leftButton', trialMouse.leftButton);
    psychoJS.experiment.addData('trialMouse.midButton', trialMouse.midButton);
    psychoJS.experiment.addData('trialMouse.rightButton', trialMouse.rightButton);
    psychoJS.experiment.addData('trialMouse.time', trialMouse.time);
    
    sound_1.stop();  // ensure sound has stopped at end of routine
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _endResp_allKeys;
var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from endCode
    endHits.text = ((("Total Hits: " + (hitTotal + hitCounter).toString()) + " / ") + (tasksNum * trialReps).toString());
    endPoints.text = ("Total Points: " + (pointsTotal + pointsCounter).toString());
    
    endResp.keys = undefined;
    endResp.rt = undefined;
    _endResp_allKeys = [];
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(endText);
    endComponents.push(endHits);
    endComponents.push(endPoints);
    endComponents.push(endResp);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *endText* updates
    if (t >= 0.0 && endText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endText.tStart = t;  // (not accounting for frame time here)
      endText.frameNStart = frameN;  // exact frame index
      
      endText.setAutoDraw(true);
    }

    
    // *endHits* updates
    if (t >= 0.0 && endHits.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endHits.tStart = t;  // (not accounting for frame time here)
      endHits.frameNStart = frameN;  // exact frame index
      
      endHits.setAutoDraw(true);
    }

    
    // *endPoints* updates
    if (t >= 0.0 && endPoints.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endPoints.tStart = t;  // (not accounting for frame time here)
      endPoints.frameNStart = frameN;  // exact frame index
      
      endPoints.setAutoDraw(true);
    }

    
    // *endResp* updates
    if (t >= 0.0 && endResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endResp.tStart = t;  // (not accounting for frame time here)
      endResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endResp.clearEvents(); });
    }

    if (endResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = endResp.getKeys({keyList: ['space'], waitRelease: false});
      _endResp_allKeys = _endResp_allKeys.concat(theseKeys);
      if (_endResp_allKeys.length > 0) {
        endResp.keys = _endResp_allKeys[_endResp_allKeys.length - 1].name;  // just the last key pressed
        endResp.rt = _endResp_allKeys[_endResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    endResp.stop();
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  var message = "You can now close this tab and return to the questionnaire.";
  document.documentElement.style.cursor = 'auto';
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
