# Author: Christian Abdelmassih, Alexandra Runhem

#Fist-in Last-out Stack system

class Node:
   def __init__(self, value):
      self.value = value
      self.next = None #Since the stack is empty from the beginning, there is no next node. 

class Stack:
   def __init__(self):
      self.top = None 

   def push(self,value):
      new_node = Node(value) 
      new_node.next = self.top #The new node is also going to be the top node.
      self.top = new_node

   def pop(self): #get
      value = self.top.value #Takes the top node
      self.top = self.top.next #The new top is now the one after the one we took
      return value

   def is_empty(self):
      if self.top == None: #Checks if the stack is empty
         return True
      else: 
         return False
