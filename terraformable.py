import re

def num_terraformable(content:str):
	pattern = re.compile(r'Terraformable')
	terraformable = pattern.findall(content)
	return len(terraformable)
		
