import random
import art
from replit import clear

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  # blackjack -> 0
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if computer_score == user_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
  
def blackjack():
  user_cards = []
  computer_cards = []

  # print logo
  print(art.logo)

  # initial 2 cards each side
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  is_game_over = False
  hand_turn = 1
  while not is_game_over:
    print(f"Hand {hand_turn}:")
    print(f"Your cards: {user_cards}, current score: {user_score if user_score != 0 else 21}")
    print(f"Computer's first card: {computer_cards[0]}")
    print("---------------------------------------------")
    # Check blackjack for user and computer and check user over 21 scores -> end game
    if(user_score == 0 or computer_score == 0 or user_score > 21):
      is_game_over = True
    else:
      ask = input("Type 'y' to get another card, type 'n' to pass: ")
      print("---------------------------------------------")
      if ask == 'y':
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        hand_turn += 1
      else:
        is_game_over = True
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  
  print(f"Your final hand: {user_cards}, final score: {user_score if user_score != 0 else 21}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  print("---------------------------------------------")
  
while input("Do you want to play a game of Blackjack. Type 'y' or 'n': ") == 'y':
  clear()
  blackjack()