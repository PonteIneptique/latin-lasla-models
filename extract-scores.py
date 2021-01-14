#!/bin/python3

import glob
import os

indexes = {
	
}
reports = {
	
}
for file in glob.glob("reports/*.md", recursive=True):
	with open(file) as f:
		record = False
		stored = ""
		for line in f:
			if line.startswith("## "):
				record = True
				stored += line.replace("## ", "#### ")
				indexes[line[3:].strip()] = file
			elif line.startswith("### "):
				record = False
			elif record is True:
				stored += line

		reports[os.path.basename(file)] = stored

#print(stored)
#print(index)

sources = {
	"header": "",
	"between-lasla": "",
	"footer": ""
}

with open("README.md") as f:
	index = "header"
	ignore = False
	for line in f:
		if line.startswith("<!-- Start Scores LASLA+ -->"):
			sources[index] += line
			ignore = True
		elif line.startswith("<!-- End Scores LASLA+ -->"):
			ignore = False
			index = "footer"
			sources[index] += line
		elif line.startswith("<!-- Start Scores LASLA -->"):
			sources[index] += line
			ignore = True
		elif line.startswith("<!-- End Scores LASLA -->"):
			ignore = False
			index = "between-lasla"
			sources[index] += line
		elif ignore is False:
			sources[index] += line

from pprint import pprint

indexes1 = "More details:\n"+ "\n".join([
	f"- [{task}]({link}#{task})"
	for task, link in indexes.items()
])+"\n\n\n"

indexes2 = "More details:\n"+ "\n".join([
	f"- [{task}]({link}#{task})"
	for task, link in indexes.items()
])+"\n\n\n"
print(indexes)

with open("README.md", "w") as f:
	f.write("\n\n".join([
		sources["header"],
		indexes1,
		reports["lasla.md"],
		sources["between-lasla"],
		indexes2,
		reports["lasla-plus.md"],
		sources["footer"],
	]))
