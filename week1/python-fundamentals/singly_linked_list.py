#Singly Linked List Implementation

# I've gotten the code started for you, showing you what your node class should look like
class Node(object):
	def __init__(self, val):
		# have our node hold a value
		self.value = val
		# initially it will not keep track of a node that comes after
		self.next = None

class SinglyLinkedList(object):
	def __init__(self):
		# initially set our head attribute to None
		self.head = None

	def traverse(self):
		# this method prints the values of of all the nodes in the list
		print "traversing..."
		if self.head != None:
			# we will initialize our current node as the head node
			current_node = self.head
			#print the value of the head node
			print current_node.value
			# this while loop moves us forward through the linked list
			while current_node.next != None:
				current_node = current_node.next
				print current_node.value
		# in the case that there are no nodes
		else:
			print "No nodes"
			return False

	# create a method to add a new node
	def add_node(self, val):
		# creating a new node
		new_node = Node(val)
		# if there are no nodes yet set the head attribute to our new node
		if self.head == None:
			self.head = new_node
		# else we will have to traverse to the last node in the chain and
		#add our new node to the end
		else:
			current_node = self.head
			while current_node.next != None:
				current_node = current_node.next
			current_node.next = new_node

	# now implement the following functions
	# as you are going through/when you finish each method,
	# make comments so you are aware of what's going on in each method
	def print_as_list(self):
		# this method should print all the values of the nodes in a list
		pass

	def remove_node(self):
		# this method should remove the last node in the linked list
		pass

	def insert_node_after(self, val):
		# this method should insert the node before the node with the value we pass in
		pass

	def remove_node_after(self, val):
		# this method should remove the node after the node with the value we pass in
		pass

	def find_value(self, val):
		# return True if val exists in the linked list
		# return False if val does not exist in the linked list
		pass

# creating a new instance of the Singly Linked List
sll = SinglyLinkedList()
# show how the traverse function works
sll.traverse()
# add more nodes and use traverse to look at all the values
sll.add_node(10)
sll.traverse()
sll.add_node(12)
sll.add_node(15)
sll.traverse()
