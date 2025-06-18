""" Homework 6: OOP and Inheritance """
import random,math

#####################
# Required Problems #
#####################

class methods:
    """The base class for encryption methods."""

    def encrypt(self, message):
        """Encrypt the message."""
        pass

class shiftcipher(methods):
    """A class for shift cipher encryption method.
    >>> cipher = shiftcipher(3)
    >>> cipher.encrypt('hello')
    'khoor'
    >>> cipher.encrypt('world')
    'zruog'
    """

    def __init__(self, shift):
        """
        Initialize the shift cipher with a shift.
        If shift is greater than 26, shift = shift % 26.
        """
        "*** YOUR CODE HERE ***"
        while shift<0:
            shift+=26
        while shift>=26:
            shift-=26
        if shift<26 and shift >=0:
            self.shift=shift

    def encrypt(self, message):
        """Encrypt the message by shifting each character by the shift."""
        "*** YOUR CODE HERE ***"
        aft_encrypt=[]
        for i in message:
            t=ord(i)+self.shift
            if t>122:
                t-=26
            aft_encrypt.append(chr(t))
        return "".join(aft_encrypt)

class dictionarycipher(methods):
    """A class for dictionary cipher encryption method.
    >>> cipher = dictionarycipher({'h': 'a', 'e': 'b', 'l': 'c', 'o': 'd', 'w': 'e', 'r': 'f', 'd': 'g'})
    >>> cipher.encrypt('hello')
    'abccd'
    >>> cipher.encrypt('world')
    'edfcg'
    """

    def __init__(self, dictionary):
        """
        Initialize the dictionary cipher with a dictionary.
        If a key is not in the dictionary, the value is the key itself.
        We promise that any letter will only appear once as a value in the dictionary.
        """
        "*** YOUR CODE HERE ***"
        self.dictionary=dictionary

    def encrypt(self, message):
        """Encrypt the message using the dictionary cipher."""
        "*** YOUR CODE HERE ***"
        dic_encrypt=""
        for i in message:
            if i in self.dictionary:
                dic_encrypt+=self.dictionary[i]
            else:
                dic_encrypt+=i
        return dic_encrypt

class fencecipher(methods):
    """A class for fence cipher encryption method.
    >>> cipher = fencecipher(3)
    >>> cipher.encrypt('hello')
    'hleol'
    >>> cipher.encrypt('world')
    'wlodr'
    """

    def __init__(self, rails):
        """Initialize the fence cipher with a number of rails."""
        "*** YOUR CODE HERE ***"
        self.rails=rails
        
    def encrypt(self, message):
        """Encrypt the message using the fence cipher."""
        "*** YOUR CODE HERE ***"
        fen_encrypt=[[] for _ in range(self.rails)]
        for i in range(len(message)):
            fen_encrypt[i%self.rails].append(message[i])
        return "".join(["".join(rail) for rail in fen_encrypt])
    

class extensions:
    """The base class for encryption extensions."""

    def decorator(self, function, message):
        """Apply the function to the message."""
        pass

class multipleencryption(extensions):
    """A class for multiple encryption extension.
    >>> cipher = shiftcipher(3)
    >>> extension = multipleencryption(2)
    >>> extension.decorator(cipher.encrypt, 'hello')
    'nkrru'
    >>> extension.decorator(cipher.encrypt, 'world')
    'cuxrj'
    """

    def __init__(self, counts=1):
        """Initialize the multiple encryption extension with a number of times."""
        "*** YOUR CODE HERE ***"
        self.cnt=counts

    def decorator(self, function, message):
        """Apply the function to the message multiple times."""
        "*** YOUR CODE HERE ***"
        for i in range(self.cnt):
            message=function(message)
        return message

class splitencryption(extensions):
    """A class for split encryption extension.
    It extracts characters from positions that are multiples of `x` (excluding 0), 
    concatenates them, and appends them to the original string before applying the encryption method.
    >>> cipher = shiftcipher(3)
    >>> extension = splitencryption(2)
    >>> extension.decorator(cipher.encrypt, 'hello')
    'khoor'
    >>> extension.decorator(cipher.encrypt, 'world')
    'zroug'
    """

    def __init__(self, x):
        """Initialize the split encryption extension with a number x."""
        "*** YOUR CODE HERE ***"
        self.x=x

    def decorator(self, function, message):
        """Apply the function to the message after splitting the message."""
        "*** YOUR CODE HERE ***"
        split_mes, rest_mes=[],[]
        for i in range(len(message)):
            if i%self.x==0 and i:
                split_mes.append(message[i])
            else :
                rest_mes.append(message[i])    
        t=rest_mes+split_mes
        return function(t)


class encryption:
    """A class for encryption.
    >>> cipher = shiftcipher(3)
    >>> extension = multipleencryption(2)
    >>> encrypt = encryption(cipher, extension)
    >>> encrypt.encrypt('hello')
    'nkrru'
    >>> encrypt.encrypt('world')
    'cuxrj'
    """

    def __init__(self, method, extension):
        """Initialize the encryption with a method and an extension."""
        "*** YOUR CODE HERE ***"
        self.method=method
        self.extension=extension

    def encrypt(self, message):
        """Encrypt the message using the method and extension."""
        "*** YOUR CODE HERE ***"
        # 调用了很多class
        return self.extension.decorator(self.method.encrypt, message)


class Card:
    cardtype = 'Staff'

    def __init__(self, name, attack, defense):
        """
        Create a Card object with a name, attack,
        and defense.
        >>> staff_member = Card('staff', 400, 300)
        >>> staff_member.name
        'staff'
        >>> staff_member.attack
        400
        >>> staff_member.defense
        300
        >>> other_staff = Card('other', 300, 500)
        >>> other_staff.attack
        300
        >>> other_staff.defense
        500
        """
        "*** YOUR CODE HERE ***"
        self.name=name
        self.attack=attack
        self.defense=defense

    def power(self, other_card):
        """
        Calculate power as:
        (player card's attack) - (opponent card's defense) / 2
        where other_card is the opponent's card.
        >>> staff_member = Card('staff', 400, 300)
        >>> other_staff = Card('other', 300, 500)
        >>> staff_member.power(other_staff)
        150.0
        >>> other_staff.power(staff_member)
        150.0
        >>> third_card = Card('third', 200, 400)
        >>> staff_member.power(third_card)
        200.0
        >>> third_card.power(staff_member)
        50.0
        """
        "*** YOUR CODE HERE ***"
        return self.attack-other_card.defense/2

    def effect(self, other_card, player, opponent):
        """
        Cards have no default effect.
        """
        return

    def __repr__(self):
        """
        Returns a string which is a readable version of
        a card, in the form:
        <cardname>: <cardtype>, [<attack>, <defense>]
        """
        return '{}: {}, [{}, {}]'.format(self.name, self.cardtype, self.attack, self.defense)

    def copy(self):
        """
        Returns a copy of this card.
        """
        return Card(self.name, self.attack, self.defense)

class Player:
    def __init__(self, deck, name):
        """Initialize a Player object.
        A Player starts the game by drawing 5 cards from their deck. Each turn,
        a Player draws another card from the deck and chooses one to play.
        >>> test_card = Card('test', 100, 100)
        >>> test_deck = Deck([test_card.copy() for _ in range(6)])
        >>> test_player = Player(test_deck, 'tester')
        >>> len(test_deck.cards)
        1
        >>> len(test_player.hand)
        5
        """
        self.deck = deck
        self.name = name
        "*** YOUR CODE HERE ***"
        self.hand=[]
        for i in range(5):
            self.draw()

    def draw(self):
        """Draw a card from the player's deck and add it to their hand.
        >>> test_card = Card('test', 100, 100)
        >>> test_deck = Deck([test_card.copy() for _ in range(6)])
        >>> test_player = Player(test_deck, 'tester')
        >>> test_player.draw()
        >>> len(test_deck.cards)
        0
        >>> len(test_player.hand)
        6
        """
        assert not self.deck.is_empty(), 'Deck is empty!'
        "*** YOUR CODE HERE ***"
        self.hand.append(self.deck.draw())

    def play(self, card_index):
        """Remove and return a card from the player's hand at the given index.
        >>> from cards import *
        >>> test_player = Player(standard_deck, 'tester')
        >>> ta1, ta2 = TACard("ta_1", 300, 400), TACard("ta_2", 500, 600)
        >>> tutor1, tutor2 = TutorCard("t1", 200, 500), TutorCard("t2", 600, 400)
        >>> test_player.hand = [ta1, ta2, tutor1, tutor2]
        >>> test_player.play(0) is ta1
        True
        >>> test_player.play(2) is tutor2
        True
        >>> len(test_player.hand)
        2
        """
        "*** YOUR CODE HERE ***"
        card=self.hand[card_index]
        self.hand.pop(card_index)
        return card

    def display_hand(self):
        """
        Display the player's current hand to the user.
        """
        print('Your hand:')
        for card_index, displayed_card in zip(range(len(self.hand)),[str(card) for card in self.hand]):
            indent = ' '*(5 - len(str(card_index)))
            print(card_index, indent + displayed_card)

    def play_random(self):
        """
        Play a random card from hand.
        """
        return self.play(random.randrange(len(self.hand)))
    

class TutorCard(Card):
    cardtype = 'Tutor'

    def effect(self, other_card, player, opponent):
        """
        Discard the first 3 cards in the opponent's hand and have
        them draw the same number of cards from their deck.
        >>> from cards import *
        >>> player1, player2 = Player(player_deck, 'p1'), Player(opponent_deck, 'p2')
        >>> other_card = Card('other', 500, 500)
        >>> tutor_test = TutorCard('Tutor', 500, 500)
        >>> initial_deck_length = len(player2.deck.cards)
        >>> tutor_test.effect(other_card, player1, player2)
        p2 discarded and re-drew 3 cards!
        >>> len(player2.hand)
        5
        >>> len(player2.deck.cards) == initial_deck_length - 3
        True
        """
        "*** YOUR CODE HERE ***"
        # Uncomment the line below when you've finished implementing this method!
        for _ in range(3):
            opponent.hand.pop()
        for _ in range(3):
            opponent.draw()
        print('{} discarded and re-drew 3 cards!'.format(opponent.name))

    def copy(self):
        """
        Create a copy of this card.
        """
        return TutorCard(self.name, self.attack, self.defense)

class TACard(Card):
    cardtype = 'TA'

    def effect(self, other_card, player, opponent):
        """
        Swap the attack and defense of an opponent's card.
        >>> from cards import *
        >>> player1, player2 = Player(player_deck, 'p1'), Player(opponent_deck, 'p2')
        >>> other_card = Card('other', 300, 600)
        >>> ta_test = TACard('TA', 500, 500)
        >>> ta_test.effect(other_card, player1, player2)
        >>> other_card.attack
        600
        >>> other_card.defense
        300
        """
        "*** YOUR CODE HERE ***"
        op_defense=other_card.defense
        op_attack=other_card.attack
        other_card.defense=op_attack
        other_card.attack=op_defense
        

    def copy(self):
        """
        Create a copy of this card.
        """
        return TACard(self.name, self.attack, self.defense)

class ProfessorCard(Card):
    cardtype = 'Professor'

    def effect(self, other_card, player, opponent):
        """
        Adds the attack and defense of the opponent's card to
        all cards in the player's deck, then removes all cards
        in the opponent's deck that share an attack or defense
        stat with the opponent's card.
        >>> test_card = Card('card', 300, 300)
        >>> professor_test = ProfessorCard('Professor', 500, 500)
        >>> opponent_card = test_card.copy()
        >>> test_deck = Deck([test_card.copy() for _ in range(8)])
        >>> player1, player2 = Player(test_deck.copy(), 'p1'), Player(test_deck.copy(), 'p2')
        >>> professor_test.effect(opponent_card, player1, player2)
        3 cards were discarded from p2's deck!
        >>> [(card.attack, card.defense) for card in player1.deck.cards]
        [(600, 600), (600, 600), (600, 600)]
        >>> len(player2.deck.cards)
        0
        """
        orig_opponent_deck_length = len(opponent.deck.cards)
        "*** YOUR CODE HERE ***"
        for my_card in player.deck.cards:
            my_card.defense+=other_card.defense
            my_card.attack+=other_card.attack

        # 删除牌时使用循环会打乱顺序！！,复制一个副本，再清空原列表，符合条件的再加入
        list_copy=opponent.deck.cards[:]
        opponent.deck.cards=[]
        for op_card in list_copy:
            if op_card.defense != other_card.defense or op_card.attack!=other_card.attack :
                opponent.deck.cards.append(op_card)
            
        discarded = orig_opponent_deck_length - len(opponent.deck.cards)
        if discarded:
            # Uncomment the line below when you've finished implementing this method!
            print('{} cards were discarded from {}\'s deck!'.format(discarded, opponent.name))
            return

    def copy(self):
        return ProfessorCard(self.name, self.attack, self.defense)


##########################
# Just for fun Questions #
##########################


class dmethods:
    """The base class for decryption methods."""

    def decrypt(self, message):
        """Decrypt the message."""
        pass

class shiftdecipher(dmethods):
    """A class for shift cipher decryption method.
    >>> cipher = shiftdecipher(3)
    >>> cipher.decrypt('khoor')
    'hello'
    >>> cipher.decrypt('zruog')
    'world'
    """

    def __init__(self, shift):
        """
        Initialize the shift cipher with a shift.
        If shift is greater than 26, shift = shift % 26.
        """
        "*** YOUR CODE HERE ***"

    def decrypt(self, message):
        """Decrypt the message by shifting each character by the shift."""
        "*** YOUR CODE HERE ***"

class dictionarydecipher(dmethods):
    """A class for dictionary cipher decryption method.
    >>> cipher = dictionarydecipher({'h': 'a', 'e': 'b', 'l': 'c', 'o': 'd', 'w': 'e', 'r': 'f', 'd': 'g'})
    >>> cipher.decrypt('abccd')
    'hello'
    >>> cipher.decrypt('edfcg')
    'world'
    """

    def __init__(self, dictionary):
        """
        Initialize the dictionary cipher with a dictionary.
        If a key is not in the dictionary, the value is the key itself.
        We promise that any letter will only appear once as a value in the dictionary.
        """
        "*** YOUR CODE HERE ***"

    def decrypt(self, message):
        """Decrypt the message using the dictionary cipher."""
        "*** YOUR CODE HERE ***"

class fencedecipher(dmethods):
    """A class for fence cipher decryption method.
    >>> cipher = fencedecipher(3)
    >>> cipher.decrypt('hleol')
    'hello'
    >>> cipher.decrypt('wlodr')
    'world'
    """

    def __init__(self, rails):
        """Initialize the fence cipher with a number of rails."""
        "*** YOUR CODE HERE ***"

    def decrypt(self, message):
        """Decrypt the message using the fence cipher."""
        "*** YOUR CODE HERE ***"

class dextensions:
    """The base class for decryption extensions."""

    def decorator(self, function, message):
        """Apply the function to the message."""
        pass

class multipledecryption(dextensions):
    """A class for multiple decryption extension.
    >>> cipher = shiftdecipher(3)
    >>> extension = multipledecryption(2)
    >>> extension.decorator(cipher.decrypt, 'nkrru')
    'hello'
    >>> extension.decorator(cipher.decrypt, 'cuxrj')
    'world'
    """

    def __init__(self, counts=1):
        """Initialize the multiple decryption extension with a number of times."""
        "*** YOUR CODE HERE ***"

    def decorator(self, function, message):
        """Apply the function to the message multiple times."""
        "*** YOUR CODE HERE ***"

class splitdecryption(dextensions):
    """A class for split decryption extension.
    It extracts characters from positions that are multiples of `x` (excluding 0), 
    concatenates them, and appends them to the original string before applying the decryption method.
    >>> cipher = shiftdecipher(3)
    >>> extension = splitdecryption(2)
    >>> extension.decorator(cipher.decrypt, 'khoor')
    'hello'
    >>> extension.decorator(cipher.decrypt, 'zroug')
    'world'
    """

    def __init__(self, x):
        """Initialize the split decryption extension with a number x."""
        "*** YOUR CODE HERE ***"

    def decorator(self, function, message):
        """Apply the function to the message after splitting the message."""
        "*** YOUR CODE HERE ***"

class decryption:
    """A class for decryption.
    >>> cipher = shiftcipher(3)
    >>> extension = multipleencryption(2)
    >>> encrypt = encryption(cipher, extension)
    >>> decrypt = decryption(encrypt)
    >>> decrypt.decrypt('nkrru')
    'hello'
    >>> decrypt.decrypt('cuxrj')
    'world'
    """

    def __init__(self, encryption_instance):
        """Initialize the decryption with an encryption method."""
        "*** YOUR CODE HERE ***"

    def decrypt(self, message):
        """Decrypt the message using the method and extension."""
        "*** YOUR CODE HERE ***"


class Fib:
    """A Fibonacci number.

    >>> start = Fib()
    >>> start.value
    0
    >>> start.next().value
    1
    >>> start.next().next().value
    1
    >>> start.next().next().next().value
    2
    >>> start.next().next().next().next().value
    3
    >>> start.next().next().next().next().next().value
    5
    >>> start.next().next().next().next().next().next().value
    8
    >>> start.value # Ensure start isn't changed
    0
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** YOUR CODE HERE ***"


########################################
# Do not edit anything below this line #
########################################

class Deck:
    def __init__(self, cards):
        """
        With a list of cards as input, create a deck.
        This deck should keep track of the cards it contains, and
        we should be able to draw from the deck, taking a random
        card out of it.
        """
        self.cards = cards

    def draw(self):
        """
        Draw a random card and remove it from the deck.
        """
        assert self.cards, 'The deck is empty!'
        rand_index = random.randrange(len(self.cards))
        return self.cards.pop(rand_index)

    def is_empty(self):
        return len(self.cards) == 0

    def copy(self):
        """
        Create a copy of this deck.
        """
        return Deck([card.copy() for card in self.cards])

class Game:

    win_score = 8

    def __init__(self, player1, player2):
        """
        Initialize a game of <REPLACE NAME>.
        """
        self.player1, self.player2 = player1, player2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self, p1_card, p2_card):
        """
        After each player picks a card, play them against
        each other.
        """
        p1_card.effect(p2_card, self.player1, self.player2)
        p2_card.effect(p1_card, self.player2, self.player1)
        p1_power = p1_card.power(p2_card)
        p2_power = p2_card.power(p1_card)
        if p1_power > p2_power:
            # Player 1 wins the round.
            self.p1_score += 1
            result = 'won'
        elif p2_power > p1_power:
            # Player 2 wins the round.
            self.p2_score += 1
            result = 'lost'
        else:
            # This round is a draw.
            result = 'tied'
        # Display results to user.
        print('You {} this round!'.format(result))
        print('{}\'s card: {}; Power: {}'.format(self.player1.name, p1_card, p1_power))
        print('Opponent\'s card: {}; Power: {}'.format(p2_card, p2_power))


    def game_won(self):
        """
        Check if the game is won and, if so,
        which player won.
        """
        if self.p1_score < self.win_score and self.p2_score < self.win_score:
            return 0
        return 1 if self.p1_score > self.p2_score else 2

    def display_scores(self):
        """
        Display players' scores to the user.
        """
        print('{}\'s score: {}'.format(self.player1.name, self.p1_score))
        print('Opponent\'s score: {}'.format(self.p2_score))
