# type() function returns the type of the data it receives as an argument

print (type(3.5))
print (type(3))
print (type("rt"))


# use of type() function

def distance_from_zero(num):
      if type(num) == int or type(num) == float:
         print (abs(num))
      else:
         print ("Nope")

distance_from_zero(10.04)