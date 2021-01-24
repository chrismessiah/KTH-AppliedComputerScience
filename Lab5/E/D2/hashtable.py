# Written by Christian Abdelmassih, Alexandra Runhem

class Atom():
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight

class Hashtabell():
	def __init__(self, length):

		self.length=length*2
		self.hash_table=[]
		
		for i in range (0,self.length): #Hashtabell måste ha 50% luft
			self.hash_table.append(Atom(None,None))

	def put(self, key, atom):
		index = hashing(key, self.length)
		state = self.index_value_type(index)
		
		if state == "Empty":
			self.hash_table[index] = atom	

		elif state == "Occupied": # Create new hashtable
			old_atom = self.hash_table[index]

			new_hash_table = Hashtabell(self.length) # Create new hashtable
			new_hash_table.put2(old_atom.name, old_atom) # put Old atom in new hashtable
			new_hash_table.put2(atom.name, atom) # put New atom in new hashtable

			self.hash_table[index] = new_hash_table # insert new hashtable in the old location of Old atom

		elif state == "Hashtable": # Put atom in the other hashtable
			self.hash_table[index].put2(atom.name, atom)
		else:
			print("ERROR! PUT")

	# Put function used when atom colission occurs to put into the other hashtable
	def put2(self, key, atom):
		index = hashing_2(key, self.length)
		state = self.index_value_type(index)
		
		if state == "Empty":
			self.hash_table[index] = atom
		
		else: # Linear probing, in case colission occurs in the other hashtable
			self.linear_probe(atom, index)

	# Returns an index value which is not occupied
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

	# Returns the type of value which is located at the index
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

# converts strings to ascii number strings
def string_to_ascii(in_string):
	convert_list = list(in_string)
	for i in range(0,len(convert_list)):
		letter = convert_list[i]
		convert_list[i] = str(ord(letter))
	ascii_list = convert_list
	return ascii_list

# returns index value
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

# 2nd hashing function used for the 2nd degree hashtables
def hashing_2(in_value, hash_table_length):
	hash_value = hashing(in_value, hash_table_length, tweak_factor = 3)
	return hash_value

# Checks if a value is a atom objct
def is_atom(something):
	try:
		something.name
		something.weight
		return True
	except:
		return False

# Checks if a value is a hashtable objct
def is_hashtable_object(something):
	try:
		something.length
		something.hash_table
		return True
	except:
		return False










