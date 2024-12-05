
import random


print("***Guess the number game***\n You have 3 chances")

attempt=3


randomNumber=random.randint(1,5)

while attempt > 0:
 guess=int(input("Enter your guess :"))


 if guess == randomNumber:
     print("correct answer")
     break
 else:
     print("incorrect answer")
     attempt=attempt-1






if attempt==0:
   print("You Lost, the correct answer is",randomNumber )
 
