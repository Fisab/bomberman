import player
import tools

class Data:
	def __init__(self, walls, players):
		self.players = players
		self.walls = walls

		self.tick = 0

	def update(self):
		pass

	def get_players(self):
		return self.players

	def delete_player(self, player):
		self.players.remove(player)
		del(player)



def create_players(screen, pygame, map):
	res = []

	data = tools.load_file('config.json')
	for i in data['players']:
		if i['color'] == '':
			i['color'] = '0,0,0'
		pl = player.Hero(screen, pygame, map, i['color'], i['nick'], i['script_path'], i['data_file'])
		res.append(pl)
	return res