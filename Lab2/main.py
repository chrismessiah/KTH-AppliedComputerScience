# Author: Christian Abdelmassih, Alexandra Runhem


from LinkedQFile import LinkedQ # First-in First-out
from StackFile import Stack 	# First-in Last-out

# Runs the magic trick and returns the card-layout as a queue 
def magic(queue): 
	final_queue = LinkedQ()
	i = True
	while not queue.is_empty():
		value = queue.get()
		
		if i == False:
			final_queue.put(value) #Put place value last
		
		elif i == True:
			queue.put(value)
		
		i = not(i) # Toggles 'i'

	return final_queue

# Flips the queue order by putting the cards in the stack and then putting them back in the queue, returns the final queue
def flip_queue(queue):
	staq = Stack()
	queue, staq = queue_to_stack(queue, staq)
	queue, staq = stack_to_queue(queue, staq)
	return queue

# Pushes all cards from the queue to the stack, returns the stack
def queue_to_stack(queue, staq):
	while not(queue.is_empty()):
		value = queue.get()
		staq.push(value)
	return queue, staq

# Puts all cards in the queue from the stack, returns queue
def stack_to_queue(queue, staq):
	while not(staq.is_empty()):
		value = staq.pop()
		queue.put(value)
	return queue, staq

# Runs the reversed magictrick (reverse to magic()). 
def reversed_magic(queue):
	staq = Stack()

	queue, staq = queue_to_stack(queue, staq)
	while not(staq.is_empty()):		
		queue.put(staq.pop()) # takes a value from the top of the stack and puts it last in the queue
		queue.put(queue.get()) # takes the first value from the queue and puts it last in the queue
	
	queue = flip_queue(queue) # Flips the queue to get the right order.
	return queue

# Reads userinput and creates a inital queue holding the cards, returns the initial queue.
def queue_init():
	value_str = input("Vilken ordning ligger korten i? Separera korten med mellanslag: ")
	value_list = value_str.split(" ") 
	
	# Puts everything exept empty spaces in the list
	new_value_list = [] 
	for value in value_list:
		if value != "":
			new_value_list.append(value)
	value_list = new_value_list 
	
	# Creates LinkedQ object
	queue = LinkedQ()
	for value in value_list:
		queue.put(value)

	return(queue)

# Runs program, prints result.
def main():
	usr_input = input("Mata in siffor för att välja alternativ till kortkonsten.\n1. Framlänges\n2. Baklänges\n\nSvar: ")
	
	queue = queue_init() 
	if usr_input == "1": # Ordinary
		final_queue = magic(queue)
	elif usr_input == "2": # Reversed
		final_queue = reversed_magic(queue)
	else:
		print("Var god följ instruktionerna!")
		final_queue = ""
		
	print(final_queue) 

while True:
	main()




