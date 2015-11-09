class Node(object): 
	def __init__(self, val): 
		self.value = val
		self.next = None

class SinglyLinkedList(object): 
	def __init__(self): 
		self.head = None

	def traverse(self): 
		if self.head != None: 
			current_node = self.head 
			print current_node.value
			while current_node.next != None: 
				current_node = current_node.next
				print current_node.value
		else: 
			print "No nodes"
			return False

	def add_node(self, val): 
		new_node = Node(val)

		if self.head == None: 
			self.head = new_node
		else: 
			current_node = self.head
			while current_node.next != None: 
				current_node = current_node.next
			current_node.next = new_node 

	def print_as_list(self): 
		value_list = []
		if self.head != None: 
			current_node = self.head 
			while current_node.next != None: 
				value_list.append(current_node.value)
				current_node = current_node.next 
			value_list.append(current_node.value)
			print value_list
			print self.head
		else: 
			print "No nodes"
			return False

	def remove_node(self): 
		if self.head != None: 
			current_node = self.head 
		#Remove if list only has one node
		if self.head.next == None: 
			self.head = None
			print self.head
			#While not last, set current_node to next node 
			while current_node.next != None: 
				current_node = current_node.next
				#If only one item in list, remove it
				if current_node.next.next == None: 
					current_node.next = None
		else: 
			print "No nodes"
			return False

	# this method should insert the node after the node with the value we pass in
	def insert_node_after(self, val, new): 
		#New node with value passed in
		new_node = Node(new)
		#If not the head
		if self.head != None: 
			current_node = self.head
			#Traverse through until current_node = value, starting at head
			while current_node.value != val:
				current_node = current_node.next
				if current_node.next == None: 
					print "Value not in list"
					return False
			#Add new node to current next, then set current node to new
			new_node.next = current_node.next
			current_node.next = new_node

		else: 
			#If nothing in list, set head to new node
			self.head = new_node

	# this method should remove the node after the node with the value we pass in
	def remove_node_after(self, val): 
		#Check to see if the list is empty 
		if self.head != None: 
			current_node = self.head
			temp_pointer = current_node
			#Traverse through list to find value
			while current_node.value != val: 
				current_node = current_node.next 
				if current_node.next == None: 
					print "Value not in list"
					return False
			#Set val after selected node to temp
			temp_pointer = current_node.next
			#Set current pointer to the moved pointer 
			current_node.next = temp_pointer.next


	# return True if val exists in the linked list
	# return False if val does not exist in the linked list
	def find_value(self, val): 
		if self.head != None: 
			current_node = self.head 
			while current_node.value != val: 
				current_node = current_node.next 
				if current_node.next == None: 
						print val, "not in list"
						return False
			print val, "in list"

# creating a new instance of the Singly Linked List
sll = SinglyLinkedList()
sll.add_node(10)
sll.add_node(23)
sll.add_node(15)
sll.add_node(50)
sll.traverse()
sll.print_as_list()
sll.remove_node()
print "Add nodes"
sll.print_as_list()
sll.insert_node_after(23, 30)
print "Insert node"
sll.print_as_list()
print "Remove node after head"
sll.remove_node_after(10)
sll.print_as_list()
print "Remove node"
sll.print_as_list()
sll.find_value(15)