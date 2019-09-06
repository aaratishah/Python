#importing libraries
#from math import * (everything) to import every function available in that library
#from math import sqrt for particular code which needs only sqrt function
from math import *           #import math
def practice(n):
  print (int(sqrt(n)))          #print math.sqrt(n)
  
practice (5)



#source code to print all the functions available in math library
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print (everything) # Prints 'em all!