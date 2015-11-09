class Node(object): 
	def __init__(self, val): 
		self.value = val 
		self.next = None 
		self.prev = None

class DoublyLinkedList(object): 
	def __init__(self): 
		self.head = None
		self.tail = None

	def add_node(self, val): 
		new_node = Node(val)
		#If no head, set new node as head
		if self.head == None: 
			self.head = new_node
			self.tail = new_node
		else: 
			current_node = self.head
			#if next not none (tail) continue traversing
			while current_node.next != None: 
				current_node = current_node.next
			#if tail, add to end
			current_node.next = new_node 
			#set prev pointer to current node
			new_node.prev = current_node
			#set new tail to new node
			self.tail = new_node

	#Traverse forward
	def traverse_forward(self): 
		if self.head != None: 
			current_node = self.head 
			#If next node is not tail
			while current_node.next != None: 
				#Set current as next and traverse forward
				print "Traverse forward current", current_node.value
				current_node = current_node.next
				print "Traverse forward current", current_node.value
		else: 
			print "No nodes"
			return False
	
	#Traverse backwards 
	def traverse_back(self):
		if self.tail != None: 
			#Set current node to the tail (tail is set when new node added)
			current_node = self.tail 
			#Check to see if at the head, traverse backwards and print
			while current_node.prev != None: 
				print "Traverse backwards current", current_node.value
				current_node = current_node.prev
			print "Traverse backwards current", current_node.value
		else: 
			print "No nodes"
			return False

	def print_as_list(self): 
		#Create empty list
		value_list = []
		if self.head != None: 
			current_node = self.head 
			#Start at head and check if next is not tail
			while current_node.next != None: 
				#Add current node to list and traverse forward
				value_list.append(current_node.value)
				current_node = current_node.next 
			value_list.append(current_node.value)
			print value_list
		else: 
			print "No nodes"
			return False

	def remove_node_from_end(self): 
		if self.head != None: 
			current_node = self.head 
			while current_node.next.next != None: 
				current_node = current_node.next
			current_node.next.prev = None
			current_node.next = None
			self.tail = current_node

	def remove_node(self, val): 
		if self.head != None: 
			current_node = self.head 
			#If val is the head 
			if self.head.value == val: 
				self.head.next.prev = None
				self.head = self.head.next
			#If val is the tail
			elif self.tail.value == val: 
				self.tail.prev.next = None
				self.tail = self.tail.prev
			else: 
				while current_node.next.value != val: 
					current_node = current_node.next 
					#If val is not in list 
					if current_node.next.value != val: 
						print "Value not in list"
						return False
				#Set next next node's prev pointer to current node
				current_node.next.next.prev = current_node 
				#Set next node to current's next next pointer
				current_node.next = current_node.next.next

	def insert_node_after(self, val, insert_val): 
		if self.head != None: 
			#Create new node
			current_node = self.head 
			new_node = Node(insert_val)
			#If val is first item in list, insert after 
			if self.head.value == val: 
				self.head.next.prev = new_node
				new_node.prev = self.head
				new_node.next = self.head.next
				self.head.next = new_node
			#If tail is val, create new tail
			elif self.tail.value == val: 
				self.tail.next = new_node
				new_node.prev = self.tail
				self.tail = new_node
			else: 
				#If neither head nor tail, traverse through
				while current_node.value != val: 
					current_node = current_node.next 
					#If val is not in list, give error message
					if current_node.value != val: 
						print "Value not in list"
						return False
				#Set new node's next to current node's next 
				new_node.next = current_node.next
				#Insert new node next to current node
				current_node.next = new_node
				#Set new node next prev's pointer to new node
				new_node.next.prev = new_node
				#Set new node's prev pointer to current node 
				new_node.prev = current_node



dll = DoublyLinkedList()
dll.add_node(10)
dll.add_node(20)
dll.add_node(30)
dll.add_node(35)
dll.print_as_list()
# dll.remove_node_from_end()
# dll.remove_node(35)
# dll.print_as_list()
# dll.remove_node(10)
dll.print_as_list()
dll.insert_node_after(35, 25)
dll.print_as_list()
