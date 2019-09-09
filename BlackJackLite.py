import random


class Card():

    def __init__(self, suite, name, rank):
        self.suite = suite
        self.name = name
        self.rank = rank


class Deck():

    def __init__(self):
        self.cards = []

    def addcard(self, card):
        self.cards.append(card)

    def delete_card(self, card):
        self.cards.remove(card)


class Dealer():

    def __init__(self, deck, bank):
        self.deck_on_hand = deck
        self.bank = bank

    def change_bank(self, m_operator, value):
        if m_operator == '+':
            self.bank += value
        elif m_operator == '-':
            self.bank -= value

    def collected_points(self):
        player_cards = self.deck_on_hand.cards
        points = 0
        for each in player_cards:
            points += each.rank

        return (points, points - 10)


class Player(Dealer):

    def __init__(self, deck, bank):
        Dealer.__init__(self, deck, bank)
        self.first_turn = True


def put_cards_in_deck():
    game_deck.cards.clear()
    for card_t in card_suits:
        for card_v in card_values.items():
            c = Card(card_t, card_v[0], card_v[1])
            game_deck.addcard(c)


def get_card(player_cards, show=True):
    random_card = random.choice(game_deck.cards)
    player_cards.append(random_card)
    game_deck.delete_card(random_card)

    if show:
        show_cards(player_cards)


def ask_user(message, answers):
    answers_up = [a.upper() for a in answers]
    while True:
        a = input(message).upper()
        if a not in answers_up:
            continue
        else:
            break

    return a


def show_cards(cards):
    for each in cards:
        print(each.name + ' <=> ' + each.suite)


def user_turn():

    next_card = False
    play_again = False
    dealer_turn = False

    player_points = _player.collected_points()
    player_cards = _player.deck_on_hand.cards

    if player_points[0] == 21 or player_points[1] == 21:
        pot_win = pot_size * 0.01
        _dealer.change_bank('-', pot_win)
        _player.change_bank('+', pot_win)
        print('P:{}$ D:{}$'.format(_player.bank, _dealer.bank))

        print("You've won the Game and earn {}$".format(_player.bank))
        answer = ask_user('Would you like to paly again? ', ('y', 'n'))

        if answer == 'Y':
            play_again = True

    elif player_points[0] > 21 or player_points[1] > 21:
        pot_win = pot_size * 0.01
        _dealer.change_bank('+', pot_win)
        _player.change_bank('-', pot_win)
        print('P:{}$ D:{}$'.format(_player.bank, _dealer.bank))

        print("You've lost the Game!")
        answer = ask_user('Would you like to paly again? ', ('y', 'n'))

        if answer == 'Y':
            play_again = True

    elif player_points[0] > 21 and player_points[1] < 21:
        answer = ask_user('Would you like to receive a card (your Ace now going to have a rank equal 1)? ', ('y', 'n'))

        if answer == 'Y':
            next_card = True

    else:
        answer = ask_user('Would you like to receive a card? ', ('y', 'n'))

        if answer == 'Y':
            next_card = True
        else:
            dealer_turn = True

    if next_card:
        get_card(player_cards)

    return {'next_card': next_card,
            'dealer_turn': dealer_turn,
            'play_again': play_again}


def dealer_turn():

    next_card = False
    play_again = False
    dealer_turn = False

    dealer_cards = _dealer.deck_on_hand.cards

    while True:
        get_card(dealer_cards, False)
        dealer_points = _dealer.collected_points()

        if dealer_points[0] == 21 or dealer_points[1] == 21:
            pot_win = pot_size * 0.01
            _dealer.change_bank('+', pot_win)
            _player.change_bank('-', pot_win)
            print('P:{}$ D:{}$'.format(_player.bank, _dealer.bank))

            print("Dealer has won the Game and earn {}$".format(_dealer.bank))
            answer = ask_user('Would you like to paly again? ', ('y', 'n'))

            if answer == 'Y':
                play_again = True

            break

        elif dealer_points[0] > 21 or dealer_points[1] > 21:
            pot_win = pot_size * 0.01
            _dealer.change_bank('-', pot_win)
            _player.change_bank('+', pot_win)
            print('P:{}$ D:{}$'.format(_player.bank, _dealer.bank))

            print("Dealer has lost the Game and earn {}$".format(_dealer.bank))
            answer = ask_user('Would you like to paly again? ', ('y', 'n'))

            if answer == 'Y':
                play_again = True

            break

    return {'next_card': next_card,
            'dealer_turn': dealer_turn,
            'play_again': play_again}


def prepare_players():
    _player.deck_on_hand.cards.clear()
    _dealer.deck_on_hand.cards.clear()


def gameplay():

    # User goes first
    result = user_turn()
    while True:

        # result = user_turn()

        if result['dealer_turn']:
            result = dealer_turn()
        elif result['next_card']:
            result = user_turn()
        elif result['play_again']:
            prepare_players()
            put_cards_in_deck()
            result = user_turn()
        else:
            break


# ### Main Program ### #

card_suits = ('clubs', 'diamonds', 'hearts', 'spades')
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
               '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

pot_size = 100

game_deck = Deck()
user_deck = Deck()
dealer_deck = Deck()

put_cards_in_deck()

player_name = input('Type your name here ::: ')
print('Hi', player_name)
player_cash = int(input('How much money do you have? :) ::: '))
print('Ok, let\'s go')

_player = Player(user_deck, player_cash)
_dealer = Dealer(dealer_deck, pot_size)

gameplay()
