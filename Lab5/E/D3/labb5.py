# Written by Christian Abdelmassih, Alexandra Runhem

from hashtest import *
from hashtabell import *
from molgrafik import *

# Creates a list with all the atoms as elements
def create_atom_list():
	init_atom_list = skapaAtomlista()
	final_atom_list = []

	for atom in init_atom_list:
		temp_letter_list = atom.split(" ")

		while True:
			try:
				temp_letter_list.remove("")
			except:
				break

		atom_name = temp_letter_list[0]
		atom_weight = temp_letter_list[1]
		final_atom_list.append(Atom(atom_name, float(atom_weight)))
	return final_atom_list

# Creates the hash_table object
def create_hash_table(atom_list):
	h_tabell = Hashtabell(len(atom_list))
	for atom in atom_list:
		h_tabell.put(atom.name, atom)
	return h_tabell

# Prints the atom, depending on input if exists.
# Now uses tkinter to print atoms
def get_atom(h_tabell, mg_obj):
	usr_in = input("Atombeteckning: ")
	usr_in = usr_in.replace(" ","")
	while usr_in == "":
		print("Var god och mata in en atombeteckning\n")
		usr_in = input("Atombeteckning: ")

	try:
		atom = h_tabell.get(usr_in)
		r = Ruta(atom = atom.name, num = atom.weight)
		mg_obj.show(r)
		print(usr_in, "fanns med i hashtabellen.\n")
	except KeyError:
		print(usr_in, "fanns INTE med i hashtabellen.\n")

def main():
	atom_list = create_atom_list()

	mg_obj = Molgrafik()
	h_tabell = create_hash_table(atom_list)

	print("\n\n     *Hämta valfri atom*\n")
	while True:
		get_atom(h_tabell, mg_obj)

main()


