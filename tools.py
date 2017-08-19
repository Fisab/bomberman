import json

def load_file(file_name):
	with open(file_name) as data_file:    
		data = json.load(data_file)
	return data
