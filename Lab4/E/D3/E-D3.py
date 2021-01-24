# Author: Christian Abdelmassih, Alexandra Runhem

from bintreeFile import Bintree
from LinkedQFile import LinkedQ

class Node:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

# A class with all needed attributes to finish the task
class ChildOperation():
	def __init__(self):
		self.start_word = "söt"
		self.end_word = "sur"

		self.swe_tree = Bintree()
		self.old_tree = Bintree()
		self.queue = LinkedQ()

		self.start_node = Node(self.start_word)
		self.queue.put(self.start_node)

		self.file_reader()

		self.init_alphabet()

	# Creates alphabet attribute
	def init_alphabet(self):
		self.alphabet = []
		for x in range(ord("a"),ord("z")+1):
			self.alphabet.append(chr(x))
		for x in ("å","ä","ö"):
			self.alphabet.append(x)

	# Reads file and puts each word into the tree
	def file_reader(self):
		file_name = "word3.txt"
		f = open(file_name, "r", encoding="utf-8")
		for line in f:
			self.swe_tree.put(line.replace("\n",""))
		f.close()

	# Creates children of parent_node
	def make_children(self, parent_node):
		i = 0

		for x in range(0,len(parent_node.word)):
			temp_letter_list = list(parent_node.word)

			for alph_letter in self.alphabet:		
				temp_letter_list[i] = alph_letter
				child_word = ''.join(temp_letter_list)

				child_node = Node(child_word, parent=parent_node)

				if child_word == self.end_word:		# found word!
					self.queue.put(child_node)
					write_chain(child_node)

				if self.swe_tree.exists(child_word) and not(self.old_tree.exists(child_word)):
					self.old_tree.put(child_word)
					self.queue.put(child_node)

			i += 1

# Writes out the chain and exits the program
def write_chain(child):
	output_string = recursive_write_chain(child,"")
	print(output_string)
	raise SystemExit # Comment out to see ALL solutions

# recursive chail function, will go on until it has reached the final parent
def recursive_write_chain(child, io_string):
	if child.parent != None:
		io_string = recursive_write_chain(child.parent, io_string)
		io_string = io_string + child.word + "\n"
		return io_string
	else:
		io_string = io_string + child.word + "\n"
		return io_string

# Create child of childs until queue is empty
obj = ChildOperation()
while not(obj.queue.isEmpty()):
    nod = obj.queue.get()
    obj.make_children(nod)
print("Error! No way to " + obj.end_word + " was found!")







