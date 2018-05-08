import time
from tkinter import Button
import threading


class Item:
	row =0 
	col =0
	h =0
	g =0
	f =0
	parent =  None
	
	def __init__(self, r=0, c=0):
		self.row = r 
		self.col = c
		
	def __str__(self):
		return 'row:%s col:%s h:%s g:%s f:%s' %(self.row, self.col, self.h, self.g, self.f)
		
		
_rows = 0
_cols = 0
_grid = []
_buttons = []
_start_node = Item(0,0)
_target_node = Item(0,0)
PATH_COLOR = 'green'
CHECK_COLOR = 'orange'
THREAD_SLEEP = 0


def init(grid, buttons, start_node, target_node, speed):
	
	global _rows, _cols, _grid, _buttons, _start_node, _target_node, THREAD_SLEEP
	_rows = len(grid)
	_cols = len(grid[0])
	_grid = grid
	_buttons = buttons 
	_start_node = Item(start_node[0], start_node[1])
	_target_node = Item(target_node[0], target_node[1])
	THREAD_SLEEP = speed

	threading.Thread(target=a_start_algorithm).start()
	
	
	
def a_start_algorithm():
	print('A* Initialized...')
	print(_start_node)
	
	start_time = time.time()
	
	open_list = []
	closed_list = []
	
	rows = len(_grid)
	cols = len(_grid[0])
	
	open_list.append(_start_node)
	
	
	while len(open_list) > 0:
		
		current = Item()
		current.f = 99999
		
		for c in open_list:
			print(c)
			if c.f < current.f:
				current = c 
		
		if current is None:
			print('Current is None')
			break 
		
		
		open_list.remove(current)
		closed_list.append(current) 
		
		r = current.row
		c = current.col
		
		if r == _target_node.row and c == _target_node.col:
			print('node fuckin found')
			construct_road(closed_list, current)
			break
		
		
		
		
		neighbors = []
		neighbors.append(return_item(r, c+1, r, c)) #right
		neighbors.append(return_item(r, c-1, r, c))#left 
		neighbors.append(return_item(r+1, c, r, c))#bottom 
		neighbors.append(return_item(r-1, c, r, c))#top
		
		'''
		top_right 		= return_item(r-1, c+1)
		top_left 		= return_item(r-1, c-1)
		bottom_right 	= return_item(r+1, c+1)
		bottom_left 	= return_item(r+1, c-1)
		'''
		for neighbor in neighbors:
			if neighbor is None:
				continue 
				
			if is_in_list(neighbor.row, neighbor.col, closed_list) > -1:
				colorize_button(neighbor.row,neighbor.col, 'blue')
				continue
			
			
			
			colorize_button(neighbor.row,neighbor.col, CHECK_COLOR)
			
			neighbor.h = heuristics_manhattan_dist(neighbor.row, neighbor.col)
			neighbor.g = current.g + 1 #normal cost:1 diagonal cost:1.414 (pythagoras)
			neighbor.f = neighbor.g + neighbor.h
			
			set_text(neighbor.row, neighbor.col, neighbor.f)
		
			indx = is_in_list(neighbor.row, neighbor.col, open_list)
			if indx > -1:
				if current.g + 1 < open_list[indx].g:
					#open_list[indx] = neighbor
					#open_list[indx].g = current.g
					open_list[indx].parent = current
					
			else:
				neighbor.parent = current
				open_list.append(neighbor)
					
		
		
		time.sleep(THREAD_SLEEP)
		
			
	
	print('A* Finished with: %s' %(time.time() - start_time))
	



def is_in_list(r,c, list):
	i = 0
	for cl in list:
		if r == cl.row and c == cl.col:
			return i
		i+=1
	
	return -1

def construct_road(list, item):
	
	p = item.parent
	while p is not None:
		colorize_button(p.row, p.col, PATH_COLOR)
		i = is_in_list(p.row,p.col, list)
		p = None 
		if i > -1:
			p = list[i].parent
	
	
def return_item(row,col,parent_x, parent_y):
	if row >= 0 and row < _rows \
	and col >= 0 and col < _cols \
	and _grid[row][col] == 0: #check for walls
		return Item(row, col)
	else:
		return None
	

def heuristics_manhattan_dist(r,c):
	return abs(r - _target_node.row)+abs(c - _target_node.col)
	
	
def colorize_button(row, col, color):
	_buttons[row][col].config(bg=color)

def set_text(row, col, text):
	_buttons[row][col].config(text=text)
	
