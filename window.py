import pygame
import math
import tools

class Window:
	def __init__(self):
		self.pygame = pygame
		self.pygame.init()
		self.pygame.display.set_caption("Bomber man v0.1.322")

		self.cell_size = tools.get_val_config('cell_size')
		self.cell_amount = tools.get_val_config('cell_amount')
		self.screen_size = [self.cell_amount[0] * self.cell_size, self.cell_amount[1] * self.cell_size]
		self.screen = pygame.display.set_mode(self.screen_size)

		self.grid_color = (200,200,200)
		self.clear_color = (255,255,255)

		self.tick = 0

	def draw_grid(self):
		for y in range(self.cell_amount[1]):
			pygame.draw.line(self.screen, self.grid_color, [0, y * self.cell_size], [self.screen_size[0], y * self.cell_size], 1)
		for x in range(self.cell_amount[0]):
			pygame.draw.line(self.screen, self.grid_color, [x * self.cell_size, 0], [x * self.cell_size, self.screen_size[1]], 1)

	def clear(self):
		self.tick += 1
		self.screen.fill(self.clear_color)
		self.draw_grid()

	def get_tick(self):
		return self.tick