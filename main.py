import game_data
import art
import random
#print logo
# pick comparison a ---> pick() function
#print vs art
# pick comparison b ---> pick()function

#input choice
#check between a and b with ---> compare() function
#if choice is correct, score ++; else game over
#other choice becomes pick a and randomly pick b

#game() function

def pick():
  pick = random.choice(game_data.data)
  return pick

def show_choices(a, b):
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
  print(art.vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

def compare(a, b):
  if a > b:
    return "a"
  elif b > a:
    return "b"

def check_answer(choose, higher):
  if choose == higher:
    return True
  else:
    return False


def game():
  score = 0
  game_over = False
  print(art.logo)
  choice_a = pick()
  while game_over == False:
    choice_b = pick()
    #print(choice_a) 
    #print(choice_b)
    show_choices(choice_a, choice_b)
    higher = compare(choice_a["follower_count"], choice_b["follower_count"])
    choose = input("Who has more followers? Type 'A' or 'B': ").lower()
    if check_answer(choose, higher) == True: 
      score += 1
      print(f"You're right! Your current score is {score}.")
      choice_a = choice_b 
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      game_over = True


game()
