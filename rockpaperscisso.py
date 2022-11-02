# import random
# print("Welcome to Rock Paper Scissors Game")
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors")
# if user_choice == "0":
#     print(rock)
# elif user_choice == "1":
#     print(paper)
# elif user_choice == "2":
#     print(scissors)
#
# comp_choice = random.randint(0,2)
# if comp_choice == 0:
#     print(comp_choice)
#     print(rock)
# elif comp_choice == 1:
#     print(comp_choice)
#     print(paper)
# elif comp_choice == 2:
#     print(comp_choice)
#     print(scissors)
#
# if user_choice == "0" and comp_choice == 2 or user_choice == "1" and comp_choice == 0 or user_choice == "2" and comp_choice == 1:
#     print(f"You Win, because you choose {user_choice}")#correct
# elif user_choice == "0" and comp_choice == 0 or user_choice == "1" and comp_choice == 1 or user_choice == "2" and comp_choice == 2:
#     print(f"Its a tie Your choice {user_choice} Computer's Choice {comp_choice}")
# else:
#     print(f"Computer chose {comp_choice}, You lose ")


list_of_numbers = range(1,101)
print(list_of_numbers)