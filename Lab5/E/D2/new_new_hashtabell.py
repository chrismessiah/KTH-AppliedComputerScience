# Written by Christian Abdelmassih, Alexandra Runhem

# Hastable based on queues

from time import *
from LinkedQFile import LinkedQ

class Node():
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def __str__(self):
		if self.key != None and self.value != None:
			return "Artist: " + self.key + " Song: " + str(self.value)
		else:
			return "Node empty"

class Hashtabell():
	def __init__(self, length):

		self.length=length*2
		self.hash_table=[]

		for i in range (0,self.length): #Hashtabell måste ha 50% luft
			self.hash_table.append(LinkedQ())

	def put(self, key, value):
		index = hashing(value.key, self.length)
		index = normalize_index(index, self.length)
		queue = self.hash_table[index]

		if queue.is_empty():
			queue.put(value)
		else:
			key_list = fetch_all_keys_in_queue(queue)
			if key in key_list:
				while True:
					queue_value = queue.get()
					if queue_value.key == key:
						queue_value = value
						queue.put(queue_value)
						break
					queue.put(queue_value)
			else:
				queue.put(value)


		self.hash_table[index].put(value)
			
	def get(self, in_key):
		index = hashing(in_key, self.length)
		index = normalize_index(index, self.length)

		if self.is_empty(index):
			raise KeyError
		else:
			queue = self.hash_table[index]
			
			temp_list = []
			while True:
				value = queue.get()
				if value == None:
					break
				else:
					temp_list.append(value)

			for value in temp_list:
				queue.put(value)
			
			for value in temp_list:
				if value.key == in_key:
					return value
			
			raise KeyError 

	def is_empty(self, index):
		something = self.hash_table[index].get()
		if something == None:
			return True
		else:
			self.hash_table[index].put(something)
			return False

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


def fetch_all_keys_in_queue(queue):
	temp_list = []
	while True:
		value = queue.get()
		if value == None:
			break
		else:
			temp_list.append(value)
	for value in temp_list:
		queue.put(value)
	
	new_temp_list = []
	for value in temp_list:
		new_temp_list.append(value.key)
	return temp_list



