#filename = 'part_5.conllu'

def read_file(filename):
	f = open(filename)
	lines = f.readlines()
	f.close()

	return lines


def write_to_file(filename, data):
	f = open(filename, "w+")
	f.write(data)
	f.close()