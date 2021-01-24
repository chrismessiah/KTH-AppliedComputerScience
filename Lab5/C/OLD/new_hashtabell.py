# Written by Christian Abdelmassih, Alexandra Runhem

# Hastable based on linear and quadratic probing

from time import *

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
			#index = self.linear_probe(index)
			index = self.quadratic_probe(index)
		self.hash_table[index] = atom	
			
	def get(self, atom_name):
		index = hashing(atom_name, self.length)
		index = normalize_index(index, self.length)

		if self.is_empty(index):
			raise KeyError
		else:
			atom = self.hash_table[index]
			if atom.name != atom_name:
				#atom = self.linear_probe(index, compare_atoms=True, atom_name=atom_name)
				atom = self.quadratic_probe(index, compare_atoms=True, atom_name=atom_name)
			return atom

	def is_empty(self, index):
		node = self.hash_table[index]
		if node.name == None:
			return True
		if node.name != None:
			return False
		else:
			print("ERROR ISEMPTY")

	def quadratic_probe(self, index, compare_atoms=False, atom_name=None):
		i = 1
		while True:
			t_index = index + (i^2)
			t_index = normalize_index(t_index, self.length)

			if compare_atoms == True:
				if atom_name == self.hash_table[t_index].name:
					return self.hash_table[t_index]
					break
			if compare_atoms == False:
				if self.is_empty(t_index):
					return t_index
					break
			i += 1

	def linear_probe(self, index, compare_atoms=False, atom_name=None):
		t_index = index
		turned = 0
		while True:

			t_index += 1
			if t_index >= self.length:
				t_index = normalize_index(t_index, self.length)
				turned += 1
			if compare_atoms == True:
				if atom_name == self.hash_table[t_index].name:
					return self.hash_table[t_index]
					break
			if compare_atoms == False:
				if self.is_empty(t_index):
					return t_index
					break
			if turned == 2:
				raise KeyError

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






