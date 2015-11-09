class Underscore(object):
	def map(self, list, callback):
		new_list = []
		for i in list:
			new_list.append(callback(i))
		print new_list

	def reduce(self, list, callback):
		new_list = []
		total = 0
		for i in list: 
			new_list.append(callback(i))
		for j in new_list:
			total += j
		print total

	def find(self, list, callback):
		for i in range(0, len(list)): 
			if callback(list[i]) == True: 
				print list[i]
				break
			else: 
				return False

	def filter(self, list, callback):
		result = []
		for i in range(0, len(list)): 
			if callback(list[i]) == True: 
				result.append(list[i])
		print result

	def reject(self, list, callback):
		result = []
		for i in range(0, len(list)): 
			if callback(list[i]) != True: 
				result.append(list[i])
		print result

# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
maps = _.map([1, 2, 4, 8, 6], lambda x: x % 2 == 0)
evens = _.filter([1, 2, 4, 8, 6], lambda x: x % 2 == 0)
odds = _.reject([1, 2, 4, 3, 8, 6], lambda x: x % 2 == 0)
findItem = _.find([2, 4, 8, 6, 7], lambda x: x % 2 == 0)
reduceItem = _.reduce([47,11,42,13], lambda x: x**2)
