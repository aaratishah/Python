import random 

def func():
    dice = [1, 2, 3, 4, 5, 6]
    for n in dice:
        print("you got " + str(random.choice(dice)))
        break
       
m = input ("enter anything to roll the dice ")
func()    

