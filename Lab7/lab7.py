# Author: Christian Abdelmassih, Alexandra Runhem

# <formel>::= <mol> \n
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...

# Kattis-länk: https://kth.kattis.com/problems/kth%3Atilda%3Aformelkoll2
# KTH-länk: https://www.kth.se/social/course/DD1320/subgroup/vt-2015-tildav14/page/laboration-7-12/

# SyntaxOperation-constructor() -> self.main() -> self.group_reader() WHILE LOOP -> self.atom_reader() OR self.molecule_reader() RECURSIVE 

from sys import stdin
from molgrafik import *
from atomdict import create_atom_dict

# An class derived from the Exception-class. Will be used to raise errors.
class DevDefSyntaxError(Exception):
	pass

# Class used as a variable- and method container. Has all functionality to complete identify the syntax
class SyntaxOperation(object):
	
	# Contructor-method, creates attribute alphabet and use_stfdin & print_active to control if output should be printed or returned as string.
	def __init__(self, use_stdin = True, print_active = True):
		self.alphabet = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"]
		
		# boolean to control whenether output should be printed or returned
		self.use_stdin = use_stdin
		self.print_active = print_active
		
		# ******** EDITED FROM LAB 6******** DOWN
		self.mol_obj = Molgrafik()
		
		# Ruta-attributes
		self.r = None # original Ruta-object
		self.current_r = None # current ruta tracker

		self.weight_dict = create_atom_dict()
		# ******** EDITED FROM LAB 6******** UP

	
	# Will run the group-reader after relevant pre-values are set.
	def main(self, row = None):
		if self.use_stdin:
			atom_text = stdin
		else:
			atom_text = row

		for line in atom_text:
			self.line = line
			self.error_message = "ERROR! ERROR! ERROR! ERROR! No error occurred or defined but was called!"
			
			try:
				self.program_stopper() # Checks if program needs to be stopped (# as input) 
				self.main_data_reseter() # Resets relevant variables before starting to identify syntax

				self.group_reader() # Starts indentifying syntax 
				
				if self.print_active:
					print("Formeln är syntaktiskt korrekt")
				else:
					return "Formeln är syntaktiskt korrekt"

				# ******** EDITED FROM LAB 6******** DOWN
				weight = self.get_weight(self.r, 0)
				self.mol_obj.show(self.r, weight)
				self.mol_obj.root.update() # Updates tkinter window
				# ******** EDITED FROM LAB 6******** UP
				
			except DevDefSyntaxError:
				if self.print_active:
					print(self.error_message.replace("\n",""))
				else:
					return self.error_message.replace("\n","")

	# resets the index counter and the last index of the new input
	def main_data_reseter(self):
		self.index = 0
		self.last_index = len(self.line) - 1
		
		# ******** EDITED FROM LAB 6******** DOWN
		# Ruta-related attribute reset
		self.r = None
		self.current_r = None
		# ******** EDITED FROM LAB 6******** UP

	# Shuts down program if input is #
	def program_stopper(self):
		if self.line[0] == "#":
			raise SystemExit

	# Reads groups. Checks if the group is an atom or molecule.
	def group_reader(self):
		self.current_r = None
		while self.index <= self.last_index:
			if self.line[self.index].isupper(): # is an atom
				self.atom_reader()
			elif self.line[self.index] == "(": # is a molecule

				# ******** EDITED FROM LAB 6******** DOWN
				# creation of a new Ruta object to be placed in tk.root 
				self.ruta_handler(False, 0, "()", use_stack = True)
				self.molecule_reader(normal_level = self.current_r)
				# ******** EDITED FROM LAB 6******** UP

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
	def atom_reader(self, down = False):
		if self.index < self.last_index:

			# If the letters could be a two-letter atom like He or Bb
			if self.line[self.index].isupper() and self.line[self.index+1].islower():
				
				# If the two-letters are actually an atom
				if (self.line[self.index] + self.line[self.index+1]) in self.alphabet:
					
					# ******** EDITED FROM LAB 6******** DOWN
					atom_string =  self.line[self.index] + self.line[self.index+1]
					self.ruta_handler(down, 2, atom_string)
					self.digit_reader()
					# ******** EDITED FROM LAB 6******** UP

				else: # If the are not
					self.error_message = "Okänd atom vid radslutet " + self.line[self.index+2:]
					raise DevDefSyntaxError
			
			# If the atom is a one-letter atom like A or H
			elif self.line[self.index].isupper() and not(self.line[self.index+1].islower()):
				
				# If the one-letter is actually an atom
				if self.line[self.index] in self.alphabet:
				
					# ******** EDITED FROM LAB 6******** DOWN
					atom_string =  self.line[self.index]
					self.ruta_handler(down, 1, atom_string)
					self.digit_reader()
					# ******** EDITED FROM LAB 6******** UP

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
	def molecule_reader(self, normal_level = None, down = False):
		down_state = True
		# Checks or a nasty syntax fault.
		if self.line[self.index] == "(" and self.line[self.index+1] == ")":
			self.error_message = "Okänd atom vid radslutet " + self.line[self.index+1:]
			raise DevDefSyntaxError 
		
		# If the molecule has parenthesis
		elif self.line[self.index] == "(":
			self.index += 1
			while self.line[self.index] != ")":
				
				# ******** EDITED FROM LAB 6******** DOWN
				# found molecule within molecule!
				if self.line[self.index] == "(":
					if self.line[self.index-1] == "(":
						self.ruta_handler(True, 0, "()", use_stack = True)
					else:
						self.ruta_handler(down, 0, "()", use_stack = True)
					self.molecule_reader(normal_level = self.current_r)
					# ******** EDITED FROM LAB 6******** UP
				
				# found atom!
				elif self.line[self.index].isupper():
					# ******** EDITED FROM LAB 6******** DOWN
					self.atom_reader(down = down_state)
					down_state = False
					# ******** EDITED FROM LAB 6******** UP
				
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
				#******** EDITED FROM LAB 6******** DOWN
				if normal_level != None:
					self.current_r = normal_level
				# ******** EDITED FROM LAB 6******** UP

				self.digit_reader()			
			# If no number exists
			else:
				self.error_message = "Saknad siffra vid radslutet " + self.line[self.index:]
				raise DevDefSyntaxError 

	# Reads the digits, checks if numbers 1 or 0 exists
	def digit_reader(self, return_digits = False, string = None):
		if not(return_digits):		
			if self.index < self.last_index:
				if self.line[self.index] == "0" or (self.line[self.index] == "1" and not(self.line[self.index + 1].isdigit())):
					self.error_message = "För litet tal vid radslutet " + self.line[self.index+1:]
					raise DevDefSyntaxError 
			else:
				if self.line[self.index] == "0" or self.line[self.index] == "1":
					self.error_message = "För litet tal vid radslutet " + self.line[self.index+1:]
					raise DevDefSyntaxError 
			
		# If the number is accepted, keep accepting as long as digits are present
		
		if return_digits:
			self.index = 0
			self.last_index = len(string) - 1
			self.line = string

		# ******** EDITED FROM LAB 6******** DOWN
		atom_number = []
		while self.line[self.index].isdigit() and self.index < self.last_index:
			atom_number.append(self.line[self.index])
			self.index += 1
		if atom_number:
			atom_number = int("".join(atom_number))
			self.current_r.num = atom_number
			return atom_number, self.line[self.index:]
		else:
			return 1, self.line[self.index:]

	def ruta_exists(self):
		if self.r == None:
			return False
		else:
			return True

	def ruta_handler(self, down, add_num, atom_name, use_stack = False):
		self.index += add_num
		new_ruta = Ruta(atom = atom_name)
		if not(self.ruta_exists()): # make new_ruta as root-ruta if none exists 
			self.r = new_ruta
			self.current_r = self.r
		else:

			# used to control drawing output
			if down:
				self.current_r.down = new_ruta
			else:
				self.current_r.next = new_ruta
			self.current_r = new_ruta

	def get_weight(self, r, weight):
		if r.down != None:

			normal_level = r
			paranthesis_num = normal_level.num
			
			r = r.down
			new_weight = self.get_weight(r, 0)
			temp_weight = new_weight * paranthesis_num
			weight = temp_weight + weight

			r = normal_level
			if r.next == None:
				if r.atom != "()":
					nucleus_weight = self.weight_dict[r.atom]
					atom_weight = r.num * nucleus_weight
					weight = weight + atom_weight
				return weight
			else:
				r = r.next
				weight = self.get_weight(r, weight)
				return weight

		elif r.next != None:
			nucleus_weight = self.weight_dict[r.atom]
			atom_weight = r.num * nucleus_weight
			weight = weight + atom_weight
			r = r.next
			new_weight = self.get_weight(r, weight)
			return new_weight

		else:
			nucleus_weight = self.weight_dict[r.atom]
			atom_weight = r.num * nucleus_weight
			weight = weight + atom_weight
			return weight
	#******** EDITED FROM LAB 6******** UP

obj = SyntaxOperation()
obj.main()


