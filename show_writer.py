import json
import math
import sys

def add_space(str,length):
	diff = length - len(str)
	if diff < 0:
		print(str)
		return None
	if diff % 2 == 1:
		str = str + " "
	
	r = math.ceil((diff+1)/2)
	spaces = " " * r
	return spaces + str + spaces

def longest_str(entries,key):
	max = 0
	for entry in entries:
		l_str = len(entry[key])
		if l_str > max:
			max = l_str
	return max

def format_data(data):
	format_str = "Show list"
	#cat (category)
	for cat_name,cat_values  in data.items():
		
		catv0 = cat_values[0]
		keys = catv0.keys()
		space_lengths = {key : longest_str(cat_values,key) for key in keys}

		#Add table names
		f_str = ""
		for key in keys:
			f_str += add_space(key,space_lengths[key]) + ": "
		f_str = f_str[:-2]
		f_str += "\n"
		line = "-" * len(f_str)
		f_str += line + "\n"

		cat = add_space(cat_name,len(line))
		format_str += f"\n{cat}\n"
		format_str += f_str

		#Contstruct the table entries
		for entry in cat_values:
			for field_name, field_value in entry.items():
				format_str += add_space(field_value,space_lengths[field_name]) + ": "
			format_str = format_str[:-2]
			format_str += "\n"
	return format_str

with open(sys.argv[1],'rb') as file:
	data = json.load(file)

with open(sys.argv[1] + "formatted.txt",'w') as file:
	file.write(format_data(data))