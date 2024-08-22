#Deck class
import random
#Global values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class card():

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank +" of "+self.suit

class Deck():
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                Created_Card=card(suit,rank)
                self.all_cards.append(Created_Card)

    

    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

class hand():

    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    
    
    def add_card(self,card):
        #card passed in is from Deck.deal()--> single card(suit,rank)
        self.cards.append(card)
        #Finding the value of each card in the hand
        self.value+=values[card.rank]

        #Track the aces
        if card.rank=='Ace':
            self.aces+=1
        
    def adjust_for_ace(self):
        #if total value >21 and i still have an ace the
        #Change the ace to value of 1
        while self.value >21 and self.aces:
            self.value-=10
            self.aces-=1

class chip():
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    
    def win_bet(self):
        self.total +=self.bet

    def lose_bet(self):
        self.total -=self.bet

    
def take_bet(chips):
    while True:

        try:
            chip.bet=int(input("HOw many chips would you like to bet?"))
        
        except:
                print("Sorry, Please provide an integer")
        else:
                if(chip.bet>chip.total):
                    print("Sorry, you don't have enough chip, You have ",chip.total)
                else:
                    break

def hit(Deck, hand):
    single_card=Deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x=input("Hit or stand: h or s")
        if x[0].lower=='h':
            hit(Deck,hand)
        elif(x[0].lower=='s'):
            print("Player stnds dealer's turn:")
            playing =False
        else:
            print("wrong input")
            continue
        break

def show_some(player,dealer):


    #show only one of the dealer's card
    print("\nDealer's Hand:")
    print("\nFirst card hidden!")
    print(dealer.card[1])

    #show all cards of  and player
    print("\nPlayer's Hand cards:")
    for card in player.card:
        print(card)
    

def show_all(player,dealer):
    #show all the dealer's cards
    #calculate the values of cards of dealer
    print("\Dealer's Hand cards:")
    for card in dealer.cards:
        print(card)
    #instead of for we can also do this
    print("\nDealer cards:",*dealer.cards,sep='\n')

    print(f"Value of dealers hand is:{dealer.value}")
    #show the all cards of player and also their value
    print("\nPlayer's Hand cards:")
    for card in player.card:
        print(card)
    
    print("\nPlayer's hand card value:",player.value)

def player_busts(player,dealer,chips):
    print("Bush Player!")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("Player Wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Player wins ! dealer busted")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and player tie!")



if __name__== '__main__':
    while True:
        print("************BLACK JACK*************\n")

        deck_obj=Deck()
        deck_obj.shuffle()

        player_hand=hand()
        player_hand.add_card(Deck.deal_one())
        player_hand.add_card(Deck.deal_one())

        dealer_hand=hand()
        dealer_hand.add_card(Deck.deal_one())
        dealer_hand.add_card(Deck.deal_one())
