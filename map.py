import data_worker
import random
import tools

class Map:
	def __init__(self, screen, pygame):
		self.screen = screen
		self.pygame = pygame

		self.cell_size = tools.get_val_config('cell_size')
		self.cell_amount = tools.get_val_config('cell_amount')

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
			check_x = pos[0] > 4 and pos[0] < self.cell_amount[0] - 4
			check_y = pos[1] > 4 and pos[1] < self.cell_amount[1] - 4
				
			if valid and check_y and check_x:
				near_cells = [[0,1],[-1,0],[0,-1],[1,0]]
				for i in near_cells:
					new_pos = [pos[0]+i[0], pos[1]+i[1]]
					self.del_simple_block(new_pos)
				return pos

	def del_simple_block(self, pos):
		for i in self.blocks['simple_blocks']:
			if i['pos'] == pos:
				self.blocks['simple_blocks'].remove(i)
				return

	def load_map(self):
		#gen map in real time
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
				#continue
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

	def check_col(self, pos, block_name):
		for i in self.blocks[block_name]:
			if i['pos'] == pos:
				return False
		return True

	def check_collision(self, pos, only_simple=False, only_strong=False):
		if only_simple:
			return self.check_col(pos, 'simple_blocks')
		if only_strong:
			return self.check_col(pos, 'strong_blocks')
		else:
			return self.check_col(pos, 'strong_blocks') * self.check_col(pos, 'simple_blocks')

	def draw_map(self):
		for i in self.blocks:
			for j in self.blocks[i]:
				pos = tools.scale_pos(j['pos'], self.cell_size)

				self.pygame.draw.rect(self.screen, self.colors[i], (pos[0] + j['indent'], pos[1] + j['indent'], self.cell_size - j['indent'] * 2, self.cell_size - j['indent'] * 2))

