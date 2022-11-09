import requests
from tabulate import tabulate
from bs4 import BeautifulSoup as bs
from isim_bulucu import get_namepages_in, get_name_info

import pandas as pd
import csv
import time


hyperlink_male_names = "https://isimbulamadim.com/erkek-isimleri"
male_page_num = 358

hyperlink_female_names = "https://isimbulamadim.com/kiz-isimleri"
female_page_num = 181


def create_next_page_links(hyperlink, num_pages):
	return [hyperlink]+[hyperlink + "/" + str(i) for i in range(2, num_pages+1)]


def create_csv(data, filename):
	df_names = pd.DataFrame(data)
	df_names.to_csv(filename, sep='\t')


def create_namepage_list():
	links = create_next_page_links(hyperlink_male_names, male_page_num)
	links += create_next_page_links(hyperlink_female_names, female_page_num)

	namepages = []
	for link in links:
		namepages += get_namepages_in(link)
		print("namepages collected: "+ str(len(namepages)))

	create_csv(namepages, "namepages.csv")	


def read_nampage_list():
	namepages = []
	with open('namepages.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter='\t')
		for row in csv_reader:
			namepages.append(row[1])

	return namepages


def create_name_list():
	#last recorded name is Hatip, index 1521 in namepages.csv 
	namepages = read_nampage_list()
	names = []

	for namepage in namepages[1521:]:
		start = time.time()
		try:
			info = get_name_info(namepage)
			if info != None:
				names.append(info)
			else:
				print("SKIP AT: ", namepage)
		except:
			print("ERROR AT: ", namepage)
			create_csv(names, "save.csv")
		
		print("no of names: ", len(names), " + 1522 - ", time.time()-start)
	
	create_csv(names, "name_data2.csv")	


#create_namepage_list()
create_name_list()




