# Author: Christian Abdelmassih, Alexandra Runhem

#First-in First-out Q system

class Node():
	def __init__(self, value, next_node): 
		self.value = value
		self.next = next_node

class LinkedQ():
	def __init__(self):
		self.first = None #The queue is empty at the beginning, therefore no first nor last value
		self.last = None

	def __str__(self):
		string = "Korten kommer ut i denna ordning: "
		node = self.first
		while node != None:
			string = string + str(node.value) + " "
			node = node.next
		string = string + "\n"
		return string
			
	
	def put(self, value): #The new value will always be placed last
		if self.is_empty(): # No nodes
			self.first = Node(value, None) 
			self.last = self.first

		elif not(self.is_empty()): # More than one node
			self.last.next = Node(value, None) 
			self.last = self.last.next

	def get(self):
		if self.is_empty():
			return None

		elif not(self.is_empty()) and self.first == self.last:
			value = self.first.value
			self.first = None
			self.last = None
			return value

		elif not(self.is_empty()):
			value = self.first.value
			self.first = self.first.next
			return value

	def is_empty(self):
		if self.first == None and self.last == None:
			return True
		else:
			return False
