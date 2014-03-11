import unittest
from Stack import Stack, PopFromEmptyStackException

class StackTest(unittest.TestCase):

 	def setUp(self):
 		self.testStack = Stack()

	def tearDown(self):
		self.testStack = 0

	def test_push_to_stack_when_empty_makes_stack_height_1(self):
		self.testStack.push(1)
		self.assertEqual(self.testStack.stack_height(), 1)

	def test_push_to_stack_when_height_is_1_results_in_height_2(self):
		# given a stack with hidght 0
		self.assertEqual(self.testStack.stack_height(),0)
		self.testStack.push(1)
		self.assertEqual(self.testStack.stack_height(), 1)
		# when a number is pushed to the stack
		self.testStack.push(1)
		# expect that stack height to be 1
		self.assertEqual(self.testStack.stack_height(), 2)

	def test_stack_behaves_first_in_last_out(self):
		# given a stack with a number pushed onto it
		first_in_number = 345
		second_in_number = 23423
		third_in_number = -1443
		self.testStack.push(first_in_number)
		self.testStack.push(second_in_number)
		self.testStack.push(third_in_number)

		# when stack is popped 
		first_out_number = self.testStack.pop()
		second_out_number = self.testStack.pop()
		third_out_number = self.testStack.pop()
		
		# expect that the numbers are returned in reverse order
		self.assertEqual(third_in_number,first_out_number)
		self.assertEqual(second_in_number,second_out_number)
		self.assertEqual(first_in_number,third_out_number)

	def test_pop_from_empty_stack_thorws_empty_stack_exception(self):
		# given an empty stack stack
		self.assertEqual(self.testStack.stack_height(),0)
		# when the stack is popped
		# expect that an empty stack exception is thrown
		self.assertRaises(PopFromEmptyStackException, self.testStack.pop)

	def test_add_should_take_two_numbers_off_the_stack_sum_them_then_push_result(self):
		# given a stack with at least 2 numbers on it
		first_number = 1
		second_number = 2
		self.testStack.push(first_number)
		self.testStack.push(second_number)
		current_stack_height = self.testStack.stack_height()

		# when add is called
		self.testStack.add()

		# expect the stack height to be one lower and the last item on the stack to be equal to the sum of the 2 pushed numbers
		self.assertEqual(current_stack_height-1,self.testStack.stack_height())
		self.assertEqual(first_number+second_number, self.testStack.pop())

	def test_sub_should_take_two_numbers_off_the_stack_sum_them_then_push_result(self):
		# given a stack with at least 2 numbers on it
		first_number = 1
		second_number = 2
		self.testStack.push(first_number)
		self.testStack.push(second_number)
		current_stack_height = self.testStack.stack_height()

		# when sub is called
		self.testStack.sub()

		# expect the stack height to be one lower and the last item on the stack to be equal to the sum of the 2 pushed numbers
		self.assertEqual(current_stack_height-1,self.testStack.stack_height())
		self.assertEqual(second_number-first_number, self.testStack.pop())

	def test_add_on_empty_stack_thorws_empty_stack_exception(self):
		# given an empty stack stack
		self.assertEqual(self.testStack.stack_height(),0)
		# when the stack is popped
		# expect that an empty stack exception is thrown
		self.assertRaises(PopFromEmptyStackException, self.testStack.add)

	def test_sub_on_empty_stack_thorws_empty_stack_exception(self):
		# given an empty stack stack
		self.assertEqual(self.testStack.stack_height(),0)
		# when the stack is popped
		# expect that an empty stack exception is thrown
		self.assertRaises(PopFromEmptyStackException, self.testStack.sub)

if __name__ == '__main__':
	unittest.main()
