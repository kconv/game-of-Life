# import time
import numpy as np
import pygame
import lifeforms
from pygame.locals import *

# display:
width, height = 1600, 900
res = (width, height)
# dimensions of grid:
cell_size = 10
x_cells = width//cell_size
y_cells = height//cell_size
grid_dim = (y_cells, x_cells)
# colors:
bg_color = (11, 27, 49)
grid_color = (34, 55, 80)
alive_color = (162, 181, 202)
about_to_die_color = (96, 118, 144)
# lifeform to implement:
lifeform = lifeforms.glider_cannon(grid_dim)

def update(display, grid):
	grid_next = grid.copy()

	for row, col in np.ndindex(grid.shape):
		r,c = row,col
		if 0 in (row,col):
			if row == 0:
				r = 1
			if col == 0:
				c = 1
		tot_live_adj = np.sum(
				grid[r - 1:row + 2, c - 1:col + 2]) - grid[row, col]
		
		if grid[row, col] == 1 and tot_live_adj < 2 or tot_live_adj > 3:
			colr = about_to_die_color
			grid_next[row, col] = 0
		elif ((grid_next[row, col] == 0 and tot_live_adj == 3) or 
			  (grid_next[row, col] == 1 and 2 <= tot_live_adj <= 3)):
			colr = alive_color
			grid_next[row, col] = 1
		else:
			colr = bg_color
			
		pygame.draw.rect(display, colr, pygame.Rect(col * cell_size, row * cell_size, cell_size - 1, cell_size - 1))

	return grid_next


def main():
	pygame.init()
	pygame.display.set_caption('Game of Life')
	display = pygame.display.set_mode(res)

	grid = lifeform
	print(grid.shape)

	while True:
		display.fill(grid_color)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		grid = update(display, grid)
		pygame.display.update()


if __name__ == '__main__':
	main()