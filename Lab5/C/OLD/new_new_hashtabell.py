# Written by Christian Abdelmassih, Alexandra Runhem

# Hastable based on queues

from time import *
from LinkedQFile import LinkedQ

class Node():
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

	def __str__(self):
		if self.name != None and self.weight != None:
			return "Artist: " + self.name + " Song: " + self.weight
		else:
			return "Node empty"

class Hashtabell():
	def __init__(self, length):

		self.length=length*2
		self.hash_table=[]

		for i in range (0,self.length): #Hashtabell måste ha 50% luft
			self.hash_table.append(Node(None,None))

	def put(self, key, atom):
		index = hashing(atom.name, self.length)
		index = normalize_index(index, self.length)

		if not(self.is_empty(index)):
			something = self.hash_table[index]
			if is_atom_object(something):
				atom2 = something
				self.hash_table[index] = LinkedQ()
				self.hash_table[index].put(atom2)
				self.hash_table[index].put(atom)
			elif is_queue_object(something):
				self.hash_table[index].put(atom)
			else:
				print("Error!! OBJECT")
		else:
			self.hash_table[index] = atom	
			
	def get(self, atom_name):
		index = hashing(atom_name, self.length)
		index = normalize_index(index, self.length)

		if self.is_empty(index):
			raise KeyError
		else:
			something = self.hash_table[index]
			if is_queue_object(something):
				queue = something

				while True:
					some_atom = queue.get()
					if some_atom.name == atom_name:
						return some_atom
					else:
						queue.put(some_atom)


			if is_atom_object(something):
				atom = something
				if atom.name == atom_name:
					return atom
				else:
					print("Error not node!!")

	def is_empty(self, index):
		something = self.hash_table[index]
		if is_queue_object(something):
			return False
		if something.name == None:
			return True
		if something.name != None:
			return False
		else:
			print("ERROR ISEMPTY")

def hashing(in_value, hash_table_length):
	temp_number = 0
	i = 0
	for letter in in_value:
		temp_number = temp_number + ord(letter)*31^(len(in_value)-1-i)
		i += 1
	hash_value = normalize_index(temp_number, hash_table_length)
	return hash_value

def normalize_index(index, hash_table_length):
	if index >= hash_table_length:
		index = index % hash_table_length
	return index


def is_queue_object(something):
	try:
		something.first
		something.last
		return True
	except:
		return False

def is_atom_object(something):
	try:
		something.name
		something.weight
		return True
	except:
		return False







