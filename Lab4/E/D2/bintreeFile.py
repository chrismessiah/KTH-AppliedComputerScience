# Author: Christian Abdelmassih, Alexandra Runhem

# Postorder
# http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda13/forel/f04.html

class Node():
	def __init__(self, node_value):
		self.value = node_value
		self.value_occurence = 1
		self.left = None
		self.right = None

class Bintree:
	def __init__(self):
		self.root = None
		self.string = None

	def recursive_put(self,c_node, value): # Recursive function of old put
		first_value, second_value = self.word_alph_order(c_node.value, value)
		if first_value == second_value:
			c_node.value_occurence += 1
		else:
			if first_value == value:
				if c_node.left == None:
					c_node.left = Node(value)
				else:
					self.recursive_put(c_node.left, value) # Call recursive method and go left
			elif second_value == value:
				if c_node.right == None:
					c_node.right = Node(value)
				else:
					self.recursive_put(c_node.right, value) # Call recursive method and go right

	def put(self,value): # SKA ANROPA EN REKURSIV FN
		if self.root == None:
			self.root = Node(value)
		else:
			self.recursive_put(self.root,value)

	def exists(self, value):
		if self.root == None:
			return False
		else:
			self.recursive_exists(self.root, value)
			return self.ex

	def recursive_exists(self,c_node, value):
			first_value, second_value = self.word_alph_order(c_node.value, value)	
			if c_node.value == value and c_node.value_occurence > 0:
				self.ex = True
			elif first_value == value and c_node.left != None:
				self.recursive_exists(c_node.left, value)
			elif second_value == value and c_node.right != None:
				self.recursive_exists(c_node.right, value)
			else:
				self.ex = False
					

	def write(self):
		self.string = ""
		if self.root == None:
			self.string = "Tree is empty"
			return self.string
		else:
			while self.root != None:
				self.recursive_write(self.root)
			return self.string

	def recursive_write(self, c_node):
		if c_node.left != None: # Go left
			if c_node.left.left != None or c_node.left.right != None: # Check if it is further coneccted
				self.recursive_write(c_node.left)
			else:
				# Found node to delete!
				node = c_node.left
				c_node.left = None 
				self.string_fixer(node)

		elif c_node.left == None: # Go right if left is empty
			if c_node.right != None:
				if c_node.right.left != None or c_node.right.right != None: # Check if it is further coneccted
					self.recursive_write(c_node.right)
				else:
					# Found node to delete
					node = c_node.right
					c_node.right = None
					self.string_fixer(node)

			elif c_node.right == None and c_node == self.root:
				node = c_node
				self.root = None
				self.string_fixer(node)

	
	def string_fixer(self, node):
		if node.value_occurence > 1:
			self.string = self.string + str(node.value) + " x" + str(node.value_occurence) + "\n"
		elif node.value_occurence == 1:
			self.string = self.string + str(node.value) + "\n"

	def word_alph_order(self, word1, word2):
		least_chars = min([len(word1),len(word2)])
		for i in range(0,least_chars):
			if ord(word1[i]) > ord(word2[i]):
				a = word2
				b = word1
				break
			elif ord(word1[i]) < ord(word2[i]):
				a = word1
				b = word2
				break
			elif ord(word1[i]) == ord(word2[i]) and i == (least_chars-1):
				if len(word1) != len(word2):
					if len(word1) > len(word2):
						a = word2
						b = word1
					elif len(word1) < len(word2):
						a = word1
						b = word2
				elif word1 == word2:
					a = word2
					b = a
		return a, b




