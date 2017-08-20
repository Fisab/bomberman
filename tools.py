import json
import time

def load_file(file_name):
	with open(file_name) as data_file:    
		data = json.load(data_file)
	return data

def get_val_config(key):
	data = load_file('config.json')
	return data[key]

def scale_pos(pos, size):
	return [pos[0] * size, pos[1] * size]

def clear_data_file():
	with open('data/data.json', mode='w', encoding='utf-8') as f:
		json.dump('', f)