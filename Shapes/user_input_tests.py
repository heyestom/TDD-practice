import unittest
from user_input import determine_if_r_of_c ,make_rectangle, make_circle
import mock
import math

class ShapeTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_if_input_is_r_then_call_make_rectangle(self):
		with mock.patch('user_input.make_rectangle') as mock_method:
			determine_if_r_of_c("r")
			mock_method.assert_called_with()

	def test_if_input_is_c_then_call_make_circle(self):
		with mock.patch('user_input.make_circle') as mock_method:
			determine_if_r_of_c("c")
			mock_method.assert_called_with()

	def test_make_rectangle_takes_two_user_inputs_3_and_2_then_returns_a_rectangle(self):
		with mock.patch('__builtin__.raw_input', side_effect=['3', '2']):
			resultRectangle = make_rectangle()
			self.assertEqual(resultRectangle.circumference,10)

	def test_make_rectangle_takes_two_user_inputs_4_and_3_then_returns_a_rectangle(self):
		with mock.patch('__builtin__.raw_input', side_effect=['4', '3']):
			resultRectangle = make_rectangle()
			self.assertEqual(resultRectangle.circumference,14)

	def test_make_circle_takes_a_user_input_0point5_and_returns_a_circle(self):
		with mock.patch('__builtin__.raw_input', side_effect=['0.5']):
			resultCircle = make_circle()
			self.assertEqual(resultCircle.circumference,math.pi)

	def test_make_circle_takes_a_user_input_1_and_returns_a_circle(self):
		with mock.patch('__builtin__.raw_input', side_effect=['1']):
			resultCircle = make_circle()
			self.assertEqual(resultCircle.circumference,2*math.pi)


if __name__ == '__main__':
        unittest.main()		