class Hero():
	def __init__(self, screen, pygame, size, map, color, nick, path, data_path):
		self.Map = map

		self.pos = self.Map.get_player_pos()

		color = color.split(',')
		for i in range(len(color)):
			color[i] = int(color[i])
		self.color = tuple(color)

		self.size = size

		self.vel = [0,0]

		self.screen = screen
		self.pygame = pygame

		self.intent = 2

		self.name = nick
		self.script_path = path
		self.data_file_path = data_path

	def scale_pos(self, pos):
		return [pos[0] * self.size, pos[1] * self.size]

	def draw(self):
		pos = self.scale_pos(self.pos)
		self.pygame.draw.rect(self.screen, self.color, (pos[0] + self.intent, pos[1] + self.intent, self.size - self.intent * 2, self.size - self.intent * 2))

	def set_vel(self, dir):
		if dir == 'up':
			self.vel = [0, -1]
		if dir == 'down':
			self.vel = [0, 1]
		if dir == 'right':
			self.vel = [1, 0]
		if dir == 'left':
			self.vel = [-1, 0]

	def move(self):
		new_pos = [self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]]
		can_move = self.Map.check_collision(new_pos)
		if can_move:
			self.pos = [self.pos[0] + self.vel[0], self.pos[1] + self.vel[1]]
		self.vel = [0, 0]

	def query(self, req):
		reqs = req.split(';')
		for i in reqs:
			if i.lower().find('move') != -1:
				dir = i.split(' ')[1].lower()
				self.set_vel(dir)
				self.move()
