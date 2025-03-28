import random
n = random.randint(1,100)
y = 0
while (y<5):
 print("Guess the number")
 x = int(input("enter the number"))
 y = y+1
 print("please try again")
 if(x<n):
  print("the number is too low")
 elif(x>n):
  print("the number is too high")
 elif(x==n):
  print("congratulation you gussed the correct number")
else:
 print("you lost the game")
   
