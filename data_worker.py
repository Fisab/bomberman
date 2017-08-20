import player
import tools
import json
import os
import tools

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

		walls = {'simple_blocks': [], 'strong_blocks': []}
		for i in walls:
			for j in self.walls[i]:
				walls[i].append({
					'pos': j['pos']
				})
		data['walls'] = walls
		data['tick'] = self.tick

		players = []
		bombs = []
		for pl in self.players:
			players.append({
				'name': pl.name,
				'pos': pl.pos,
				'color': pl.color,
				'last_plant': pl.last_plant
			})
			for bomb in pl.bombs:
				bombs.append({
					'owner_name': pl.name,
					'pos': bomb.pos,
					'color': bomb.color[1],
					'exp_radius': bomb.exp_radius,
					'time': bomb.time
				})

		data['players'] = players

		self.insert_to_file('data/data.json', data)

	def query_scripts(self):
		for i in self.players:
			os.system(i.script_path)

	def query_cmds(self):
		for i in self.players:
			cmds = self.load_file(i.data_file_path)
			i.query(cmds, self.tick)

	def update(self):
		self.insert_data()

		self.query_scripts()
		self.query_cmds()

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