# Author: Christian Abdelmassih, Alexandra Runhem

# Keys: He_
# value: list of words: Hea, Heb, Hec
from bintreeFile import Bintree
from LinkedQFile import LinkedQ
import time

start_time = time.time()

class Node():
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

# A class with all needed attributes to finish the task
class Operation(object):
    
    def __init__(self):
        self.init_aplhabet()
        self.child_node_list = []

        self.start_word = "söt"

        self.old_tree = Bintree()
        self.queue = LinkedQ()
        self.d = {}

        self.start_node = Node(self.start_word)
        self.queue.put(self.start_node)

        self.start_word_bucket_list = self.make_buckets(self.start_word)
        self.file_reader()

    # Creates a list of bucketed words
    def make_buckets(self, word):
        bucket_list = []
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            bucket_list.append(bucket)
        return bucket_list

    # Creates alphabet attribute
    def init_aplhabet(self):
        self.alphabet = []
        for x in range(ord("a"),ord("z")+1):
            self.alphabet.append(chr(x))
        for x in ("å","ä","ö"):
            self.alphabet.append(x)

    # Reads file and places lines in dict sorted
    def file_reader(self):
        self.word_list = []

        file_name = "word3.txt"
        f = open(file_name, "r", encoding="utf-8")
        for line in f:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if not(bucket in self.d):
                    self.d[bucket] = [] # create list with bucket as key
                    self.d[bucket].append(word)
                else:
                    self.d[bucket].append(word)
        f.close()
   
    # Creates children of parent_node by getting the corresponding child from graph object     
    def make_children(self, parent_node):
        word = parent_node.value
        bucket_list = self.make_buckets(word)

        for bucket in bucket_list:
            word_list = self.d[bucket]
            
            for new_word in word_list:
                child_node = Node(new_word, parent=parent_node)
                
                if self.queue.isEmpty(): 
                    self.child_node_list.append(child_node)
                
                if not(self.old_tree.exists(new_word)):
                    self.old_tree.put(new_word)
                    self.queue.put(child_node)

# Writes out the chain and exits the program
def write_chain(child):
    output_string = recursive_write_chain(child,"")
    return(output_string)

# recursive chail function, will go on until it has reached the final parent
def recursive_write_chain(child, io_string):
    if child.parent != None:
        io_string = recursive_write_chain(child.parent, io_string)
        if child.value != child.parent.value: 
            if not(child.value in io_string):
                io_string = io_string + child.value + "\n"
        return io_string
    else:
        io_string = io_string + child.value + "\n"
        return io_string

# Gets the longest chain of a list of child
def get_longest_chain(obj):
    temp_list_length = []
    temp_list_string = []

    for child in obj.child_node_list:
        string = write_chain(child)
        temp_list_string.append(string)
        temp_list_length.append(string.count("\n"))
    maximum_length = max(temp_list_length)

    final_list = []
    i = 0
    for length in temp_list_length:
        if length == maximum_length:
            print(temp_list_string[i])
            final_list.append(temp_list_string[i])
        i += 1
    return final_list, maximum_length

obj = Operation()
while not (obj.queue.isEmpty()):
    nod = obj.queue.get()
    obj.make_children(nod)

final_list, maximum_length= get_longest_chain(obj)

print("\n\n".join(final_list))
print("Length: " + str(maximum_length) + "\n")
print("Time: " + str(round(time.time() - start_time,2)) + " seconds")

