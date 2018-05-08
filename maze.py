import random
import threading
import time
from tkinter import Frame
from tkinter import Button

WALL_COLOR = 'gray'
PATH_COLOR = 'white'


ROW = 0
COL = 0
GRID = []
BTNS = []
NO_BORDER = 0
THERAD_SLEEP = 0
frame = None

START = None 
END = None 


def init(root, row, col, speed, no_border): 
	
	global WINDOW, ROW, COL, BTNS, frame, NO_BORDER, THERAD_SLEEP
	ROW = row
	COL = col
	frame = root
	NO_BORDER = no_border
	THERAD_SLEEP = speed
	
	for btn_row in BTNS:
		for btn in btn_row:
			btn.destroy()
		
	del GRID[:]
	del BTNS[:]
	
	threading.Thread(target=threaded).start()

	
	
def threaded():
	generate()
	time.sleep(.2)
	randomized_prims_algorithm()

	
def generate():
	
	for r in range(ROW):
		cols = []
		buttons = []
		for c in range(COL):
			cols.append(1)
			
			b = Button(frame, width=2, height=1)
			b.grid(column=c, row=r, padx=0, pady=0)#, sticky=W)
			if NO_BORDER == 1:
				b.config(relief='flat')
			b.config(bg='gray')
			buttons.append(b)
		
		GRID.append(cols)
		BTNS.append(buttons)

	

		
def randomized_prims_algorithm():
	
	start_time = time.time()
	
	item = [1, 1] #where we start 
	visited = [] #need for backtracking nese mesum n`lloq
	
	global START, END 
	START = item
	END = item
	
	while item is not None:
	
		r = item[0]
		c = item[1]
		
		GRID[r][c] = 0
		colorize_button(r,c, 'orange')
		
		time.sleep(THERAD_SLEEP)
		
		
		colorize_button(r,c, PATH_COLOR)
		
		
		neighbors = []
		
		#increment +2 cause we need +1 cell as a wall 
	
		if r+2 < ROW -1 and GRID[r+2][c] != 0:
			neighbors.append([r+2,c])
			colorize_button(r+2,c, 'yellow')
			
		if r-2 > 0 and GRID[r-2][c] != 0:
			neighbors.append([r-2,c])
			colorize_button(r-2,c, 'yellow')
			
		if c+2 < COL-1 and GRID[r][c+2] != 0:
			neighbors.append([r,c+2])
			colorize_button(r,c+2, 'yellow')
			
		if c-2 > 0 and GRID[r][c-2] != 0:
			neighbors.append([r,c-2])
			colorize_button(r,c-2, 'yellow')
	
	
		size = len(neighbors)
		
		if size > 0: 		
			rand = random.randint(0, size-1)
			
			new_item = neighbors[rand]
			
			r = int((item[0] + new_item[0]) / 2)
			c = int((item[1] + new_item[1]) / 2)
			GRID[r][c] = 0
			colorize_button(r,c, PATH_COLOR)
			
			item = END = new_item
			visited.append(item)
			
		
		else:
			item = visited.pop() if len(visited) > 0 else None # it will be None if nothing to pop, and we will get-out from wh


		
	
	del neighbors
	del visited
	
	colorize_button(START[0], START[1], 'green')
	colorize_button(END[0], END[1], 'red')
	
	
	print('Finished for: %s' %(time.time() - start_time))

	
	for i in range (0, 10):
		r = random.randint(1, ROW-2)
		c = random.randint(1, COL-2)
		GRID[r][c] = 0
		colorize_button(r,c, PATH_COLOR)

	

	
def colorize_button(row, col, color):
	BTNS[row][col].config(bg=color)

