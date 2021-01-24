# Author: Christian Abdelmassih, Alexandra Runhem

# Postorder
# http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda13/forel/f04.html

# Node class with references to right-node, left-node and the amount of times the value has occured
class Node():
	def __init__(self, node_value):
		self.value = node_value
		self.value_occurence = 1
		self.left = None
		self.right = None

# Binary tree class
class Bintree:
	def __init__(self):
		self.root = None

	# puts value in the bintree, creates root if there is no root, otherwise it calls the recursive put function
	def put(self,value): 
		value = str(value)
		if self.root == None:
			self.root = Node(value)
		else:
			self.recursive_put(self.root,value)

	# Recursive putting function, that walks throuh the tree, and creates new nodes at the correct place. 
	def recursive_put(self,c_node, value): # Recursive function of old put
		first_value, last_value = self.word_alph_order(c_node.value, value)
		
		if first_value == last_value: # If we have found the node that the inputted has
			c_node.value_occurence += 1 # increase occurence by one to mark it as a doublette/triplete
		
		else: # If the current node does not contain the inputted value
			
			if first_value == value: # if inputted value is first alphabetically, go left
				if c_node.left == None: # if there is no node to the left, create node there
					c_node.left = Node(value)
				else: # if there is a node to the left, go left
					self.recursive_put(c_node.left, value) # Call recursive method and go left
			
			# Same as above but right direction
			elif last_value == value:
				if c_node.right == None:
					c_node.right = Node(value)
				else:
					self.recursive_put(c_node.right, value) # Call recursive method and go right

	# Returns true or false depending if the value exists or not.
	def exists(self, value):
		value = str(value)
		if self.root == None: # if there is no root
			return False
		else:
			self.recursive_exists(self.root, value)
			return self.ex

	# goes through the tree, checking if the value exists
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
					
	# Prints all values in the tree, starting from the far left by printing all the leaves then going uppwards to the right
	def write(self):
		self.output_string = ""
		if self.root == None:
			self.output_string = "Tree is empty"
			return self.output_string
		else:
			while self.root != None:
				self.recursive_write(self.root)
			return self.output_string

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

	# Tells if the inputted node should be printed or not depending on if it occurs more than once
	def string_fixer(self, node):
		if node.value_occurence > 1:
			self.output_string = self.output_string + str(node.value) + " x" + str(node.value_occurence) + "\n"
		elif node.value_occurence == 1:
			#self.output_string = self.output_string + str(node.value) + "\n"
			pass

	# A function that checks which of the two inputted words that are the first by alphabetical order.
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




