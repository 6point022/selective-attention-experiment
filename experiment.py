from psychopy import core, visual, gui, data, event
from math import cos, sin, radians
from random import randint, choice

gui = gui.Dlg()
gui.addField("Subject ID:")
gui.show()

fileName = f'{gui.data[0]}_{data.getDateStr()}'
file = open(f'./data/{fileName}', 'w')

win = visual.Window([1920, 1080], monitor = 'testMonitor', units = 'deg', color = 'black', fullscr = True)

instructions = '''Instructions\n\n
1. Before every trial, you will be shown 8 dots which represent the circle.\n\n
2. You have to look for two targets -- N and X.\n\n
3. Press 'N' when N is the target displayed in the circle.\n\n
4. Press 'X' when X is the target displayed in the circle.\n\n
5. Respond as fast and accurately as possible.\n\n
6. A distractor stimuli will also be presented with the target stimuli.\n\n
Press any key to continue.'''

instMsg = visual.TextStim(win, pos = [0, 0], text = instructions, height = 0.75)
instMsg.draw()
win.flip()
event.waitKeys()

listCircleCoordinates = []
numOfLetters = 8
theta = 0
radius = 2

listOfChars = list(map(chr, range(65, 91)))
listOfChars.remove('N')
listOfChars.remove('X')

for i in range(numOfLetters):
	listCircleCoordinates.append([radius * cos(radians(theta)), radius * sin(radians(theta))])
	theta += 360 / numOfLetters

def showFixation():
	# fixation

	for c in listCircleCoordinates:
		x = visual.TextStim(win, pos = c, text = '.')
		x.draw()
			
	win.flip()
	core.wait(1)

def drawDistraction(target):
	global listCircleCoordinates
	global listOfChars

	r = randint(1, 3)

	if r == 1:
		text = 'X'
	elif r == 2:
		text = 'N'
	else:
		text = f'{choice(listOfChars)}'

	pos = choice(listCircleCoordinates).copy()

	pos[0] *= 3
	pos[1] *= 3

	x = visual.TextStim(win, pos = pos, text = text)

	x.draw()

	if text == target:
		return 1 # compatible
	elif text != target and (text == 'N' or text == 'X'):
		return 2 # incompatible
	else:
		return 3 # neutral


allResponses = []



condition = 1 # low load

for j in range(20):
	thisResponse = [] 
	thisResponse.append(condition)

	i = 1
	targetPos = randint(1, 8)

	showFixation()

	for c in listCircleCoordinates:
		if targetPos == i:
			if randint(1, 2) == 1:
				x = visual.TextStim(win, pos = c, text = 'N')
				thisResponse.append('N')

			else:
				x = visual.TextStim(win, pos = c, text = 'X')
				thisResponse.append('X')

			x.draw()
			thisResponse.insert(1, drawDistraction(thisResponse[1]))

		i += 1
	
	win.flip()
	core.wait(0.1)
	win.flip()
	timer = core.MonotonicClock(start_time = None)
	thisResponse.append(event.waitKeys(maxWait = 1.5))
	thisResponse.append(round(timer.getTime(applyZero = True), 2))
	allResponses.append(thisResponse)



condition = 2 # low load degradation

for j in range(20):
	thisResponse = [] 
	thisResponse.append(condition)

	i = 1
	targetPos = randint(1, 8)

	showFixation()

	for c in listCircleCoordinates:
		if targetPos == i:
			if randint(1, 2) == 1:
				x = visual.TextStim(win, pos = c, contrast = 0.3, text = 'N')
				thisResponse.append('N')
			else:
				x = visual.TextStim(win, pos = c, contrast = 0.3, text = 'X')
				thisResponse.append('X')

			x.draw()
			thisResponse.insert(1, drawDistraction(thisResponse[1]))
			
		i += 1
	
	win.flip()
	core.wait(0.1)
	win.flip()
	timer = core.MonotonicClock(start_time = None)
	thisResponse.append(event.waitKeys(maxWait = 1.5))
	thisResponse.append(round(timer.getTime(applyZero = True), 2))
	allResponses.append(thisResponse)



condition = 3 # high load

for j in range(20):
	thisResponse = [] 
	thisResponse.append(condition)

	i = 1
	targetPos = randint(1, 8)

	showFixation()

	for c in listCircleCoordinates:
		if targetPos == i:
			if randint(1, 2) == 1:
				x = visual.TextStim(win, pos = c, text = 'N')
				thisResponse.append('N')

			else:
				x = visual.TextStim(win, pos = c, text = 'X')
				thisResponse.append('X')

			x.draw()

		else:
			x = visual.TextStim(win, pos = c, text = f'{choice(listOfChars)}')
			x.draw()
			
		i += 1

	thisResponse.insert(1, drawDistraction(thisResponse[1]))

	win.flip()
	core.wait(0.1)
	win.flip()
	timer = core.MonotonicClock(start_time = None)
	thisResponse.append(event.waitKeys(maxWait = 1.5))
	thisResponse.append(round(timer.getTime(applyZero = True), 2))
	allResponses.append(thisResponse)



x = visual.TextStim(win, pos = [0, 0], text = 'Thank you!')
x.draw()
win.flip()
print(allResponses)
file.write(str(allResponses))
print(len(allResponses))
event.waitKeys()


'''

thisResponse = [high/low/degradedlow, compatible/incompatible/neutral, correctAns, userAns, reactionTime]

'''
    
