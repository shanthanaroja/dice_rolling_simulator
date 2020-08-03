import random
try:
    min=int(input("Enter minimum value of die:"))
    max=int(input("Enter maximum value of die:"))
except:
    print("Invalid inputs, using default values ")
    min=1
    max=6
roll_again=True
while roll_again:
    print(random.randint(min,max))
    again=input("Do you want to roll the die again? ")
    if again.lower()=='yes' or again.lower()=='y':
        continue
    else:
        break
