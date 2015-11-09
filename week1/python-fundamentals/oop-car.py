class Car(object): 
	def __init__(self, price, speed, fuel, mileage): 
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax
		self.tax()
		self.display_all()

	def tax(self): 
		if self.price >= 10000: 
			self.tax = ".15"
		else: 
			self.tax = ".12"

	def display_all(self): 
		print "Price:", self.price
		print "Speed:", self.speed
		print "Fuel:", self.fuel
		print "Mileage:", self.mileage
		print "Tax:", self.tax

car1 = Car(2000, "35mph", "full", "15mpg")
car2 = Car(2000, "5mpg", "not full", "105mpg")
car3 = Car(2000, "15mpg", "kind of full", "95mpg")
car4 = Car(2000, "25mpg", "full", "25mpg")
car5 = Car(2000, "25mpg", "full", "55mpg")