import json
import random
#with open('data/fisab/fisab.cmd') as data_file:
#	data = json.load(data_file)
dirs = ['UP', 'DOWN', 'LEFT', 'RIGHT']

with open('data/fisab/fisab.cmd', mode='w', encoding='utf-8') as f:
	json.dump('MOVE %s;PLANT 5;'%(dirs[random.randint(0,3)]), f)
	#json.dump('PLANT 5;', f)