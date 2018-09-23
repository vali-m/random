#BlackJack
from IPython.display import clear_output
import random

class Blackjack:
    
    def __init__(self):
        #1. Create Players
        self.players = []
        self.players.append(Dealer())
        self.players.append(Player("Vali"))
        #2. Prepare deck
        self.deck = list(range(2,15))
        self.deck.extend(self.deck)
        self.deck.extend(self.deck)
        random.shuffle(self.deck)
        print(f"Deck is shuffled as: {self.deck}")
#         list.append()
                    #maybe ask for game init info
        #3. Initialize other things
        self.turn = 0
        self.cardCnt = 0
        self.hideCards = False
        
        #4. Give out first cards
            #Dealer - [*] and [?]
        dealer = self.players[0]
        self.hit(dealer)
        dealer.revealHand()
        self.hit(dealer)
        
            #Others - 2x[?]
        for player in self.players[1:]:
            self.hit(player)
            self.hit(player)
            
        self.display()
        print("Good Luck and Have Fun!")
        input("Press any Key to continue")
        
        for player in self.players[1:]:
            while not player.isBust() and not player.stays:
                self.playTurn(player)
                
        
        while not dealer.isBust() and 17 > dealer.handSum:
            self.playTurn(dealer)
        
        winner = self.findWinner()
        if winner == None:
            print(f"Nobody won!")
            return
        
        self.revealCards()
        self.display()
        print(f"{type(winner)} {winner.name} has won the game with a score of {winner.handSum}")
        return
    
    def revealCards(self):
        for player in self.players:
            player.revealHand()
            
    def findWinner(self):
        notBustPlayers = [player for player in self.players if not player.isBust()]
        #In case of tie, dealer or random first player wins
        return max(notBustPlayers, default=None, key=lambda player : player.handSum)
    
    def playTurn(self, player):
        clear_output()
        print(f"*************[{self.turn}] - {player.name}*************************")
        self.display()
        self.turn += 1
        print(f"Turn {self.turn} - Player {player.name} plays (currently has {player.handSum}) ")
        while True:
            try:
                print("Note: you can exit with 'X'")
                playerChoice = input("Hit (H) or Stay (S)? ").upper()
                if playerChoice == 'H':
                    self.hit(player)        
                elif playerChoice == 'S':
                    player.stays = True
                elif playerChoice == 'X':
                    exit()
                else:
                    raise Exception("Invalid Character, not 'H' or 'S'!")
            except:
                print("Invalid Input!")
            else:
                break
        
    def hit(self, player):
        self.cardCnt += 1
        cardNum = self.deck[self.cardCnt]
        player.hit(cardNum)
    
    def display(self):
        for player in self.players:
            print(str(player))
            print(player.getHand())

class Card:
    def __init__(self,num):
        self.isVisible = False
        if num == 11:
            self.val = 11
            self.face = 'A'
        elif num == 12:
            self.val = 10
            self.face = 'J'
        elif num == 13:
            self.val = 10
            self.face = 'Q'
        elif num == 14:
            self.val = 10
            self.face = 'K'
        else:
            self.val = num
            self.face = str(num)
            
    def __str__(self):
        if self.isVisible:
            return "[" + self.face + "]"
        else:
            return "[*]"
    
        
    
        
class Player:
    def __init__(self,name,balance=100):
        self.balance = balance
        self.cardCnt = 0
        self.cards = []
        self.handSum = 0
        self.name = name
        self.stays = False
        print(f"Player {self.name} has been created with balance = {self.balance}")
    
    def isBust(self):
        if self.handSum <= 21:
            return False
        else:
            # Check for Aces
            aces = list(filter(lambda card : card.val == 11, self.cards))
            if len(aces) > 0:
                #One ace becomes used up
                aces[0].val = 1
                self.handSum -= 10
                return False
            else:
                return True
                

    def hit(self, cardNum):
        self.cardCnt += 1
        card = Card(cardNum)
        card.isVisible = True
        self.cards.append(card)
        self.handSum += card.val
        if self.isBust():
            print(f"{type(self)} {self.name} is bust having {self.handSum}!!")

    
    def getSum(self):
        return int(sum(self.cards))

    def getHand(self):
        return " ".join([str(card) for card in self.cards])
    
    def revealHand(self):
        for card in self.cards:
            card.isVisible = True
    
    def __str__(self):
        return f'{self.name} - {self.balance}: {self.handSum}'
    
class Dealer(Player):
    
        def __init__(self,balance=100):
            Player.__init__(self, "Dealer", balance)
#             print(f"Dealer has been created with balance = {self.balance}")
            
game = Blackjack()
# game.deck
#game.play()