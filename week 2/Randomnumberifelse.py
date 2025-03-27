import random
n = random.randint(1,100)
while true:
print("Guess the number")
x = int(input("enter the number"))
if(x<n):
print("the number is too low")
elif(x>n):
print("the number is too high")
else:
print("congratulation you gussed the correct number")
break;
