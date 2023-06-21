import random

def guess_number():
     computer = random.randint(1,100)
     attempt = 0
     while True:
           guess = int(input("Enter the guess number: "))
           attempt +=1 

           if computer < guess:
                 print("Too bigg")
           elif computer > guess:
                 print("Too small")

           else:
                 print(f"Congratulations!!! You guess the right number in {attempt} attempts")  
                 break
           
     new = input("Do you want to play again , y/n: ")
     if new == "y":
           guess_number()
   
        
guess_number()

