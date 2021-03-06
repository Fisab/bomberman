import tools
import bomb

class Hero:
	def __init__(self, screen, pygame, map, color, nick, path, data_path):
		self.Map = map

		self.pos = self.Map.get_player_pos()

		color = color.split(',')
		for i in range(len(color)):
			color[i] = int(color[i])
		self.color = tuple(color)

		self.size = tools.get_val_config('cell_size')

		self.vel = [0,0]

		self.screen = screen
		self.pygame = pygame

		self.intent = 2

		self.cooldown_plant = tools.get_val_config('cooldown_plant')
		#self.tick_exp = tools.get_val_config('bomb_exp_ticks')

		self.name = nick
		self.script_path = path
		self.data_file_path = data_path

		self.bombs = []

		self.last_plant = 0

	def draw(self):
		pos = tools.scale_pos(self.pos, self.size)
		self.pygame.draw.rect(self.screen, self.color, (pos[0] + self.intent, pos[1] + self.intent, self.size - self.intent * 2, self.size - self.intent * 2))

	def update(self):
		for bomb in self.bombs:
			bomb.update()
			bomb.draw()

	def set_vel(self, dir):
		if dir == 'up':
			self.vel = [0, -1]
		if dir == 'down':
			self.vel = [0, 1]
		if dir == 'right':
			self.vel = [1, 0]
		if dir == 'left':
			self.vel = [-1, 0]

	def delete_bomb(self, bomb):
		self.bombs.remove(bomb)
		del(bomb)

	def check_col_pl(self, pos):
		for i in self.Data.players:
			if i.pos == self.pos and self.color != i.color:
				return False
		return True

	def move(self):
		new_pos = [self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]]
		can_move = self.Map.check_collision(new_pos)
		can_move_pl = self.check_col_pl(new_pos)
		if can_move and can_move_pl:
			self.pos = [self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]]
		self.vel = [0, 0]

	def plant_bomb(self, tick, time=tools.get_val_config('bomb_exp_ticks')):
		if tick - self.last_plant < self.cooldown_plant:
			#cooldown
			return
		self.last_plant = tick
		pos = self.pos
		self.bombs.append(bomb.Bomb(pos, self.color, self.pygame, self.screen, self, time))

	def query(self, req, tick):
		reqs = req.split(';')
		check_am = [0,0]
		for i in reqs:
			cmd = i.lower()
			if cmd.find('move') != -1 and check_am[0] == 0:
				dir = i.split(' ')[1].lower()
				check_am[0] = 1
				self.set_vel(dir)
				self.move()
			if cmd.find('plant') != -1 and check_am[1] == 0:
				check_am[1] = 1
				buf = cmd.split(' ')
				if len(cmd) == 1:
					self.plant_bomb(tick)
				else:
					buf[1] = int(buf[1])
					if buf[1] > 15:
						buf[1] = 15
					elif buf[1] < 0:
						buf[1] = 1
					self.plant_bomb(tick, time=buf[1])
	
	def delete(self):
		del(self)

