class Hero():
	def __init__(self, pos, screen, pygame, size):
		self.pos = pos
		self.color = (0,0,0)

		self.size = size

		self.screen = screen
		self.pygame = pygame

		self.intent = 2

	def scale_pos(self, pos):
		return [pos[0] * self.size, pos[1] * self.size]

	def draw(self):
		pos = self.scale_pos(self.pos)
		self.pygame.draw.rect(self.screen, self.color, (pos[0] + self.intent, pos[1] + self.intent, self.size - self.intent * 2, self.size - self.intent * 2))