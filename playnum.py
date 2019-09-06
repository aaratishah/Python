# built-in functions 
# max, min, abs
# part 1

def biggest_number(*args):    # *args takes variable number of arguments 
      print (max(args))
      return (max(args))
    
def smallest_number(*args):
  print (min(args))
  return min(args)

def distance_from_zero(arg):
  print (abs(arg))
  return abs(arg)

def calculate(arg, ar):
  print (pow(arg, ar))
  return (pow(arg, ar))

biggest_number(-10, -5, 5, 10, 20)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
calculate(5,2)


# part 2
# we can also directly pass the arguments

maximum = max(3, 6, 8)
print (maximum)

minimum = min(3.4, 5.6, 3.3)
print (minimum)

absolute = abs (-42)
print (absolute)