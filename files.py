#SUBMODULE: FILES

#ACTIONS

def load(filename):
    with open(filename, 'r') as file:
	return file.readlines()

def save(filename,data):
    with open(filename, 'w') as file:
	file.writelines(data)
