class Stack(object):

	def __init__(self):
		self.data_stack = []

	def stack_height(self):
		return len(self.data_stack)

	def push(self,data):
		self.data_stack.append(data)

	def pop(self):
		if len(self.data_stack) <= 0:
			raise PopFromEmptyStackException("Attemped to pop a value from an empty stack.")
		return self.data_stack.pop()

	def add(self):
		first_number = self.pop()
		second_number = self.pop()
		self.push(first_number+second_number)

	def sub(self):
		first_number = self.pop()
		second_number = self.pop()
		self.push(first_number-second_number)

class PopFromEmptyStackException(Exception):
	pass