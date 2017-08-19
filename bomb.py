
class Bomb:
	def __init__(self, pos, color, time=10):
		#owner get by color
		self.pos = pos
		self.color = color

		self.time = time

	def explode(self):
		pass

	def update(self):
		if self.time == 0:
			self.explode()
		self.time -= 1

