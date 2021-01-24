# Author: Christian Abdelmassih, Alexandra Runhem

# Keys: He_
# value: list of words: Hea, Heb, Hec
from bintreeFile import Bintree
from LinkedQFile import LinkedQ
from adjGraph import Graph
from adjGraph import Vertex
import time

start_time = time.time()

# Builds graph-object by reading input-file and creating dictionaries with arrays as values,
# the keys to the dictionary are bracketed words such as HEL_O
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r', encoding="UTF-8")
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

class Node():
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent

# A class with all needed attributes to finish the task
class Operation(object):
    
    def __init__(self, start_time):
        self.init_aplhabet()

        # Used for file with 3 letter-words ––––––––––––––
        
        self.g = buildGraph("word3.txt")
        self.start_word = "söt"
        self.end_word = "sur"

        # Used for file with 5 letter-words ––––––––––––––
        
        # self.start_word = "anstå"
        # self.end_word = "anslå"
        # self.g = buildGraph("word5.txt")

        self.old_tree = Bintree()
        self.queue = LinkedQ()

        self.start_time = start_time

        self.start_node = Node(self.start_word)
        self.queue.put(self.start_node)

    # Creates alphabet attribute
    def init_aplhabet(self):
        self.alphabet = []
        for x in range(ord("a"),ord("z")+1):
            self.alphabet.append(chr(x))
        for x in ("å","ä","ö"):
            self.alphabet.append(x)
    
    # Creates children of parent_node by getting the corresponding child from graph object 
    def make_children(self, parent_node):
        word = parent_node.word
        parent_vertex = self.g.getVertex(word) # Gets the vertex corresponding with the word

        if parent_vertex == None:
            print("Error there is no way to " + self.end_word)
            pass
        else:
            connected_vertices = parent_vertex.getConnections() # Gets the connected vertecies

            for vertex in connected_vertices:
                vertex_name = vertex.getId() # Gets the word
                new_word = vertex_name

                child_node = Node(new_word, parent=parent_node)

                if new_word == self.end_word: 
                    self.queue.put(child_node)
                    write_chain(child_node, self.start_time, self)
         
                if not(self.old_tree.exists(new_word)):
                    self.old_tree.put(new_word)
                    self.queue.put(child_node)

                if new_word != self.end_word and self.queue.isEmpty():
                    print("Error there is no way to " + self.end_word)
                    raise SystemExit

# Writes out the chain and exits the program
def write_chain(child, start_time, obj):
    output_string = recursive_write_chain(child,"")
    #obj.queue.flush_queue()
    print(output_string)
    print("Length: " + str(output_string.count("\n")) + " words")
    print("Time: " + str(round(time.time() - start_time,2)) + " seconds\n\n")
    raise SystemExit # Comment out to see ALL solutions

# recursive chail function, will go on until it has reached the final parent
def recursive_write_chain(child, io_string):
    if child.parent != None:
        io_string = recursive_write_chain(child.parent, io_string)
        io_string = io_string + child.word + "\n"
        return io_string
    else:
        io_string = io_string + child.word + "\n"
        return io_string

obj = Operation(start_time)

while not(obj.queue.isEmpty()):
    nod = obj.queue.get()
    obj.make_children(nod)





