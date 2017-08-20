import tools

class Bomb:
	def __init__(self, pos, color, pygame, screen, owner, time):
		self.pos = pos
		self.color = [(1,1,1), color]

		cell_size = tools.get_val_config('cell_size')

		self.size = [int(cell_size / 2), 1]
		self.owner = owner

		self.exp_radius = tools.get_val_config('bomb_exp_radius')

		self.time = time
		self.step_burn = self.size[0] / self.time

		#
		self.pygame = pygame
		self.screen = screen
		#

	def explode_players(self, pos):
		players = self.owner.Data.players
		pl_remove = []
		a = True
		for i in players:
			if i.pos[0] == pos[0] and i.pos[1] == pos[1]:
				pl_remove.append(i)
				a = False
		for i in pl_remove:
			self.owner.Data.delete_player(i)
		return a


	def explode(self):
		check_collision = self.owner.Map.check_collision
		poses_draw = []#there draw explosions
		dirs = [[0,1,True],[-1,0,True],[0,-1,True],[1,0,True]]#x,y,need_go_next?
		stop = False
		for j in range(1, self.exp_radius):
			if j > 1:
				for i in range(len(dirs)):
					dirs[i][0] = int(dirs[i][0] / (j - 1))
					dirs[i][1] = int(dirs[i][1] / (j - 1))
			if stop:
				break
			for i in range(len(dirs)):
				dirs[i][0] *= j
				dirs[i][1] *= j
			for i in range(len(dirs)):
				if not dirs[i][2]:
					continue
				del_player = self.explode_players(self.pos)
				if not del_player:
					for t in dirs:
						t[2] = False
					stop = True
					break
				pos = [ self.pos[0] + dirs[i][0], self.pos[1] + dirs[i][1] ]
				del_player = self.explode_players(pos)
				if not del_player:
					poses_draw.append(pos)
					dirs[i][2] = False
					continue
				if check_collision(pos, only_strong=True):
					poses_draw.append(pos)
				else:
					dirs[i][2] = False
					continue
				del_wall = check_collision(pos, only_simple=True)
				if not del_wall:#explosion was collision with some wall
					dirs[i][2] = False
					self.owner.Map.del_simple_block(pos)
		self.draw_explosion(poses_draw)
		self.owner.delete_bomb(self)

	def update(self):
		if self.time == 0:
			self.explode()
			return
		self.size[1] += self.step_burn
		self.time -= 1

	def draw(self):
		pos = tools.scale_pos(self.pos, self.size[0]*2)
		pos = [pos[0]+self.size[0], pos[1]+self.size[0]]
		self.pygame.draw.circle(self.screen, self.color[0], (pos[0], pos[1]), self.size[0], 0)
		self.pygame.draw.circle(self.screen, self.color[1], (pos[0], pos[1]), int(self.size[1]), 0)

	def draw_explosion(self, poses):
		for pos in poses:
			pos = tools.scale_pos(pos, self.size[0]*2)
			pos = [pos[0]+self.size[0], pos[1]+self.size[0]]
			self.pygame.draw.circle(self.screen, self.color[1], (pos[0], pos[1]), self.size[0], 0)


