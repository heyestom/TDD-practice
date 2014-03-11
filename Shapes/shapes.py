import math

class Rectangle:
	def __init__(self, x,y):
		self.x = x
		self.y = y
		self.circumference = (self.x+self.y) *2
		self.area = x*y

	def __str__(self):
		return "Circumference : " + str(self.circumference) + "\nArea :" + str(self.area)


class Circle:
	def __init__(self, r):
		self.r =r
		self.circumference = r*2*math.pi
		self.area = (r*2*math.pi)**2

	def __str__(self):
		return "Circumference : " + str(self.circumference) + "\nArea :" + str(self.area)


