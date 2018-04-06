import re

def get_star_system_names(content:str):
	pattern = re.compile("\"StarSystem\":\"[-\w+\s\d+]+")
	planets = pattern.findall(content)
	if planets:
		for r in planets:
			
			if r[0] == r[-1]:
				r+=1
			print (r+'"')
	return len(planets)
