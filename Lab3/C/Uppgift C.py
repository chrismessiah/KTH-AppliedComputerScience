# Author: Christian Abdelmassih, Alexandra Runhem

from bintreeFile import Bintree
import time
import random

starttime = time.time()

tree = Bintree()
file_name = "word3.txt"

# create list and tree with random integers. 
value_list = [] 
for x in range(0,100000+1):
	value = random.randint(0,1000000)
	
	value_list.append(value)
	tree.put(value)

random.shuffle(value_list)

# find some value in that exists
x = 0
while True:
	x += 1
	if tree.exists(x):
		break

print("Finding value: " + str(x))

decimals = 10

# find the value in the tree
print("Running binary tree: ")
starttime = time.time()
tree.exists(x)
print("Time: "+ str( round(time.time() - starttime,decimals) ))

# find the value in the list
print("Running list: ")
starttime = time.time()
value_list.index(x)
print("Time: "+ str( round(time.time() - starttime,decimals) ))




