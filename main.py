from art import logo, vs
from game_data import data
import random

#without function:
# a_name = a_dic["name"]
# a_descr = a_dic["description"]
# a_country = a_dic["country"]
# print(f"Compare A: {a_name}, a  {a_descr}, from {a_country}")   

# print(vs)

# b_name = b_dic["name"]
# b_descr = b_dic["description"]
# b_country = b_dic["country"]
# print(f"Against B: {b_name}, a  {b_descr}, from {b_country}")   

def format_dic(dic_para): 
  """Take the dictionary values from keys and returns the printable format"""
  name = dic_para["name"]
  descr = dic_para["description"]
  country = dic_para["country"]
  return f"{name}, a  {descr}, from {country}" 
# Function is later called inside a f string  
# print(f"Compare A: {format_dic(dic_a)}.")
# print(vs)
# print(f"Against B: {format_dic(dic_b)}.")

def compare(choice_para, a_followers, b_followers):
  """Take the user guess and follower counts and return True if they got it right.Or False if they got it wrong."""
  # #long version:
  # if a_followers > b_followers and choice_para == "a":
  #   return True
  # elif a_followers > b_followers and choice_para == "b":
  #   return False
  # elif a_followers < b_followers and choice_para == "a":
  #   return False
  # elif a_followers < b_followers and choice_para == "b":
  #   return True
  # #easier version:
  # if a_followers > b_followers:
  #   if choice_para == "a":
  #     return True
  #   else:
  #     return False
  # else:???
  #short and mind bending version:
  if a_followers > b_followers:
    return choice_para == "a"
  else:
    return choice_para == "b"

print(logo)
score = 0
end_game = False
dic_b = random.choice(data)
while not end_game:
  #Make dictionary at position B become the next dictionary at position A. 
  dic_a = dic_b
  dic_b = random.choice(data)
  #Make sure a and b are not the same AND the randomly generated new b is still not the same
  while dic_a == dic_b:
    dic_b = random.choice(data)
  
  print(f"Compare A: {format_dic(dic_a)}.")
  print(vs)
  print(f"Against B: {format_dic(dic_b)}.")

  # #testing
  # print(dic_a["follower_count"])
  # print(dic_b["follower_count"])

  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  #Call the compare function and pass on artuments to check if user' answer is correct
  answer = compare(choice, dic_a["follower_count"], dic_b["follower_count"])
  #Give user feedback on their answer and score
  if answer == True:
    score += 1
    print(f"You are right, your current score is {score}.")
  else:
    print(f"Sorry you are incorrect. Your final score is {score}.")
    end_game = True
    