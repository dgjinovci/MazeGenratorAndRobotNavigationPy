import os
import threading
import random
from tkinter import *

import maze
import a_star


window = Tk()
window.title('Maze Generator & Robot Navigation')
window.geometry("500x400")



def btn_press(row, col):
	if maze.GRID[row][col] == 1:
		maze.GRID[row][col] = 0
		maze.BTNS[row][col].config(bg='white')
	else:
		maze.GRID[row][col] = 1
		maze.BTNS[row][col].config(bg='gray')
	
	
def empty_grid():
	maze.GRID = []
	maze.BTNS = []
	
	_w = int(width.get())
	_h = int(height.get())
	
	for r in range(_h):
		items = []
		buttons = []
		for c in range(_w):
			
			items.append(0)
			
			b = Button(frame, width=2, height=1,command=lambda _r=r, _c=c: btn_press(_r,_c))
			b.grid(column=c, row=r, padx=0, pady=0)#, sticky=W)
			if no_border == 1:
				b.config(relief='flat')
			b.config(bg='white')
			
			buttons.append(b)
		
		maze.GRID.append(items)
		maze.BTNS.append(buttons)
	

	
Label(window, text="Width:").grid(row=0, column=0)	
width=Entry(window, width=10)
width.grid(row=0, column=1)
width.insert(0, 10)#write number 10 in edittext

Label(window, text="Height:").grid(row=0, column=2)	
height=Entry(window, width=10)
height.grid(row=0, column=3)
height.insert(0,10)#write number 10 in edittext

no_border = IntVar()
Checkbutton(window, text="No border", variable=no_border).grid(row=0,column=4)

Label(window, text="Animation speed:").grid(row=0, column=5)
speed=Entry(window, width=5)
speed.grid(row=0,column=6)
speed.insert(0, .1)

frame= Frame(window)
frame.grid(row=2,column=0,columnspan=6)


Button(window,text="Call Prims", command=lambda: maze.init(frame, int(height.get()), int(width.get()), float(speed.get()), no_border.get())).grid(row=1, column=0)


empty_grid()
maze.START = [0,0]
maze.END = [int(height.get())-1, int(width.get())-1]

Button(window, text="Call A*", command=lambda: a_star.init(maze.GRID, maze.BTNS, maze.START, maze.END, float(speed.get()))).grid(row=3,column=0)


window.mainloop()