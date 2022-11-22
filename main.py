# Angry Goblin: Getting Started
import random
number_of_doors = 5
print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and excitement (!)")

player_name = input("What is your name? ")
print(player_name + ", can you find the goblin?")
print("|_|"* number_of_doors)

goblin_position = random.randint(1,number_of_doors)

keep_trying = True

while keep_trying:
  guessed_position = input("Can you guess where the goblin is hiding? ")
  guessed_position = int(guessed_position)
  if guessed_position == goblin_position:
    print("Well done. You've found the goblin.")
    keep_trying = False
  else:
    print("No, sorry. The goblin is still hiding somewhere.")
print("Thank you for playing. Now get back to work!")