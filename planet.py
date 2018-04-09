#Eric Le CPSC 254-03
import re

def get_planet_list(content:str):
	pattern = re.compile("\"BodyName\":\"[-\w+\s\d+]+")
	planets = pattern.findall(content)	
	if planets:
		for r in planets:

			if r[0] == r[-1]:
				r +=1
			print (r+'"')
	return 	len(planets)	
	






