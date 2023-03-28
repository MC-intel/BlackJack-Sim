

'''

PLAYER FUNCTION

'''


from mmap import ACCESS_WRITE, ALLOCATIONGRANULARITY
from numpy import False_


def player_run():

    dealers_upcard = dealer_draw()


    print('GAME')
    import decimal

    strat = "Standard Strategy Tables"

    import CreateDecks as cde
    ranks = cde.generate_multiple_lists(1)
    ranks = cde.shuffle_lists_in_dict(ranks)[0]
    ranks = convert_numbers_to_strings(ranks)
   
    wins = 0
    losses = 0




# need to break some of these functions out and call them as modules like creatdecks^

# -----------   TO DO 
    create_deck(ranks, strat, losses, wins, dealers_upcard)

    

    

def convert_numbers_to_strings(lst):
    """
    Takes in a list and converts any numbers in the list into strings.
    """
    return [str(i) if type(i) == int or type(i) == float else i for i in lst]


def dealer_draw():

    import decimal

    #ranks = ['3', '10', '2', '2', '10', '10', '10', '10', '10']
    import CreateDecks as cde
    ranks = cde.generate_multiple_lists(1)
    ranks = cde.shuffle_lists_in_dict(ranks)[0]
    ranks = convert_numbers_to_strings(ranks)

# Create a deck of cards
    deck = []
    for rank in ranks:
        card = [rank]
        deck.append(card)


    # Define a variable to keep track of the current card index
    current_card_index = 0

    # Define a function to draw a card from the deck

    # Define the number of iterations
    #------- num_iterations = 5

    # Define a variable to keep track of the running total
    dealer_sum = 0

    print("Dealer Up-Card")
    dealers_upcard = card, current_card_index = draw_card(deck, current_card_index)
    dealers_upcard = card
    print("Dealer Hand:")


    dealer_hand(deck, card, dealer_sum, current_card_index, dealers_upcard)
    return dealers_upcard


def draw_card(deck, current_card_index):
    #nonlocal current_card_index
    if current_card_index >= len(deck):
        print("No more cards in the deck!")
        return None, current_card_index
    else:
        card = deck[current_card_index]
        print(card)
        current_card_index += 1
        return card, current_card_index



def dealer_hand(deck, card, dealer_sum, current_card_index, dealers_upcard):

    rank = card[0]
    for digit in rank:
        if digit.isdigit():
            dealer_sum += int(digit)

    # Loop through the iterations
    while True:
        # Draw a card from the deck
        card, current_card_index = draw_card(deck, current_card_index)
        
        # If there are no more cards in the deck, break out of the loop
        if card is None:
            break
        
        # Add the value of the card to the running total
        rank = card[0]
        if rank.isdigit():
            dealer_sum += int(rank)

        #Handling the ACE    
        else:
            dealer_sum += 11 if dealer_sum + 11 <= 21 else 1
        
        # Check if the player's sum is greater than or equal to 17 and break out of the loop if it is
        if dealer_sum >= 17 and dealer_sum <= 21:
            print(f"Dealer Total is: {dealer_sum}")
            print("Dealer Stops")
            break
        
        # Check if the player's sum is over 21 and break out of the loop and print "bust" in this case
        if dealer_sum > 21:
            print(f"Dealer Total is: {dealer_sum}")
            print("Dealer BUST")
            break
        
        # Print the new running total
    print(f"Final Dealer Total is: {dealer_sum}")
    print(' ')
    print('_____________________________________________________________________')
    print(' ')
    
    global final_dealer_sum
    final_dealer_sum = dealer_sum
    return final_dealer_sum

    create_deck(ranks,strat,losses,wins,dealers_upcard)
#_______________________________________________________________________________






def create_deck(ranks, strat, losses, wins, dealers_upcard):

    deck = []
    for rank in ranks:
        card = [rank]
        deck.append(card)
    # Define a variable to keep track of the current card index
    current_card_index = 0
    
    # Define a variable to keep track of the running total
    player_sum = 0
    num_cards = 0


    first_draw(deck, strat, current_card_index, num_cards, player_sum, losses, wins, dealers_upcard)



def first_draw(deck, strat, current_card_index, num_cards, player_sum, losses, wins, dealers_upcard):
  
  split_check = []
  acee = []
  card, current_card_index = draw_card(deck, current_card_index)
  num_cards = num_cards + 1
  rank = card[0]

  for digit in rank:
      split_check.append(rank)
      if rank == '10':
        value = 10
        player_sum += value
        break

      if rank == '11':
        acee.append(rank)
        value = 11
        player_sum += value
        break

      if digit.isdigit():
          player_sum += int(digit)


  first_card = card[0]
  double_down = False
  pairs = False
  split = False

  card, current_card_index = draw_card(deck, current_card_index)
  num_cards = num_cards + 1
  rank = card[0]
  for digit in rank:
      split_check.append(rank)
      if rank == '10':
        value = 10
        player_sum += value
        break

      if rank == '11':
        acee.append(rank)
        value = 11
        player_sum += value
        break

      if digit.isdigit():
          player_sum += int(digit)

  bs = BlackjackStrategy(Two_Card_Hard, Two_Card_Soft, Three_Card_Hard, Three_Card_Soft)
  print(f" ")


  if rank in first_card:
    pairs = True
    print("Pairs!")
    hand1, hand2 = split_check
    import splitrun as sp
    bs = BlackjackStrategy(Two_Card_Hard, Two_Card_Soft, Three_Card_Hard, Three_Card_Soft)
    print(f"SPLIT HINT: {bs.suggest_play(player_sum, dealers_upcard, num_cards, pairs)}")
    action = bs.suggest_play(player_sum, dealers_upcard, num_cards, pairs)
    print(' ')

    if 'Y' in action.upper():
      sp.split_run(deck, strat, current_card_index, num_cards, player_sum, losses, wins, rank, first_card, acee, hand1, hand2, dealers_upcard, final_dealer_sum)
      split = True

    elif 'S' in action.upper():
      splitstand = True
      print('Stood')

  if split == False:
    print(f"HAND: {split_check}")
    print(f"PLAYER SUM: {player_sum}")
    print(f"HINT: {bs.suggest_play(player_sum, dealers_upcard, num_cards, pairs)}")
    player_round(deck, strat, current_card_index, num_cards, player_sum, losses, wins, rank, first_card, acee, dealers_upcard)
  else:
    next


def player_round(deck, strat, current_card_index, num_cards, player_sum, losses, wins, rank, first_card,acee, dealers_upcard):

    while True:
        pairs = False
        bs = BlackjackStrategy(Two_Card_Hard, Two_Card_Soft, Three_Card_Hard, Three_Card_Soft)
        
        print(' ')
        # Ask the player to hit or stand
        action = bs.suggest_play(player_sum, dealers_upcard, num_cards, pairs)


        if action.upper() == 'H':
            # Draw a card from the deck
            card, current_card_index = draw_card(deck, current_card_index)
            num_cards = num_cards + 1
                        
            # If there are no more cards in the deck, break out of the loop
            if card is None:
                print("No more cards in the deck!")
                break

            # Add the value of the card to the running total
            rank = card[0]
            for digit in rank:
              
              if rank == '10':
                value = 10
                player_sum += value
                break

              if rank == '11':
                acee.append(rank)
                value = 11
                player_sum += value
                Ace = 'inhand'
                break

              if digit.isdigit():
                  player_sum += int(digit)
            
            # Print the new running total
            print(f"Hit: Hand Total is: {player_sum}")
            print(f"Hand Size: {num_cards} cards")
   
            print(f"HINT: {bs.suggest_play(player_sum, dealers_upcard, num_cards, pairs)}")





        if action.upper() == 'D':
          if num_cards <= 2:
            card, current_card_index = draw_card(deck, current_card_index)
            num_cards = num_cards + 1
            print('Double Down!')


            # If there are no more cards in the deck, break out of the loop
            if card is None:
                print("No more cards in the deck!")
                break


            for digit in rank:

              if rank == '10':
                value = 10
                player_sum += value
                break

              if rank == '11':
                acee.append(rank)
                value = 11
                player_sum += value
                break

              if digit.isdigit():
                  player_sum += int(digit)

            # Print the new running total
            print(f"Hit: Hand Total is: {player_sum}")
            print(f"Hand Size: {num_cards} cards")
            print(f"HINT: {bs.suggest_play(player_sum, dealers_upcard, num_cards, pairs)}")
            double_down = True
            break


        elif action.upper() == 'R':
            print(' ')
            print('SURRENDER')
            break

        elif action.upper() == 'S':
            print('STAND')
            break

        else:
            print("...")

        if player_sum > 21:
          if '11' in acee:
            player_sum = player_sum - 10
            print(f"ACE-SOFT: {player_sum}")
            acee = []
          else:
            print(' ')
            print("BUST: Player Loses!")
            break



#///////////////////////////////////////////////////////////////////////////////

# Print the final hand total
    print('_____________________________________________________________________')
    print(' ')
    print(f"Final Hand Total is: {player_sum}")

    print(f"Final Dealer Total: {final_dealer_sum}")
    print(' ')

    if final_dealer_sum > 21 and player_sum <= 21:
      wins = (wins + 1)

    elif player_sum > final_dealer_sum and player_sum <= 21:
      wins = (wins + 1)

    elif player_sum == final_dealer_sum:
      print("Push!")

    else:
      losses = (losses + 1)

    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(' ')
    print(f"Strategy: {strat}")

    print(' ')
    print('......//ROUND OVER\\\......')
    print(' ')








#STRATEGY TABLES CLASS

import pandas as pd
Two_Card_Hard = {'Player Hand': [21.0, 20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0], '2': ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H'], '3': ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'], '4': ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'], '5': ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'], '6': ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'], '7': ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H'], '8': ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H'], '9': ['S', 'S', 'S', 'S', 'S', 'R', 'H', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H'], '10': ['S', 'S', 'S', 'S', 'S', 'R', 'R', 'H', 'H', 'H', 'D', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '11': ['S', 'S', 'S', 'S', 'S', 'R', 'H', 'H', 'H', 'H', 'D', 'H', 'H', 'H', 'H', 'H', 'H', 'H']}
Two_Card_Soft = {'Player Hand': [22.0, 20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0], '2': ['H', 'S', 'S', 'D', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '3': ['H', 'S', 'S', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '4': ['H', 'S', 'S', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '5': ['H', 'S', 'S', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '6': ['H', 'S', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '7': ['H', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '8': ['H', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '9': ['H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '10': ['H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '11': ['H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']}
Three_Card_Hard = {'Player Hand': [21.0, 20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0], '2': ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '3': ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '4': ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H'], '5': ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H'], '6': ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H'], '7': ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '8': ['S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '9': ['S', 'S', 'S', 'S', 'S', 'R', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '10': ['S', 'S', 'S', 'S', 'S', 'R', 'R', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '11': ['S', 'S', 'S', 'S', 'S', 'R', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']}
Three_Card_Soft = {'Player Hand': [22.0, 20.0, 19.0, 18.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0], '2': ['H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '3': ['H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '4': ['H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '5': ['H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '6': ['H', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '7': ['H', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '8': ['H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '9': ['H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '10': ['H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], '11': ['H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']}

Pairs = {'Player_Hand': [22.0, 20.0, 18.0, 16.0, 14.0, 12.0, 10.0, 8.0, 6.0, 4.0], '2': ['Y', 'S', 'Y', 'Y', 'Y', 'Y', 'H', 'H', 'Y', 'Y'], '3': ['Y', 'S', 'Y', 'Y', 'Y', 'Y', 'H', 'H', 'Y', 'Y'], '4': ['Y', 'S', 'Y', 'Y', 'Y', 'Y', 'H', 'H', 'Y', 'Y'], '5': ['Y', 'S', 'Y', 'Y', 'Y', 'Y', 'D', 'Y', 'Y', 'Y'], '6': ['Y', 'S', 'Y', 'Y', 'Y', 'Y', 'D', 'Y', 'Y', 'Y'], '7': ['Y', 'S', 'S', 'Y', 'Y', 'H', 'H', 'H', 'H', 'H'], '8': ['Y', 'S', 'Y', 'Y', 'H', 'H', 'H', 'H', 'H', 'H'], '9': ['Y', 'S', 'Y', 'R', 'H', 'H', 'H', 'H', 'H', 'H'], '10': ['Y', 'S', 'S', 'R', 'H', 'H', 'H', 'H', 'H', 'H'], '11': ['Y', 'S', 'S', 'R', 'H', 'H', 'H', 'H', 'H', 'H']}

Two_Card_Hard_df = pd.DataFrame(Two_Card_Hard)
Two_Card_Soft_df = pd.DataFrame(Two_Card_Soft)
Three_Card_Hard_df = pd.DataFrame(Three_Card_Hard)
Three_Card_Soft_df = pd.DataFrame(Three_Card_Soft)

Pairs_df = pd.DataFrame(Pairs)

class BlackjackStrategy:
    def __init__(self, two_card_hard, two_card_soft, three_card_hard, three_card_soft):

        self.two_card_hard_df = pd.DataFrame(two_card_hard)
        self.two_card_soft_df = pd.DataFrame(two_card_soft)
        self.three_card_hard_df = pd.DataFrame(three_card_hard)
        self.three_card_soft_df = pd.DataFrame(three_card_soft)

    def suggest_play(self, player_sum, dealers_upcard, num_cards, pairs):
        dealers_upcard = str(dealers_upcard[0])
        print(dealers_upcard)
        if num_cards == 2 and player_sum in self.two_card_hard_df['Player Hand'].values:
            row_idx = self.two_card_hard_df.index[self.two_card_hard_df['Player Hand'] == player_sum].tolist()[0]
            col_idx = self.two_card_hard_df.columns.get_loc(dealers_upcard)
            return self.two_card_hard_df.iloc[row_idx, col_idx]
        elif num_cards == 2 and player_sum in self.two_card_soft_df['Player Hand'].values:
            row_idx = self.two_card_soft_df.index[self.two_card_soft_df['Player Hand'] == player_sum].tolist()[0]
            print(dealers_upcard)
            col_idx = self.two_card_soft_df.columns.get_loc(dealers_upcard)
            return self.two_card_soft_df.iloc[row_idx, col_idx]
        elif num_cards >= 3 and player_sum in self.three_card_hard_df['Player Hand'].values:
            row_idx = self.three_card_hard_df.index[self.three_card_hard_df['Player Hand'] == player_sum].tolist()[0]
            col_idx = self.three_card_hard_df.columns.get_loc(dealers_upcard)
            return self.three_card_hard_df.iloc[row_idx, col_idx]
        elif num_cards >= 3 and player_sum - 10 in self.three_card_soft_df['Player Hand'].values:
            row_idx = self.three_card_soft_df.index[self.three_card_soft_df['Player Hand'] == player_sum - 10].tolist()[0]
            col_idx = self.three_card_soft_df.columns.get_loc(dealers_upcard)
            return self.three_card_soft_df.iloc[row_idx, col_idx]
        elif num_cards == 2 and pairs == True and player_sum in self.Pairs_df['Player Hand'].values:
            row_idx = self.Pairs_df.index[self.Pairs_df['Player Hand'] == player_sum].tolist()[0]
            col_idx = self.Pairs_df.columns.get_loc(dealers_upcard)
            return self.Pairs_df.iloc[row_idx, col_idx]
        else:
            return 'No Strategy Available'


bs = BlackjackStrategy(Two_Card_Hard, Two_Card_Soft, Three_Card_Hard, Three_Card_Soft)

