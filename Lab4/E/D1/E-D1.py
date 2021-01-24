# Author: Christian Abdelmassih, Alexandra Runhem

from bintreeFile import Bintree

# returns list of swedish alphabet
def init_alphabet():
	alphabet = []
	for x in range(ord("a"),ord("z")+1):
		alphabet.append(chr(x))
	alphabet.append("å")
	alphabet.append("ä")
	alphabet.append("ö")
	return alphabet

# Make all childs of start_word
def make_children(WORD):
	alphabet = init_alphabet()
	
	word_letter_list = []
	i = 0
	for letter in WORD:
		word_letter_list = list(WORD)

		for letter in alphabet:		
			word_letter_list[i] = letter
			new_word = ''.join(word_letter_list)

			if new_word != WORD and swe_tree.exists(new_word) and not(old_tree.exists(new_word)):
				old_tree.put(new_word)
		i += 1

swe_tree = Bintree()
old_tree = Bintree()

file_name = "word3.txt"
f = open(file_name, "r", encoding="utf-8")
for line in f:
	swe_tree.put(line.replace("\n",""))
f.close()

start_word = "söt"
end_word = "sur"

make_children(start_word)

print(old_tree.write())




