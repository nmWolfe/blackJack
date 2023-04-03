import random

""" Modelling required items for a game of blackjack """

# Global variables to allow access from classes
suits = ('Hearts','Diamonds','Spades','Clubs')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,
        'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

class Card:
    """ Class representing a Card Object """
    def __init__(self,suit,rank):
        """Initialize the cards"""
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        """Print statement to show the suit and value of the card"""
        return self.rank + ' of ' + self.suit

class Deck:
    """ Class representing a deck of cards """ 
    def __init__(self):
        # Emoty list to fill with a created deck
        self.all_cards = []
        # Pull from the global variables Suit and Rank to create a list of cards
        for suit in suits:
            for rank in ranks:
                # Create an instance of the Card class
                created_card = Card(suit,rank)
                # Append to the new deck list 
                self.all_cards.append(created_card)
    
    def shuffle_deck(self):
        """ Shuffle the deck """
        random.shuffle(self.all_cards)

    def starting_deal(self):
        """Deal the starting cards"""
        deal = []
        while len(deal) != 2:
            deal.append(self.all_cards.pop())
        return deal

    def deal_one_card(self):
        """Pop a single card off the new deck, modelling a hit"""
        return self.all_cards.pop()
    
class Player:
    """A class to model a player in a game of blackjack"""
    def __init__(self,name):
        self.name = name
        # Emoty list to account for cards dealt to the player
        self.hand = []

    def hit(self,card):
        """Model a 'hit' in blackjack (adding a card to players hand)"""
        self.hand.append(card)

    def has_ace(self):
        """Check for an ace, and ask for value"""
        for card in self.hand:
            if card.value == 11:
                print("You've got an ace!")
                while True:
                    try:
                        card.value = int(input("Would you like to play the ace as an 11, or 1? "))
                        break
                    except ValueError:
                        print("Enter 11, or 1. ")
                        pass
            else:
                pass

    def display_total(self):
        """Display a sum of current cards in players hand"""
        # Will throw an error up if ACE is pulled as it will nest a list - Fix this.
        total = []
        for card in self.hand:
            total.append(card.value)
        return sum(total)

    def clear_hand(self):
        """ A class to wipe the previous hands for a new game """
        self.hand = []

    def __str__(self):
        # Need to figure out how to display all cards in hand
        # Could look at using print displays in game. Not ideal. 
        return f"[ {self.hand[0]} ] and [ {self.hand[1]} ]"

class Dealer:
    """A Class to model the dealer in Blackjack"""
    def __init__(self):
        """Initialize the Dealer class"""
        self.hand = []

    def display_total(self):
        """ Display hand value """
        total = []
        for card in self.hand:
            total.append(card.value)
        return sum(total)

    def has_ace(self):
        """Check for an ace, and ask for value"""
        for card in self.hand:
            if card.value == 11:
                print("The dealer will play the Ace as a 1")
                card.value = 1
            else:
                pass

    def __str__(self):
        """ Display the dealers initial card """
        return f"[ {self.hand[0]} ]"

class Betting:
    """ A class to model the betting system for blackjack"""
    def __init__(self, player, account=0):
        """Initialize the class"""
        self.player = player
        self.account = account

    def add_funds(self, amount):
        """Add chips / money"""
        self.account += amount
        # Display amount
        print(f"You have {self.account} chips")

    def place_bet(self, amount=0):
        """Placing bets - removing funds"""
        self.amount = amount
        # Check for available funds before bet
        while self.amount > self.account:
            # Deling with incorrect amounts
            print("Sorry, you do not have enough chips to make this bet.")
            print(f"Available funds: {self.account}")
            additional_funds = input("Would you like to add more chips? Y/N ")
            # If/else to deal with amounts
            if additional_funds.lower() == 'y':
                self.add_funds(int(input("Amount: ")))
                self.place_bet(int(input("Place your bet: ")))
                self.account - self.amount
                return self.amount
            else:
                print("Please place a lower bet.")
                self.place_bet(int(input("Place your bet: ")))
                self.account - self.amount
                return self.amount
        # Bet is fine, continue
        while self.amount <= self.account:
            self.account -= self.amount
            return self.amount
            
    def __str__(self):
        """Show amount avaiable at the start of new games"""
        return f"{self.account}"

class Table:
    """A class to model a table for holding bets"""
    def __init__(self,table=0):
        """Initialize the class"""
        self.table = table
    
    def on_the_table(self,bet):
        """Taking the player bet"""
        self.bet = bet
        self.table += bet
        print(f"Currently on the table: {self.table} chips")

    def push(self):
        """If draw return money"""
        return self.table
        
    def winner(self):
        """Return the bet to the winner"""
        return self.table * 2

""" Rules for the game of Blackjack """
blackjack_rules = """
- Blackjack hands are scored by their point total. 
- The player is dealt two cards face up.
- The dealer gets one card face up, and one card face down. 
- Cards 2 through 10 are worth their face value, and face cards (jack, queen, king) are also worth 10.
- The player can either 'hit' or 'stick';
- If the player hits, they are dealt another card, face up.
- If the player sticks, they retain their total, and it is the dealers turn.
- The hand with the highest total wins as long as it doesn't exceed 21;
  a hand with a higher total than 21 is said to BUST. 
"""