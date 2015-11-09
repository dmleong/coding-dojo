class Bike(object):
	def __init__(self, price, max_speed): 
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print self.price, self.max_speed, self.miles
		return self

	def ride(self):
		self.miles += 10
		print "Riding", self.miles
		return self

	def reverse(self): 
		self.miles -= 5
		print "Reversing", self.miles
		return self

bike1 = Bike(200, "25mph")
bike1.reverse().displayInfo().ride()

bike2 = Bike(300, "15mph").ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(1000, "30mph").reverse().reverse().reverse().displayInfo()