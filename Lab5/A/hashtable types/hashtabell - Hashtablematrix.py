# Written by Christian Abdelmassih, Alexandra Runhem

# Hastable based on hashtablematrix

class Node():
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

	def __str__(self):
		return "Artist: " + self.name + " Song: " + self.weight

class Hashtabell():
	def __init__(self, length):

		self.length=length*2
		self.hash_table=[]

		self.used_indexes = []

		for i in range (0,self.length): #Hashtabell måste ha 50% luft
			self.hash_table.append(Node(None,None))

	def put(self, key, atom):
		index = hashing(key, self.length)
		state = self.index_value_type(index)
		
		if state == "Empty":
			self.hash_table[index] = atom	

		elif state == "Occupied": # Create
			old_atom = self.hash_table[index]

			new_hash_table = Hashtabell(self.length)
			new_hash_table.put2(old_atom.name, old_atom) # Old value
			new_hash_table.put2(atom.name, atom) # New value

			self.hash_table[index] = new_hash_table

		elif state == "Hashtable":
			self.hash_table[index].put2(atom.name, atom)
		else:
			print("ERROR! PUT")

	def put2(self, key, atom):
		index = hashing_2(key, self.length)
		#print(str(index))
		state = self.index_value_type(index)
		
		if state == "Empty":
			self.hash_table[index] = atom
		
		else: # Linear probing
			self.linear_probe(atom, index)

	def linear_probe(self, atom, index):
		for i in range(1, self.length):
			index += 1
			state = self.index_value_type(index)
			if index > self.length:
				index = index - self.length

			if state == "Empty":
				self.hash_table[index] = atom
				break
			if i == self.length:
				print("RAN OUT OF INDEXES")

	def index_value_type(self, index):
		something = self.hash_table[index]
		if is_atom(something):
			atom = something
			if atom.name == None:
				return "Empty"
			if atom.name != None:
				return "Occupied"
			else:
				print("ERROR ISEMPTY")
		elif is_hashtable_object(something):
			return "Hashtable"
		else:
			print("ERROR TYPE ")
			print(something)
			
	def get(self, atom_name):
		index = hashing(atom_name, self.length)
		something = self.hash_table[index]

		if is_atom(something):
			atom = something
			if atom.name == atom_name:
				return atom
			else:
				raise KeyError

		elif is_hashtable_object(something):
			new_hash_table_object = something
			index = hashing_2(atom_name, new_hash_table_object.length)

			for i in range(0,self.length):
				some_atom = new_hash_table_object.hash_table[index]
				if some_atom.name == None:
					raise KeyError
					break
				if some_atom.name == atom_name:
					atom = some_atom
					return atom
				index += 1
		else:
			print("ERROR GET")

def string_to_ascii(in_string):
	convert_list = list(in_string)
	for i in range(0,len(convert_list)):
		letter = convert_list[i]
		convert_list[i] = str(ord(letter))
	ascii_list = convert_list
	return ascii_list

def hashing(in_value, hash_table_length, tweak_factor = 1):
	ascii_list = string_to_ascii(in_value)

	if len(ascii_list) == 1:
		ascii_value = int(ascii_list[0])
	else:
		ascii_list[1] = ascii_list[1]*tweak_factor
		ascii_value = int("".join(ascii_list))	

	if ascii_value > hash_table_length:
		hash_value = ascii_value % hash_table_length
	else:
		hash_value = ascii_value
	return hash_value

def hashing_2(in_value, hash_table_length):
	temp_number = 0
	i=0
	for letter in in_value:
		temp_number = temp_number + ord(letter)*31^(len(in_value)-1-i)
		i += 1
	hash_value = temp_number % hash_table_length
	return hash_value

def is_atom(something):
	try:
		something.name
		something.weight
		return True
	except:
		return False

def is_hashtable_object(something):
	try:
		something.length
		something.hash_table
		return True
	except:
		return False









