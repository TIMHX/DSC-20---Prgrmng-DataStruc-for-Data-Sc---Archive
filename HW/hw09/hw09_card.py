"""
DSC 20 HW 09 CARD
NAME: XING HONG
PID: A15867895
"""

import numpy as np

two = 2


## Question 4.1 ##
class card:
    """
    This class represents a single card.

    >>> c1 = card(4, "Clubs")
    >>> print(c1)
    4 of Clubs
    >>> c2 = card(3, "Hearts")
    >>> print(c2)
    3 of Hearts
    >>> c1 < c2
    True
    >>> c1 > c2
    False
    >>> c1 == c2
    False

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    def __init__(self, rank, suit):
        """Write your docstring here.
        >>> c3 = card(4, "Clubs")
        >>> c4 = card(5, "Spades")
        >>> c5 = card("J", "Diamonds")
        >>> c3.rank
        4
        >>> c4.rank
        5
        >>> c5.rank_i
        10
        >>> c5.suit_i
        1
        """
        # YOUR CODE HERE
        self.rank = rank
        self.suit = suit
        self.rank_i = card.rank_names.index(self.rank)
        self.suit_i = card.suit_names.index(self.suit)

    def __repr__(self):
        """Write your docstring here.
        >>> c3 = card(4, "Clubs")
        >>> c4 = card(5, "Spades")
        >>> c5 = card("J", "Diamonds")
        >>> c3
        4 of Clubs
        >>> c4
        5 of Spades
        >>> c5
        J of Diamonds
        """
        # YOUR CODE HERE
        return '{0} of {1}'.format(self.rank, self.suit)

    def __str__(self):
        """Write your docstring here.
        >>> c3 = card(4, "Clubs")
        >>> c4 = card(5, "Spades")
        >>> c5 = card("J", "Diamonds")
        >>> print(c3)
        4 of Clubs
        >>> print(c4)
        5 of Spades
        >>> print(c5)
        J of Diamonds
        """
        # YOUR CODE HERE
        return '{0} of {1}'.format(self.rank, self.suit)

    def __eq__(self, other):
        """Write your docstring here.
        >>> c1 = card(4, "Clubs")
        >>> c3 = card(4, "Clubs")
        >>> c4 = card(5, "Spades")
        >>> c5 = card("J", "Diamonds")
        >>> c3 == c4
        False
        >>> c3 == c1
        True
        >>> c4 == c5
        False
        """
        # YOUR CODE HERE
        return self.suit_i == other.suit_i and self.rank_i == other.rank_i

    def __ne__(self, other):
        """Write your docstring here.
        >>> c1 = card(4, "Clubs")
        >>> c3 = card(4, "Clubs")
        >>> c4 = card(5, "Spades")
        >>> c5 = card("J", "Diamonds")
        >>> c3 != c4
        True
        >>> c3 != c1
        False
        >>> c4 != c5
        True
        """
        # YOUR CODE HERE
        return self.suit_i != other.suit_i or self.rank_i != other.rank_i

    def __lt__(self, other):
        """Write your docstring here.
        >>> c3 = card("Q", "Hearts")
        >>> c4 = card(9, "Spades")
        >>> c5 = card("J", "Diamonds")
        >>> c3 < c5
        False
        >>> c3 < c4
        True
        >>> c4 < c5
        False
        """
        # YOUR CODE HERE
        if self.suit_i < other.suit_i:
            return True
        elif self.suit_i > other.suit_i:
            return False
        else:
            if self.rank_i < other.rank_i:
                return True
            else:
                return False

    def __gt__(self, other):
        """Write your docstring here.
        >>> c1 = card(4, "Clubs")
        >>> c3 = card(4, "Clubs")
        >>> c4 = card(5, "Spades")
        >>> c5 = card("J", "Diamonds")
        >>> c3 > c1
        False
        >>> c3 > c4
        False
        >>> c4 > c5
        True
        """
        # YOUR CODE HERE
        if self.suit_i > other.suit_i:
            return True
        elif self.suit_i < other.suit_i:
            return False
        else:
            if self.rank_i > other.rank_i:
                return True
            else:
                return False

    def __le__(self, other):
        """Write your docstring here.
        >>> c1 = card(4, "Clubs")
        >>> c3 = card(4, "Clubs")
        >>> c4 = card(5, "Spades")
        >>> c5 = card("J", "Diamonds")
        >>> c3 <= c1
        True
        >>> c3 <= c4
        True
        >>> c4 <= c5
        False
        """

        # YOUR CODE HERE
        def __eq__(self, other):
            return self.suit == other.suit and self.rank == other.rank

        def __lt__(self, other):
            if self.suit_i < other.suit_i:
                return True
            elif self.suit_i > other.suit_i:
                return False
            else:
                if self.rank_i < other.rank_i:
                    return True
                else:
                    return False

        return __eq__(self, other) or __lt__(self, other)

    def __ge__(self, other):
        """Write your docstring here.
        >>> c1 = card(4, "Clubs")
        >>> c3 = card(4, "Clubs")
        >>> c4 = card(5, "Spades")
        >>> c5 = card("J", "Diamonds")
        >>> c3 >= c1
        True
        >>> c4 >= c3
        True
        >>> c5 >= c4
        False
        """

        # YOUR CODE HERE
        def __eq__(self, other):
            return self.suit == other.suit and self.rank == other.rank

        def __gt__(self, other):
            if self.suit_i > other.suit_i:
                return True
            elif self.suit_i < other.suit_i:
                return False
            else:
                if self.rank_i > other.rank_i:
                    return True
                else:
                    return False

        return __eq__(self, other) or __gt__(self, other)

    ## Question 4.2 ##


class deck:
    """
    >>> cards = deck()
    >>> len(cards.deck)
    52
    >>> cards = deck()
    >>> len(cards.dealt_cards)
    0
    >>> cards = deck()
    >>> print(cards)
    In Deck:
    A of Clubs
    2 of Clubs
    3 of Clubs
    4 of Clubs
    5 of Clubs
    6 of Clubs
    7 of Clubs
    8 of Clubs
    9 of Clubs
    10 of Clubs
    J of Clubs
    Q of Clubs
    K of Clubs
    A of Diamonds
    2 of Diamonds
    3 of Diamonds
    4 of Diamonds
    5 of Diamonds
    6 of Diamonds
    7 of Diamonds
    8 of Diamonds
    9 of Diamonds
    10 of Diamonds
    J of Diamonds
    Q of Diamonds
    K of Diamonds
    A of Hearts
    2 of Hearts
    3 of Hearts
    4 of Hearts
    5 of Hearts
    6 of Hearts
    7 of Hearts
    8 of Hearts
    9 of Hearts
    10 of Hearts
    J of Hearts
    Q of Hearts
    K of Hearts
    A of Spades
    2 of Spades
    3 of Spades
    4 of Spades
    5 of Spades
    6 of Spades
    7 of Spades
    8 of Spades
    9 of Spades
    10 of Spades
    J of Spades
    Q of Spades
    K of Spades
    Dealt Out:
    >>> deck_to_shuffle = deck()
    >>> np.random.seed(5)
    >>> deck_to_shuffle.shuffle()
    >>> print(deck_to_shuffle.deck[:5])
    [9 of Hearts, 4 of Hearts, 7 of Spades, 7 of Diamonds, 6 of Hearts]
    >>> deck_to_deal = deck()
    >>> hand = deck_to_deal.deal_cards(5)
    >>> np.random.seed(5)
    >>> deck_to_deal.shuffle()
    >>> deck_to_deal.deck[:5]
    [A of Spades, 9 of Hearts, Q of Spades, Q of Diamonds, J of Hearts]
    >>> cards = deck()
    >>> cards.deal_cards(5)
    [A of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs]
    >>> cards = deck()
    >>> hand = cards.deal_cards(5)
    >>> cards.deal_cards(5)
    [6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs]
    >>> cards = deck()
    >>> hand = cards.deal_cards(5)
    >>> print(cards)
    In Deck:
    6 of Clubs
    7 of Clubs
    8 of Clubs
    9 of Clubs
    10 of Clubs
    J of Clubs
    Q of Clubs
    K of Clubs
    A of Diamonds
    2 of Diamonds
    3 of Diamonds
    4 of Diamonds
    5 of Diamonds
    6 of Diamonds
    7 of Diamonds
    8 of Diamonds
    9 of Diamonds
    10 of Diamonds
    J of Diamonds
    Q of Diamonds
    K of Diamonds
    A of Hearts
    2 of Hearts
    3 of Hearts
    4 of Hearts
    5 of Hearts
    6 of Hearts
    7 of Hearts
    8 of Hearts
    9 of Hearts
    10 of Hearts
    J of Hearts
    Q of Hearts
    K of Hearts
    A of Spades
    2 of Spades
    3 of Spades
    4 of Spades
    5 of Spades
    6 of Spades
    7 of Spades
    8 of Spades
    9 of Spades
    10 of Spades
    J of Spades
    Q of Spades
    K of Spades
    Dealt Out:
    A of Clubs
    2 of Clubs
    3 of Clubs
    4 of Clubs
    5 of Clubs

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> cards.dealt_cards
    [A of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs]
    >>> np.random.seed(5)
    >>> cards.shuffle()
    >>> cards.dealt_cards
    []
    >>> cards.deck[:5]
    [A of Spades, 9 of Hearts, Q of Spades, Q of Diamonds, J of Hearts]
    """

    def __init__(self):
        """Initializes the deck of cards."""
        # YOUR CODE HERE
        self.deck = []
        self.dealt_cards = []
        for i in card.suit_names:
            for j in card.rank_names:
                self.deck.append(card(j, i))

    def shuffle(self):
        """This method shuffles the deck using np.random.choice."""
        # YOUR CODE HERE
        self.deck.extend(self.dealt_cards)
        self.deck = list(np.random.choice(self.deck, size=len(self.deck), replace=False))
        self.dealt_cards = []

    def deal_cards(self, n):
        """
        This method deals out n cards and sends them all to the dealt cards list.
        It also returns the list of the cards.
        """
        # YOUR CODE HERE
        assert n <= len(self.deck)
        deal_c = self.deck[:n]
        self.dealt_cards += deal_c
        self.deck = self.deck[n:]
        return deal_c

    def __repr__(self):
        """Write your docstring here."""
        # YOUR CODE HERE

    def __str__(self):
        """Write your docstring here."""
        # YOUR CODE HERE
        out = 'In Deck:'
        for i in self.deck:
            out += ('\n' + i.__str__())
        out += '\nDealt Out:'
        for j in self.dealt_cards:
            out += ('\n' + j.__str__())
        return out


## Question 4.3 ##
class WarGame:
    """
    >>> np.random.seed(5)
    >>> game = WarGame()
    >>> game.play_rounds(5)
    Player 1's card:  9 of Hearts
    Player 2's card:  4 of Hearts
    Player 1 Won the Round
    Player 1's card:  7 of Spades
    Player 2's card:  7 of Diamonds
    Player 1 Won the Round
    Player 1's card:  6 of Hearts
    Player 2's card:  9 of Diamonds
    Player 1 Won the Round
    Player 1's card:  7 of Clubs
    Player 2's card:  8 of Hearts
    Player 2 Won the Round
    Player 1's card:  3 of Clubs
    Player 2's card:  4 of Clubs
    Player 2 Won the Round
    The score is now 3 to 2
    >>> game.declare_winner()
    The score is 3 to 2
    Player 1 Wins!

    >>> np.random.seed(15)
    >>> game = WarGame()
    >>> game.play_rounds(4)
    Player 1's card:  8 of Hearts
    Player 2's card:  4 of Diamonds
    Player 1 Won the Round
    Player 1's card:  9 of Hearts
    Player 2's card:  J of Spades
    Player 2 Won the Round
    Player 1's card:  Q of Hearts
    Player 2's card:  9 of Spades
    Player 2 Won the Round
    Player 1's card:  A of Spades
    Player 2's card:  K of Hearts
    Player 1 Won the Round
    The score is now 2 to 2
    >>> game.declare_winner()
    The score is 2 to 2
    It's a Tie!

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> np.random.seed(10)
    >>> game = WarGame()
    >>> game.play_rounds(4)
    Player 1's card:  2 of Hearts
    Player 2's card:  K of Hearts
    Player 2 Won the Round
    Player 1's card:  8 of Spades
    Player 2's card:  J of Diamonds
    Player 1 Won the Round
    Player 1's card:  7 of Hearts
    Player 2's card:  8 of Diamonds
    Player 1 Won the Round
    Player 1's card:  4 of Clubs
    Player 2's card:  6 of Hearts
    Player 2 Won the Round
    The score is now 2 to 2
    >>> game.declare_winner()
    The score is 2 to 2
    It's a Tie!
    >>> np.random.seed(6)
    >>> game = WarGame()
    >>> game.play_rounds(3)
    Player 1's card:  K of Spades
    Player 2's card:  3 of Spades
    Player 1 Won the Round
    Player 1's card:  A of Spades
    Player 2's card:  J of Diamonds
    Player 1 Won the Round
    Player 1's card:  8 of Clubs
    Player 2's card:  A of Clubs
    Player 1 Won the Round
    The score is now 3 to 0
    >>> game.declare_winner()
    The score is 3 to 0
    Player 1 Wins!
    >>> np.random.seed(9)
    >>> game = WarGame()
    >>> game.play_rounds(3)
    Player 1's card:  8 of Clubs
    Player 2's card:  7 of Clubs
    Player 1 Won the Round
    Player 1's card:  3 of Clubs
    Player 2's card:  K of Diamonds
    Player 2 Won the Round
    Player 1's card:  J of Diamonds
    Player 2's card:  2 of Diamonds
    Player 1 Won the Round
    The score is now 2 to 1
    >>> game.declare_winner()
    The score is 2 to 1
    Player 1 Wins!
    """

    def __init__(self):
        """Write your docstring here."""
        # YOUR CODE HERE
        self.cards = deck()
        self.cards.shuffle()
        self.p1_score = 0
        self.p2_score = 0

    def play_rounds(self, n=1):
        """Write your docstring here."""
        # YOUR CODE HERE
        if n * two > len(self.cards.deck):
            n = len(self.cards.deck) / two
        for i in range(n):
            if len(self.cards.deck) == 0:
                break
            a = self.cards.deal_cards(1)[0]
            b = self.cards.deal_cards(1)[0]
            print("Player 1's card:  {}".format(a))
            print("Player 2's card:  {}".format(b))
            if a > b:
                print('Player 1 Won the Round')
                self.p1_score += 1
            elif a < b:
                print('Player 2 Won the Round')
                self.p2_score += 1
        print('The score is now {0} to {1}'.format(self.p1_score, self.p2_score))

    def declare_winner(self):
        """Write your docstring here."""
        # YOUR CODE HERE
        print('The score is {0} to {1}'.format(self.p1_score, self.p2_score))
        if self.p1_score > self.p2_score:
            print('Player 1 Wins!')
        elif self.p1_score < self.p2_score:
            print('Player 2 Wins!')
        else:
            print("It's a Tie!")
