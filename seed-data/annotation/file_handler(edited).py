#filename = 'part_4.conllu'
import csv
import pandas as pd


def read_file(filename):
	f = open(filename)
	lines = f.readlines()
	f.close()

	return lines


def write_to_file(filename, data):
    f = open(filename, "wb")
    wr = csv.writer(f, quoting = csv.QUOTE_ALL)
    wr.writerow(f)
    f.close()

def create_csv(data, filename):
    df_list = pd.DataFrame(data)
    df_list.to_csv(filename, encoding = "utf-8-sig", sep=",")
