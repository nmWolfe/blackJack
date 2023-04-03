import classes
import os
from time import sleep

""" Gameplay for BlackJack """

"""Welcome and Rules"""

welcome = input("""Welcome to the game of BlackJack! 
If you would like to see the rules to play, type 'rules'.
If you would like to quit, press 'Q'.
Otherwise, press any key to continue.
""")

if welcome.lower() == 'rules':
    # Display rules imported from CLASSES
    print(classes.blackjack_rules)
    ready = input("Ready to play? Y/N ")
    if ready.lower() == 'y':
        new_game = True
    else:
        new_game = False

elif welcome.lower() == 'q':
    new_game = False

else:
    print("Ok, lets play")
    new_game = True

while new_game:

    # Get player name and welcome
    player_one = classes.Player(input("Please enter your name, player one: "))
    print(f"Welcome, {player_one.name.title()}")

    # Get funds for game bets
    while True:
        try:
            player_one_chips = classes.Betting(player_one.name,
            int(input("How many chips would you like to play with today? ")))
            break
        except ValueError:
            pass
        print("Please enter a numerical value")

    # Set the house takings to 0
    house_takings = 0

    # Game begins here
    game_on = True

    # Win and Loss counter
    wins = 0
    losses = 0
    push = 0

    while game_on:

        # Create the table
        table = classes.Table()
        # Create the deck
        new_deck = classes.Deck()
        # Shuffle the deck
        new_deck.shuffle_deck()
        # This will reset the dealers hand each time (encountered an error)
        dealer = classes.Dealer()
        # Wipe the players previous hand
        player_one.clear_hand()
        # Deal cards to player
        print("Dealing cards..")
        sleep(0.5)
        player_one.hand.extend(new_deck.starting_deal())
        # Display the player, their cards, and the current total
        print(f"{player_one.name.title()} - {player_one} - {player_one.display_total()}")
        sleep(1)
        # Deals cards to the dealer 
        dealer.hand.extend(new_deck.starting_deal())
        print(f"Dealer - {dealer}")
        sleep(1)
        # Setting the boolean to run the dealer turn
        dealer_turn = False
        # Setting the boolean to run the player turn
        player_turn = True

        """ Player Turn """

        while player_turn:
            
            player_one.has_ace()
            # Get bets
            while True:
                try:
                    bet = player_one_chips.place_bet(int(input("Place your bets ")))
                    break
                except ValueError:
                    pass
                print("Please enter a numerical value.")
            # Displaying bets on the table
            table.on_the_table(bet)

            # Asking the player to hit or stick 
            hit_or_stick = input(f"Ok, {player_one.name.title()}, hit, or stick on {player_one.display_total()}? ")

            if hit_or_stick == 'hit':
                # Player hits - adding a card to their hand
                player_one.hit(new_deck.deal_one_card())
                print(f"[ {player_one.hand[-1]} ] - {player_one.display_total()}")
                player_one.has_ace()
                if player_one.display_total() > 21:
                    # If player goes over 21 and bust
                    print("You have BUST!")
                    losses +=1 
                    house_takings += table.winner()
                    break
                elif player_one.display_total() == 21:
                    # Assumes the player would stick on 21
                    print("Blackjack, baby!! ")
                    dealer_turn = True
                    break
                else:
                    continue
            # Player sticks - show their total value & set the dealers turn to TRUE
            elif hit_or_stick == 'stick':
                print(f"Total - {player_one.display_total()}")
                dealer_turn = True
                break
            else:
                print("Cannot compute BEEP BOOP BEEP")

        """ Dealer / House turn """

        while dealer_turn:

            # Simulating the table - card reveals
            print("The dealer flips his second card!")
            sleep(0.5)
            print(f"It's the [ {dealer.hand[1]} ]")
            sleep(1)
            print(f"Dealer - [ {dealer.hand[0]} ] and [ {dealer.hand[1]} ] - {dealer.display_total()}")
            sleep(1)
            print("The Dealer is thinking..")
            sleep(1)

            # Checking for dealer Ace, if total hand value above 16
            if dealer.display_total() != 21 or dealer.display_total() < player_one.display_total():
                dealer.has_ace()
            else:
                pass

            # Dealer must hit if total is lower than 16
            while dealer.display_total() < 22:
                # Dealer wins
                if dealer.display_total() == 21:
                    print("Blackjack!")
                    print(dealer.display_total()) 
                    break
                
                elif dealer.display_total() < 17:
                    dealer.hand.append(new_deck.deal_one_card())
                    # Pausing for effect here
                    print("The dealer hits!")
                    sleep(1)
                    # Display dealers hand
                    print(f"[ {dealer.hand[-1]} ] - {dealer.display_total()}")
                    
                else:
                    break

            """ This decides winners and returns winnings"""
            # Dealer bust
            if dealer.display_total() > 21:
                print("The House BUSTS!")
                print(f"{player_one.name.title()} wins. Please collect your winnings.")
                wins += 1
                player_one_chips.add_funds(table.winner())
            # Dealer wins
            elif dealer.display_total() > player_one.display_total():
                print("The house always wins...")
                losses += 1
                house_takings += table.winner()
            # Player wins
            elif dealer.display_total() < player_one.display_total():
                print(f"{player_one.name.title()} wins! Please collect your winnings.")
                wins += 1
                player_one_chips.add_funds(table.winner())
            # Draw - dealer wins
            elif dealer.display_total() == player_one.display_total():
                print("The game pushes!")
                push += 1
                player_one_chips += table.push()
            # Break out of loop for replay
            break

        play_again = False

        # Ask if the player would  like to play again
        while play_again != True:
            # Accounting for zero money at the end of a game
            """
            if player_one_chips <= 0:
                add_funds = input("Would you like to add more chips? Y/N")
                if add_funds.lower == 'y':
                    player_one_chips.add_funds(int(input("Chip Amount: ")))
                    continue
                else:
                    continue
            """
            replay = input("Care to play another hand? Y/N ")
            if replay.lower() == 'y':
                os.system('clear')
                # Display the wins and losses before the next game!
                print(f"** {player_one.name.title()} - {wins} | House - {losses} **") 
                print(f"You have {player_one_chips} chips")
                print(f"The house has taken {house_takings} chips from you.")
                break
            elif replay.lower() == 'n':
                # End the game
                game_on = False
                new_game = False
                break

while new_game == False:
    # Clear screen
    os.system('clear')
    # Display wins and losses 
    print(f"Wins - {wins}")
    print(f"Losses - {losses}")
    print(f"You walk away with {player_one_chips} chips!")
    # Thanks
    print("Thank you for playing.")
    break
