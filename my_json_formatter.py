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
	format_str = '<html><head><style>table, th, td {border: 1px solid black;border-collapse: collapse;}</style></head><body>'
	#cat (category)
	for cat_name,cat_values  in data.items():
		
		catv0 = cat_values[0]
		keys = catv0.keys()
		format_str += "<table><thead>"
		#Add table names
		f_str = ""
		for key in keys:
			f_str += "<th>" + key + "</th>"
		f_str += "</thead><tbody>"
		format_str += f_str
		#f_str = f_str[:-2]
		#f_str += "<br/>"
		#line = "-" * len(f_str)
		#f_str += line + "<br/>"

		#cat = add_space(cat_name,len(line))
		format_str += "<p/>" + cat_name + "<p/>"
		#format_str += f_str

		#Contstruct the table entries
		for entry in cat_values:
			format_str += "<tr>"
			for field_name, field_value in entry.items():
				format_str += "<td>"
				if field_name == "URL":
					format_str += '<a href="' + field_value+ '">' + field_value + '</a>'
				else:
					format_str += field_value
				format_str += "</td>"
			#format_str = format_str[:-2]
			#format_str += "<br/>"
			format_str += "</tr>"
		format_str += "</tbody></table></body></html>"
	return format_str
