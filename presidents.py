#!/usr/bin/env python# Exercise: Presidents  # Write a program to:# (1) Load the data from presidents.txt into a dictionary.# (2) Print the years the greatest and least number of presidents were alive.#     (between 1732 and 2015 (inclusive))#     Ex. #       'least = 2015'#       'most = 2015'# Bonus: Confirm there are no ties.############################################################################### Imports# Bodydef load_presidents(s):	dictionary = {}	with open(s) as fin: 		history = fin.read()		history = history.split("\r")		for president in history : 			president_list = president.split(",")			president_list = replace_None(president_list) # Replace Nones in death year by current year			dictionary[president_list[0]] = president_list[1:] # Assign birth year and death year as dictionary values	return dictionarydef replace_None(president_list):	""" Returns the list with None replaced with 2015"""	if president_list[2] == "None":		president_list[2] = "2015"	return president_listdef president_alive(life, year):	""" For a given year, returns True if the president is alive and False otherwise"""	if year in range(int(life[0]), int(life[1])):		return True	else:		return Falsedef alive(presidents):	""" Return a dictionary of years with number of presidents alive during that year. """	alive_d = {}	years = range(1732, 2016)	for year in years:		for president in presidents:			if president_alive(presidents[president], year):				alive_d[year] = alive_d.get(year, 0) + 1 	return alive_ddef inverse_dict(d):	inverse = {}	for key, value in d.items():		inverse[value] = inverse.get(value, []) + [key]	return inverse##############################################################################def main():  # CALL YOUR FUNCTION BELOW	presidents = load_presidents("presidents.txt")	alive_d = alive(presidents)	inverse_alive = inverse_dict(alive_d)	min_key = min(inverse_alive.keys())	max_key = max(inverse_alive.keys())	print "The years with the least number of presidents alive were {} with {} president alive".format(inverse_alive[min_key], min_key)	print "The years with the most number of presidents alive were {} with {} presidents alive".format(inverse_alive[max_key], max_key)if __name__ == '__main__':    main()