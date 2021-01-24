# Author: Christian Abdelmassih, Alexandra Runhem

#First-in First-out
class Node():
	def __init__(self, value, next_node):
		self.value = value
		self.next = next_node

class LinkedQ():
	def __init__(self):
		self.first = None
		self.last = None
	
	def __str__(self):
		string = ""
		i = 1
		value = self.get()
		while value != None:
			string = string + "Value " + str(i) + ": " + str(value) + "\n"
			i += 1
			value = self.get()
		return string
			
	
	def put(self, value):
		if self.isEmpty(): # No nodes
			self.first = Node(value, None)
			self.last = self.first

		elif not(self.isEmpty()): # More than one node
			self.last.next = Node(value, None)
			self.last = self.last.next

	def get(self):
		if self.isEmpty():
			return None
		elif not(self.isEmpty()) and self.first == self.last:
			value = self.first.value
			self.first = None
			self.last = None
			return value
		elif not(self.isEmpty()):
			value = self.first.value
			self.first = self.first.next
			return value

	def reverse_get(self):
		if (self.isEmpty()) or (not(self.isEmpty()) and self.first == self.last):
			return self.get()
		elif not(self.isEmpty()):
			value = self.last.value
			temp_node = self.first
			while True:
				if temp_node.next == self.last:
					break
				else:
					temp_node = temp_node.next
			self.last = temp_node
			return value

	
	def flip_stack(self, n_s):
		if self.isEmpty():
			pass
		else:
			value = self.reverse_get()
			n_s.first = Node(value, None)
			n_s.last = n_s.first
			while not(self.isEmpty()):
				value = self.reverse_get()
				n_s.last.next = Node(value, None)
				n_s.last = n_s.last.next
			return n_s

	def isEmpty(self):
		if self.first == None and self.last == None:
			return True
		else:
			return False
