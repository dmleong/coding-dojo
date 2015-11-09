class MathDojo(object):
	def __init__(self): 
		self.total = 0

	def add(self, *num): 
		for i in range(0, len(num)):
			#Check if list or tuple
			if type(num[i]) is list or type(num[i]) is tuple:
				#unpack if list or tuple and increment
				for j in num[i]: 
					self.total += j
			else:
				self.total += num[i]
		# print self.total
		return self 

	def subtract(self, *num): 
		for i in range(0, len(num)):
			#check if list or tuple
			if type(num[i]) is list or type(num[i]) is tuple:
				#unpack if list or tuple and increment
				for j in num[i]: 
					self.total -= j
			else:
				self.total -= num[i]
		return self

	def result(self): 
		print self.total

md = MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()