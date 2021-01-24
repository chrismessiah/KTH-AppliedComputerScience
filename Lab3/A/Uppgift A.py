# Author: Christian Abdelmassih, Alexandra Runhem

from bintreeFile import Bintree

file_name = "word3.txt"

tree = Bintree()
output_tree = Bintree()

# place all values in the tree
f = open(file_name, "r", encoding="utf-8")
for line in f:
	tree.put(line.replace("\n",""))
f.close()

# reverse the word and check if both words exists in the tree but are diffrent
# if they are, place the word in the output tree.
f = open(file_name, "r", encoding="utf-8")
for line in f:
	line = line.replace("\n","")
	line_rev = line[::-1]
	
	if tree.exists(line_rev) and line != line_rev:
		print(line + "   " + line_rev)
f.close()

