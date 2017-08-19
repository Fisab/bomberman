import player
import tools

def create_players(screen, pygame, size, map):
	res = []

	data = tools.load_file('config.json')
#сделать генерацию позиции в Map
	for i in data['players']:
		if i['color'] == '':
			i['color'] = '0,0,0'
		#print(i['script_path'], i['data_file'])
		res.append( player.Hero(screen, pygame, size, map, i['color'], i['nick'], i['script_path'], i['data_file']) )

	return res