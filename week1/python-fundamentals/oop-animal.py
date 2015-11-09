class Animal(object):
	def __init__(self, name): 
		self.name = name
		self.health = 100

	def walk(self): 
		self.health -= 1
		return self

	def run(self): 
		self.health -= 1
		return self

	def displayHealth(self): 
		print self.name, self.health

animal1 = Animal("Cheetah")
animal1.walk().walk().walk().run().run().displayHealth()
