import csv

def read_file(filename):
	f = open(filename)
	lines = f.readlines()
	f.close()

	return lines


def write_to_file(filename, data):
	f = open(filename, "w+")
	f.write(data)
	f.close()


def get_csv_data(csv_filename):
	data = []
	with open(csv_filename, "r") as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		return [row for row in csv_reader]	
