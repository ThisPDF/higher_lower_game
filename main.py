import game_data
import random
import art
from replit import clear


def select(first, second):
  if first > second:
    return "a"
  elif first < second: 
    return "b"
  else:
    return "ab"
  
def first_choice():
  print(art.logo)
  first_value = random.choice(game_data.data)
  second_value = random.choice(game_data.data)
  print(f"{first_value['name']} is a {first_value['description']} from {first_value['country']}")
  print(art.vs)
  print(f"{second_value['name']} is a {second_value['description']} from {second_value['country']}")
  good_value = select(first_value['follower_count'], second_value['follower_count'])
  if(input(f"Witch one has more followers \"A\" {first_value['name']} or \"B\" {second_value['name']}: ").lower() in good_value):
    clear()
    return second_value
  else:
    print("You lose with a score of 0")
def game():
  first = first_choice()
  second = random.choice(game_data.data)
  score = 1
  while True:
    print(art.logo)
    print(f"Your score: {score}")
    print(f"{first['name']} is a {first['description']} from {first['country']}")
    print(art.vs)
    print(f"{second['name']} is a {second['description']} from {second['country']}")
    good_value = select(first['follower_count'], second['follower_count'])
    if(input(f"Witch one has more followers \"A\" {first['name']} or \"B\" {second['name']}: ").lower() in good_value):
      score += 1
      clear()
      first = second
      second = random.choice(game_data.data)
    else:
      clear()
      print(art.logo)
      print(f"You lose with a score of {score}")
      quit()
  
  

game()