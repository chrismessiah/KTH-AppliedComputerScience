# Author: Christian Abdelmassih, Alexandra Runhem

from bintreeFile import Bintree
from LinkedQFile import LinkedQ

# Class of all attributes and operations needed to finish the given task 
class ChildOperation():
	
	def __init__(self):
		self.start_word = "söt"
		self.end_word = "sur"

		self.swe_tree = Bintree()
		self.old_tree = Bintree()
		self.queue = LinkedQ()

		self.init_aplhabet()

		self.file_reader()

	# Creates a list with the swedish alphabet
	def init_aplhabet(self):
		self.alphabet = []
		for x in range(ord("a"),ord("z")+1):
			self.alphabet.append(chr(x))
		self.alphabet.append("å")
		self.alphabet.append("ä")
		self.alphabet.append("ö")
	
	# Reads textfile, places all words in swe_tree
	def file_reader(self):
		file_name = "word3.txt"
		f = open(file_name, "r", encoding="utf-8")
		for line in f:
			self.swe_tree.put(line.replace("\n",""))
		f.close()

	# Creates childs of 'word'
	def make_children(self, word):
		word_letter_list = []
		i = 0

		for letter in word:
			word_letter_list = list(word)

			for letter in self.alphabet:		
				word_letter_list[i] = letter
				new_word = ''.join(word_letter_list)

				if new_word != word and self.swe_tree.exists(new_word) and not(self.old_tree.exists(new_word)):
					self.old_tree.put(new_word)
					self.queue.put(new_word)
			i += 1 

# Checks if there is a way to obj.end_word
def way_finder(obj):
	if not(obj.queue.isEmpty()):
		node_value = obj.queue.get()

	# Create childs of all childs until the word is found or the queue is empty
	while not(obj.queue.isEmpty()):
		obj.make_children(node_value)
		node_value = obj.queue.get()
		
		if node_value == obj.end_word:
			print("There exists a way to " + obj.end_word)
			raise SystemExit
		elif node_value != obj.end_word and obj.queue.isEmpty():
			print("There is NO way to " + obj.end_word)
			raise SystemExit

obj = ChildOperation()
obj.make_children(obj.start_word)
way_finder(obj)







