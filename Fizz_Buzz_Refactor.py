

def divis(a, b): 
	"""testing if a can devide by b"""
	if a % b == 0:
		return True
	else:
		return False
upperlimit = 100

my_list = range(1,upperlimit)
test_list = []

for value in my_list:
	if divis(value, 15):
		test_list.append("FizzBuzz")
	elif divis(value, 3):
		test_list.append("Fizz")
	elif divis (value, 5):
		test_list.append("Buzz")
	else:
		test_list.append(value)
print test_list


