
my_list = range(1,101)
test_list = []

for number in my_list:
	if number % 3 == 0 and number % 5 == 0:
		test_list.append("FizzBuzz")
	elif number % 3 == 0:
		test_list.append("Fizz")
	elif number % 5 == 0:
		test_list.append("Buzz")
	else:
		test_list.append(number)
print test_list

