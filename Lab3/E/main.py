# Author: Christian Abdelmassih, Alexandra Runhem

from bintreeFile import Bintree
import time

# returns a list containing only words in each element
def text_preparer(filename):
	file_name = filename
	f = open(file_name, "r", encoding="utf-8")
	text_rows = len(f.readlines())
	f.close()
	
	f = open(file_name, "r", encoding="utf-8")
	word_list = []
	for i in range(0,text_rows):
		row_words = f.readline().replace("\n","").replace("\t","").split(" ")
		while True:
			try:
				row_words.remove("")
			except:
				break
		word_list.extend(row_words)
	return word_list

# puts in words from inputted wordlist into the inputted tree
def text_putter(tree, word_list):
	for word in word_list:
		tree.put(word)
	return tree


starttime = time.time()

eng_word_list = text_preparer("engelska.txt")
swe_word_list = text_preparer("word3.txt")

tree_swe = Bintree()
tree_eng = Bintree()

tree_swe = text_putter(tree_swe, swe_word_list)
tree_eng = text_putter(tree_eng, eng_word_list)

# for each word in the english list, check if the word exists in both the swedish tree and english tree
# and that it occurs at least once
for word in eng_word_list:
	swe_exist, swe_node = tree_swe.exists(word)
	eng_exist, eng_node = tree_eng.exists(word)
	if swe_exist and eng_exist and eng_node.value_occurence > 0:
		
		if eng_node.value_occurence > 1: # if a doublette is found, print only the word once, then set the occurence to zero
			eng_node.value_occurence = 0
		print(word)


print("\nTime: "+ str( round(time.time() - starttime,2) ))








