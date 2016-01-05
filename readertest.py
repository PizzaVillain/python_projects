#-*- coding: utf-8 -*-
import csv
with open('players_n.csv', "rt") as f:
	reader = csv.reader(f)
	for row in reader:
		print (row)
