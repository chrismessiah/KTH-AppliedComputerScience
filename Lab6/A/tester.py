# Author: Christian Abdelmassih, Alexandra Runhem

from lab6 import *

obj = SyntaxOperation(use_stdin = False, print_active = False)

filename = "input_atoms.txt"
f = open(filename, "r", encoding="UTF-8")
total_paragraphs = int((len(f.readlines()) - 4)/3)
f.close()

correct_tests = 0
faulty_tests = 0

f = open(filename, "r", encoding="UTF-8")
for i in range(0,4):
	f.readline()

for i in range(0,total_paragraphs):
	atom = f.readline()
	e_result = f.readline().replace("\n","")
	f.readline()

	r_result = obj.main(row = [atom,""])
	if r_result == e_result:
		print(atom.replace("\n",""),"kördes som förväntat.")
		correct_tests += 1
	else:
		print("ERROR: Oväntat resultat för",atom)
		faulty_tests += 1

print("\n–––––––––––––––––––––––––––––––––––––––––––––––\nAntal felfria testfall:",str(correct_tests),"\nAntal felaktiga testfall:",str(faulty_tests))
