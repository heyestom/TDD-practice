import unittest
from shapes import Rectangle, Circle
import math

class ShapeTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_rectangle_of_sides_1_and_1_has_circumference_4(self):
		# given 
		testRec = Rectangle(1,1)
		# when
		# expected
		self.assertEqual(testRec.circumference, 4)

	def test_rectangle_of_sides_2_and_3_has_circumference_10(self):
		testRec = Rectangle(2,3)

		self.assertEqual(testRec.circumference,10)

	def test_circle_of_radius_1_circumference_2pi(self):
		testCircle = Circle(1)
		self.assertEqual(testCircle.circumference, 2*math.pi)

	def test_circle_of_radius_2_circumference_4pi(self):
		testCircle = Circle(2)
		self.assertEqual(testCircle.circumference, 4*math.pi)


if __name__ == '__main__':
        unittest.main()