# class student:
#     def __init__(self,name,email,subject):
#       self.name=name
#       self.email=email
#       self.subject=subject
    
#     def student_con(self):
#        return f"{self.name},{self.email},{self.subject}"
    
#     class student_info:
#        def __init__(student):
#           student = student


# fullname = 'John Ade'
import random
number_to_guess= random.randint(1,10)
guesses=0
print("welcome to guess game!")
print("guess a number between 1 and 10.")

while True:

  user_guess=input("enter your guess: ")

  if not user_guess.isdigit():
    print("invalid input! please enter anumber.")
    continue

  user_guess=int(user_guess)
  guesses+=1

  if user_guess==number_to_guess:
    print(f"congratulations! your guesses  it in {guesses } attempts.")
    break
  elif user_guess<number_to_guess:
    print("too low! try again")
    
  else:

    print("too high! try again")

# import random 
# name_guess=random.randint(1,10)
# guess=0
# print("welcome to uc game show!")
# print("guess any number from 1 to 10")
# while True:

#   if not name_guess.isdigit():
#     print("invalid input! please enter a number").
#     continue
#   name_guess=int(name_guess)
#   guess +=1
#   if guess ==number_ to_guess:
#     print("")