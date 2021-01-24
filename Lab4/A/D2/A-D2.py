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

class Operation(object):
    
    def __init__(self, start_word, word_list):
        self.init_aplhabet()
        self.child_node_list = []

        self.start_word = start_word
        self.word_list = word_list

        self.old_tree = Bintree()
        self.queue = LinkedQ()
        self.d = {}

        self.start_node = Node(self.start_word)
        self.queue.put(self.start_node)

        self.start_word_bucket_list = self.make_buckets(self.start_word)
            
        self.dict_handler()

    
    def make_buckets(self, word):
        bucket_list = []
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            bucket_list.append(bucket)
        return bucket_list

    def init_aplhabet(self):
        self.alphabet = []
        for x in range(ord("a"),ord("z")+1):
            self.alphabet.append(chr(x))
        for x in ("å","ä","ö"):
            self.alphabet.append(x)

    def dict_handler(self):
        for line in self.word_list:
            word = line
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if not(bucket in self.d):
                    self.d[bucket] = [] # create list with bucket as key
                    self.d[bucket].append(word)
                else:
                    self.d[bucket].append(word)
        
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

def write_chain(child):
    output_string = recursive_write_chain(child,"")
    return(output_string)

def recursive_write_chain(child, io_string):
    if child.parent != None:
        io_string = recursive_write_chain(child.parent, io_string)
        if not(child.value in io_string):
            io_string = io_string + child.value + "\n"
        return io_string
    else:
        io_string = io_string + child.value + "\n"
        return io_string

def file_reader():
    word_list = []
    file_name = "word3.txt"
    f = open(file_name, "r", encoding="utf-8")
    for line in f:
        word = line[:-1]
        word_list.append(word)
    f.close()
    return word_list

# Gets the longest chain of a list of child
def get_longest_chain(obj):
    temp_list_length = []
    temp_list_string = []

    for child in obj.child_node_list:
        string = write_chain(child)
        temp_list_string.append(string)
        temp_list_length.append(string.count("\n"))
    maximum_length = max(temp_list_length)
    index = temp_list_length.index(maximum_length)

    return temp_list_string[index], maximum_length


final_list_str = []
final_list_len = []
word_list = file_reader()
for word in word_list:

    obj = Operation(word, word_list)

    # Keeps spawning childs of childs until there is no new childs
    while not (obj.queue.isEmpty()):
        nod = obj.queue.get()
        obj.make_children(nod)

    # Gets the longest chains of all childs and places it in a list
    str_chain, len_chain = get_longest_chain(obj)
    final_list_str.append(str_chain)
    final_list_len.append(len_chain)
maximum_length = max(final_list_len) 

print("All solutions: ")
temp = []
for i in range(0,len(final_list_len)):
    if final_list_len[i] == maximum_length:
        temp.append(final_list_str[i])
        print(final_list_str[i])

print("Length: " + str(maximum_length) + "\n")
print("Time: " + str(round(time.time() - start_time,2)) + " seconds")

