# Author: Christian Abdelmassih, Alexandra Runhem

# <formel>::= <mol> \n
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...

# Kattis-länk: https://kth.kattis.com/problems/kth%3Atilda%3Aformelkoll2
# KTH-länk: https://www.kth.se/social/course/DD1320/subgroup/vt-2015-tildav14/page/laboration-6-12/

# SyntaxOperation-constructor() -> self.main() -> self.group_reader() WHILE LOOP -> self.atom_reader() OR self.molecule_reader() RECURSIVE 

from sys import stdin

# An class derived from the Exception-class. Will be used to raise errors.
class DevDefSyntaxError(Exception):
	pass

# Class used as a variable- and method container. Has all functionality to complete identify the syntax
class SyntaxOperation(object):
	
	# Contructor-method, creates attribute alphabet and use_stfdin & print_active to control if output should be printed or returned as string.
	def __init__(self, use_stdin = True, print_active = True):
		self.alphabet = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]
		self.use_stdin = use_stdin
		self.print_active = print_active
	
	# Will run the group-reader after relevant pre-values are set.
	def main(self, row = None):
		if self.use_stdin:
			atom_text = stdin
		else:
			atom_text = row

		for line in atom_text:
			self.line = line
			self.error_message = ""
			
			try:
				self.program_stopper() # Checks if program needs to be stopped (# as input) 
				self.main_data_reseter() # Resets relevant variables before starting to identify syntax

				self.group_reader() # Starts indentifying syntax 
				
				if self.print_active:
					print("Formeln är syntaktiskt korrekt")
				else:
					return "Formeln är syntaktiskt korrekt"
			except DevDefSyntaxError:
				if self.print_active:
					print(self.error_message.replace("\n",""))
				else:
					return self.error_message.replace("\n","")

	# resets the index counter and the last index of the new input
	def main_data_reseter(self):
		self.index = 0
		self.last_index = len(self.line) - 1

	# Shuts down program if input is #
	def program_stopper(self):
		if self.line[0] == "#":
			raise SystemExit

	# Reads groups. Checks if the group is an atom or molecule.
	def group_reader(self):
		while self.index <= self.last_index:
			if self.line[self.index].isupper(): # is an atom
				self.atom_reader()
			elif self.line[self.index] == "(": # is a molecule
				self.molecule_reader()
			elif self.line[self.index] == "\n": # [ENTER], end of a line
				break
			
			else: # Neither, faulty syntax obviously...
				# Error messages of several kinds!
				if self.line[self.index] == ")":
					self.error_message = "Felaktig gruppstart vid radslutet " + self.line[self.index:]
				elif self.line[self.index].isdigit():
					self.error_message = "Felaktig gruppstart vid radslutet " + self.line[self.index:]
				elif self.line[self.index].islower():
					self.error_message = "Saknad stor bokstav vid radslutet " + self.line[self.index:]
				else:
					self.error_message = "Okänd atom vid radslutet " + self.line[self.index+1:]
				raise DevDefSyntaxError # Raise the defined error

	# Reads atoms, both one-letter atoms and two-letter atoms
	def atom_reader(self):
		if self.index < self.last_index:

			# If the letters could be a two-letter atom like He or Bb
			if self.line[self.index].isupper() and self.line[self.index+1].islower():
				
				# If the two-letters are actually an atom
				if (self.line[self.index] + self.line[self.index+1]) in self.alphabet:
					self.index += 2
					self.digit_reader()
				else: # If the are not
					self.error_message = "Okänd atom vid radslutet " + self.line[self.index+2:]
					raise DevDefSyntaxError
			
			# If the atom is a one-letter atom like A or H
			elif self.line[self.index].isupper() and not(self.line[self.index+1].islower()):
				
				# If the one-letter is actually an atom
				if self.line[self.index] in self.alphabet:
					self.index += 1
					self.digit_reader()
				else: # If the are not
					self.error_message = "Okänd atom vid radslutet " + self.line[self.index+1:]
					raise DevDefSyntaxError 
		
		# If the program is on the last letter
		elif self.index == self.last_index:
			if self.line[self.index] == "\n":
				pass
			else:
				self.error_message = "ERROR! ERROR! ERROR! ERROR! Something wrong(at_id) with the letter: '" + self.line[self.index] + "'"
				raise DevDefSyntaxError 

	# Reads molecules. Is recursive. 
	def molecule_reader(self):
		
		# Checks for a nasty syntax fault.
		if self.line[self.index] == "(" and self.line[self.index+1] == ")":
			self.error_message = "Okänd atom vid radslutet " + self.line[self.index+1:]
			raise DevDefSyntaxError 
		
		# If the molecule has parenthesis
		elif self.line[self.index] == "(":
			self.index += 1
			while self.line[self.index] != ")":
				
				# found molecule within molecule!
				if self.line[self.index] == "(":
					self.molecule_reader()
				
				# found atom!
				elif self.line[self.index].isupper():
					self.atom_reader()
				
				# Neither, the syntax is faulty
				else:
					if self.line[self.index].islower():
						self.error_message = "Saknad stor bokstav vid radslutet " + self.line[self.index:]
					elif self.index == self.last_index and self.line[self.index] != ")":
						self.error_message = "Saknad högerparentes vid radslutet " + self.line[self.index:]
					else:
						self.error_message = "Okänd atom vid radslutet " + self.line[self.index+1:]
					raise DevDefSyntaxError 
			

			self.index += 1
			
			# checks numbers after paranthesis
			if self.line[self.index].isdigit():
				self.digit_reader()
			
			# If no number exists
			else:
				self.error_message = "Saknad siffra vid radslutet " + self.line[self.index:]
				raise DevDefSyntaxError 

	# Reads the digits, checks if numbers 1 or 0 exists
	def digit_reader(self):
		if self.index < self.last_index:
			if self.line[self.index] == "0" or (self.line[self.index] == "1" and not(self.line[self.index + 1].isdigit())):
				self.error_message = "För litet tal vid radslutet " + self.line[self.index+1:]
				raise DevDefSyntaxError 
		else:
			if self.line[self.index] == "0" or self.line[self.index] == "1":
				self.error_message = "För litet tal vid radslutet " + self.line[self.index+1:]
				raise DevDefSyntaxError 
		
		# If the number is accepted, keep accepting as long as digits are present
		while self.line[self.index].isdigit() and self.index < self.last_index:
			self.index += 1

obj = SyntaxOperation()
obj.main()


