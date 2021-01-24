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

		for i in range (0,self.length):
			self.hash_table.append(LinkedQ())

	def put(self, key, value):
		index = hashing(value.key, self.length)
		index = normalize_index(index, self.length)
		queue = self.hash_table[index]
		new_node = Node(key, value)

		if queue.is_empty():
			queue.put(new_node)
		else:
			node_list, key_list, queue = fetch_all_data_in_queue(queue)
			if key in key_list:
				index = key_list.index(key)
				node_to_be_replaced = node_list[index]

				while True:
					queue_node = queue.get()
					if queue_node == node_to_be_replaced:
						queue.put(new_node)
						break
					else:
						queue.put(queue_node)
			else:
				queue.put(new_node)
			
	def get(self, in_key):
		index = hashing(in_key, self.length)
		index = normalize_index(index, self.length)
		queue = self.hash_table[index]

		if queue.is_empty():
			raise KeyError
		else:
			node_list, key_list, queue = fetch_all_data_in_queue(queue)		
			for node in node_list:
				if node.key == in_key:
					return node.value
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

def fetch_all_data_in_queue(queue):
	node_list = []
	key_list = []
	while True:
		something = queue.get()
		if something == None:
			break
		else:
			node = something
			node_list.append(node)
			key_list.append(node.key)

	for node in node_list:
		queue.put(node)

	return node_list, key_list, queue



