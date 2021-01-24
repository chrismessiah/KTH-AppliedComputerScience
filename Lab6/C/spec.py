# Author: Christian Abdelmassih, Alexandra Runhem

# <formel>::= <mol> \n
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...


# class used solely for raising errors
class SomeError(Exception):
	pass

# some class containing all relevant data and methods 
# for solving the problem
class SomeClass(object):
	def __init__(self):
		self.atom_names = ["He",..., "Ar"] # 
		self.error_message = None

	# main-function, expecting a error to be raised
	def main(self):
		try:
			self.group_reader()
			print("Formeln är syntaktiskt korrekt")
		except SomeError:
			print(self.error_message)

	# Reads groups 
	def group_reader(self):
		if isatom():
			self.atom_reader()
		elif ismolecule():
			self.molecule_reader()
		else:
			self.error_message = "Some error ..."
			raise SomeError

	# reads atoms, raises errors when the atom is unknown etc.
	def atom_reader(self):
		if not(isatom()):
			self.error_message = "Some other error ..."
			raise SomeError
		else:
			pass

	# Recursive molecule reader, will call itself when molecule
	# is detected or the atom reader if atom is detected,
	# may also raise errors
	def molecule_reader(self):
		if ismolecule():
			self.molecule_reader() # Recursion
		elif isatom():
			self.atom_reader()
		else:
			self.error_message = "Another error ..."
			raise SomeError



# create object and call main
obj = SomeClass()
obj.main()



