import data_worker
import random

class Map():
	def __init__(self, cell_size, screen, pygame, cell_amount):
		self.cell_size = cell_size
		self.screen = screen
		self.pygame = pygame

		self.cell_amount = cell_amount

		self.colors = {
			"simple_blocks": (100,100,100),
			"strong_blocks": (143,188,143)
		}
		self.blocks = {
			'strong_blocks': [],
			'simple_blocks': []
		}

		self.load_map()

	def get_player_pos(self):
		while True:
			pos = [random.randint(0, self.cell_amount[0]), random.randint(0, self.cell_amount[1])]
			valid = self.check_collision(pos)
			if valid:
				return pos


	def load_map(self):
		# map = data_worker.load_file('data/maps/map.json')
		
		# for i in map['colors']:
		# 	self.colors[i] = map['colors'][i].split(',')
		# 	for j in range(len(self.colors[i])):
		# 		self.colors[i][j] = int(self.colors[i][j])
		# 	self.colors[i] = tuple(self.colors[i])
		# self.blocks = map['blocks']
		for i in range(self.cell_amount[1]):
			for j in range(self.cell_amount[0]):
				if i % 2 == 0 and j % 2 == 0:
					self.blocks['strong_blocks'].append({
						"pos":[j, i],
						"indent": 0
					})
				elif i == 0 or j == 0 or i == self.cell_amount[1]-1 or j == self.cell_amount[0]-1:
					self.blocks['strong_blocks'].append({
						"pos":[j, i],
						"indent": 0
					})
				if i % 2 == 0 and j % 2 == 0 and i != 0 and j != 0 and i != self.cell_amount[1]-1 and j != self.cell_amount[0]-1:
					if random.randint(0,1) == 1:
						continue
					self.blocks['simple_blocks'].append({
						"pos":[j+1, i],
						"indent": 5
					})
					self.blocks['simple_blocks'].append({
						"pos":[j, i+1],
						"indent": 5
					})


	def scale_pos(self, pos):
		return [pos[0] * self.cell_size, pos[1] * self.cell_size]

	def check_collision(self, pos):
		for i in self.blocks['simple_blocks']:
			if i['pos'] == pos:
				return False
		for i in self.blocks['strong_blocks']:
			if i['pos'] == pos:
				return False
		return True

	def draw_map(self):
		for i in self.blocks:
			for j in self.blocks[i]:
				pos = self.scale_pos(j['pos'])
				self.pygame.draw.rect(self.screen, self.colors[i], (pos[0] + j['indent'], pos[1] + j['indent'], self.cell_size - j['indent'] * 2, self.cell_size - j['indent'] * 2))

