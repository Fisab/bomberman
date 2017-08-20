import player
import tools
import json

class Data:
	def __init__(self, walls, players):
		self.players = players
		self.walls = walls

		self.tick = 0

	def load_file(self, file_name):
		with open(file_name) as data_file:
			data = json.load(data_file)
		return data

	def insert_to_file(self, file_name, data):
		with open(file_name, mode='w', encoding='utf-8') as f:
			json.dump(data, f)

	def insert_data(self):
		data = {}
		# data['walls'] = self.walls
		# data['tick'] = self.tick

		data['walls'] = {
			'simple_blocks': {'pos': self.walls['simple_blocks'][0]['pos']}, 
			'strong_blocks': {'pos': self.walls['strong_blocks'][0]['pos']}
		}
		data['tick'] = self.tick
		pl = self.players[0]
		data['players'] = [{'name': pl.name,'pos': pl.pos,'color': pl.color,'last_plant': pl.last_plant}]
		if len(pl.bombs) == 0:
			return
		bomb = pl.bombs[0]
		data['bombs'] = [{'owner_name': pl.name,'pos': bomb.pos,'color': bomb.color[1],'exp_radius': bomb.exp_radius,'time': bomb.time}]
		# players = []
		# bombs = []
		# for pl in self.players:
		# 	players.append({
		# 		'name': pl.name,
		# 		'pos': pl.pos,
		# 		'color': pl.color,
		# 		'last_plant': pl.last_plant
		# 	})
		# 	for bomb in pl.bombs:
		# 		bombs.append({
		# 			'owner_name': pl.name,
		# 			'pos': bomb.pos,
		# 			'color': bomb.color[1],
		# 			'exp_radius': bomb.exp_radius,
		# 			'time': bomb.time
		# 		})

		#data['players'] = players

		self.insert_to_file('data/data.json', data)

	def update(self):
		self.insert_data()

		self.tick+=1

	def get_tick(self):
		return self.tick

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