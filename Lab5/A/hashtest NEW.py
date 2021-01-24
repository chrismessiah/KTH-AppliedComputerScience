#Testar klassen Hashtabell i filen hashfil.py
from hashtabell import *
import unittest

class Testclass(unittest.TestCase): 

    # Checks if put and get gives the correct value
    def test_if_input_is_output(self):
        atom_list = create_atom_list()
        hash_table_obj = create_hash_table_with_atoms(atom_list)

        for atom in atom_list:
            new_atom = hash_table_obj.get(atom.key)
            self.assertEqual(atom.key, new_atom.key) # Check for expected result Equal
            self.assertEqual(atom.value, new_atom.value) #
        
    # Checks if the object returned by the get() is a node
    def test_retrival_of_node_object(self):
        node = Node("FOO",123)
        hash_table_obj = Hashtabell(10)
        hash_table_obj.put("FOO", node)
        something = hash_table_obj.get("FOO")
        self.assertEqual(something, node) # Verification of a condition

    # Checks if how the hash-table responds to non-inserted items
    def test_existance_of_non_included(self):
        atom_list = create_atom_list()
        hash_table_obj = create_hash_table_with_atoms(atom_list)

        with self.assertRaises(KeyError): # Verify that a specific exception gets raised
             hash_table_obj.get("Allanballan")

    # Checks how the hash-table keeps track of multiple items with the same key
    def test_doublette_tracking(self):
        hash_table_obj = Hashtabell(20)
        node_list = []
        for i in range(0,10):
            node = Node("Hejsan!", 77+i)
            node_list.append(node)
            hash_table_obj.put("Hejsan!", node)

        last_inputted_value = node_list[9]

        for x in range(0,10):
            self.assertEqual(hash_table_obj.get("Hejsan!"), last_inputted_value)

    def test_collision_with_too_short_hashtable(self):
        hash_table_obj = Hashtabell(1)
        node_list = []
        amount_of_inputs = 1000
        for i in range(0,amount_of_inputs):
            key = "Nyckelnummer: " + str(i) 
            node = Node(key, i)
            node_list.append(node)
            hash_table_obj.put(key, node)


        for i in range(0,amount_of_inputs):
            key = "Nyckelnummer: " + str(i) 
            self.assertEqual(hash_table_obj.get(key), node_list[i])

    # Checks if the hash-table is capable of handling collisions.
    def test_collision(self):
        hash_table_obj = Hashtabell(112*2)
        atom1 = Node("Cu", 63.546)
        atom2 = Node("Se", 78.96)
        
        hash_table_obj.put(atom1.key, atom1)
        hash_table_obj.put(atom2.key, atom2)
        
        self.assertEqual(hash_table_obj.get("Cu"), atom1)
        self.assertEqual(hash_table_obj.get("Se"), atom2)


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
        final_atom_list.append(Node(atom_name, atom_weight))
    return final_atom_list

def create_hash_table_with_atoms(atom_list):
    hash_table = Hashtabell(len(atom_list))
    for atom in atom_list:
        hash_table.put(atom.key, atom)
    return hash_table

def skapaAtomlista():
    data = "H  1.00794;\
He 4.002602;\
Li 6.941;\
Be 9.012182;\
B  10.811;\
C  12.0107;\
N  14.0067;\
O  15.9994;\
F  18.9984032;\
Ne 20.1797;\
Na 22.98976928;\
Mg 24.3050;\
Al 26.9815386;\
Si 28.0855;\
P  30.973762;\
S  32.065;\
Cl 35.453;\
K  39.0983;\
Ar 39.948;\
Ca 40.078;\
Sc 44.955912;\
Ti 47.867;\
V  50.9415;\
Cr 51.9961;\
Mn 54.938045;\
Fe 55.845;\
Ni 58.6934;\
Co 58.933195;\
Cu 63.546;\
Zn 65.38;\
Ga 69.723;\
Ge 72.64;\
As 74.92160;\
Se 78.96;\
Br 79.904;\
Kr 83.798;\
Rb 85.4678;\
Sr 87.62;\
Y  88.90585;\
Zr 91.224;\
Nb 92.90638;\
Mo 95.96;\
Tc 98;\
Ru 101.07;\
Rh 102.90550;\
Pd 106.42;\
Ag 107.8682;\
Cd 112.411;\
In 114.818;\
Sn 118.710;\
Sb 121.760;\
I  126.90447;\
Te 127.60;\
Xe 131.293;\
Cs 132.9054519;\
Ba 137.327;\
La 138.90547;\
Ce 140.116;\
Pr 140.90765;\
Nd 144.242;\
Pm 145;\
Sm 150.36;\
Eu 151.964;\
Gd 157.25;\
Tb 158.92535;\
Dy 162.500;\
Ho 164.93032;\
Er 167.259;\
Tm 168.93421;\
Yb 173.054;\
Lu 174.9668;\
Hf 178.49;\
Ta 180.94788;\
W  183.84;\
Re 186.207;\
Os 190.23;\
Ir 192.217;\
Pt 195.084;\
Au 196.966569;\
Hg 200.59;\
Tl 204.3833;\
Pb 207.2;\
Bi 208.98040;\
Po 209;\
At 210;\
Rn 222;\
Fr 223;\
Ra 226;\
Ac 227;\
Pa 231.03588;\
Th 232.03806;\
Np 237;\
U  238.02891;\
Am 243;\
Pu 244;\
Cm 247;\
Bk 247;\
Cf 251;\
Es 252;\
Fm 257;\
Md 258;\
No 259;\
Lr 262;\
Rf 265;\
Db 268;\
Hs 270;\
Sg 271;\
Bh 272;\
Mt 276;\
Rg 280;\
Ds 281;\
Cn 285"
    atomlista = data.split(";")
    return atomlista


unittest.main()





















