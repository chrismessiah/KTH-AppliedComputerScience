# Written by Christian Abdelmassih, Alexandra Runhem

from hashtest import *

def meny():

	atomlista = skapaAtomlista()
	hashtabell= lagraHashtabell(atomlista)

	user_in=input("Atombeteckning: ")

	atom=hashtabell.get(user_in)

	if atom != None:
		print (atom.namn+ " "+ str(atom.vikt))

	else:
		print ("Atomen " + user_in + " fanns inte.")	

meny()


	