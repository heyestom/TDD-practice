import shapes

def determine_if_r_of_c(input_from_user):
	if input_from_user == "r":
		rectangle = make_rectangle()
		print rectangle
	elif input_from_user =="c":
		circle = make_circle()
		print circle

def make_rectangle():
	print "Rectangle side A length?"
	length = float(raw_input())
	print "Rectangle side B length?"
	height = float(raw_input())
	return shapes.Rectangle(length,height)

def make_circle():
	print "Cricle radius?"
	radius =  float(raw_input())
	return shapes.Circle(radius)


print "Shape: (c)ircle or (r)ectangle?"
determine_if_r_of_c(raw_input())