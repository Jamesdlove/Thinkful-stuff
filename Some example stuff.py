# void function, no return value, no parameters
def say_hello():
  print "hello"

say_hello()

def my_sum(a, b):
  """ Returns the sum of the two formal parameters."""
  return a + b

print my_sum(2, 2)
print my_sum(my_sum(2,3), my_sum(5,5))

a = my_sum(10, 5)
b = 3
print my_sum(a, b)

print sum([1, 2, 3, 4, 5])

def my_sum2(l):
  s = 0
  for x in l:
  s += x
  return s

def greeter1(name):
  print "Hello there {}".format(name)

def greeter2(name):
  print "Howdy {}".format(name)

def greet(l, greeter):
  for name in l:
  greeter(name)

greet(["sam", "bob", "barney"], greeter2)
greet(["sam", "bob", "barney"], greeter1)

def make_adder(a):
  def inner(x):
  return a + x
  return inner

two_adder = make_adder(2)
print two_adder(10)
#12

four_adder = make_adder(4)
print four_adder(20)