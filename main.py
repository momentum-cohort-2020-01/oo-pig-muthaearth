import random

player_Score = 0


class GAME:

    def __init__(self):

        self.players = Player()
        self.human = HUMPLAYER()
        self.computer = CPUPLAYER()
        self.die = Die()
        self.scorecard = Scorecard()


class RollOne(Exception):
    pass


class Die:
    """Single die for Pig Game"""

    def __init__(self):
        # generate random integer btwn 1 and 6#
        self.value = random.randint(1, 6)

    def roll(self):
        #return die int btwn 1-6, and raise RollOne exception if value equal to 1#

        self.value = random.randint(1, 6)
        if self.value == 1:
            raise RollOne
        return self.value

    def __str__(self):
        return "You rolled " + str(self.value) + "."

        # need help writing this line opening with name of player"
        # return("{}.format(
        #     self.players[self.active_player].name ", + you rolled a " +
        #     str(self.value) + "."


class Scorecard:

    def __init__(self):  # scorecard initialized to zero#
        self.value = 0

    def reset(self):
        self.value = 0  # scorecard reset to zero for each new game#

    def add_dice_value(self, dice_value):
        # player's throw and current score stored here#
        self.value += dice_value


class Player(object):
    # initialize name and score for human and computer player types#

    def __init__(self, name=None):
        self.name = name
        self.score = 0

    def add_score(self, player_score):  # add player score to total score#
        self.score += player_score

    def __str__(self):  # return player name and current score#

        return str(self.name) + ": " + str(self.score)


class CPUPLAYER (Player):
    cpu_names = ['Hal', 'HAL', 'HAL9000']

    def __init__(self, number):
        # assigns name to computer player from list#

        if number < len(self.cpu_names):
            name = self.cpu_names[number]
        else:
            name = 'Cpu{}'.format(number)

        # returns inherited cpu_names to computer player#
        super(CPUPLAYER, self).__init__(name)

    def keep_rolling(self, scorecard):

        # randomly determines if computer player will roll or hold#
        while scorecard.value < (10 + random.randint(1, 35)):
            print("${self.cpu.name} will roll again.")
            # print("  CPU will roll again.")#
            return True
        print("${self.cpu.name } will hold.")
        return False


class HUMPLAYER(Player):
    hum_names = ['Dave', 'Frank']

    def __init__(self, number):
        # assigns name to human player from list#

        if number < len(self.hum_names):
            name = self.hum_names[number]
        else:
            name = 'Hum{}'.format(number)

        # returns inherited hum_names to human player#
        super(HUMPLAYER, self).__init__(name)

    def __init__(self, name):
        super(HUMPLAYER, self).__init__(name)

    def keep_rolling(self, scorecard):
        # Asks human player of intent to roll or hold#

        human_decision = input_number(
            "${self.cpu.name},   1 - Roll again, 0 - Hold? ", 0, 1)

        # will roll if human enters 1, otherwise will hold#
        if human_decision == 1:
            return True
        else:
            return False


class Referee:
    def __init__(self, humans=1, computers=1):
        # Initializes game to 1 human player and 1 computer player#

        self.players = []  # assign human name and computer name to this list of players#
        # loops through potential human player names and adds to players#
        for i in range(humans):
            self.players.append(HUMPLAYER(i))
        return human

        # loops through potential computer player names and adds to players#
        for i in range(computers):
            self.players.append(CPUPLAYER(i))
        return computer

        # stores value of player count to nbr_of_players#
        self.nbr_of_players = len(self.players)

        self.die = Die()
        self.scorecard = Scorecard()


@staticmethod  # used to format welcome message#
def welcome():

    print("*" * 70)  # prints 70 inline asterisks#
    print(("Hello,  '{}'(self.human.name) and '{}'self.cpu.name").center(70))
    print("Welcome to Pig Dice!" .center(70))
    print("*" * 70)  # prints 70 inline asterisks#
    print("The objective is to be first in scoring 100 points." .center(70))
    print("On each turn you will roll a single die." .center(70))
    print("The die value will be recorded on a scoreboard." .center(70))
    print("(If the die is 1, the active player earns no points," .center(70))
    print("and the turn goes to the opposing player.)" .center(70))
    print("A human player may opt to either roll again," .center(70))
    print("or hold. If the human player holds, those points" .center(70))
    print("will be added to your total on the scoreboard." .center(70))
    print(" Good luck!".center(70, "*"))
    print(" And, playa, don't even think about disconnecting the computer! " .center(70, "*"))
    print()
    print("I will now throw the die to decide who starts" .center(70, " "))
    print()

    def whooz_on_first(self):
        # Randomly choose starting player, and print name#

        self.active_player = random.randint(
            1, self.nbr_of_players) % self.nbr_of_players

        print('{} starts'.format(self.players[self.active_player].name))

    def next_player(self):  # change active player to next player#"
        self.active_player = (self.active_player + 1) % self.nbr_of_players

    def previous_player(self):  # change active player to previous player#"
        self.active_player = (self.active_player - 1) % self.nbr_of_players

    def get_all_scores(self):  # Returns a join of all player scores#
        return ', '.join(str(player) for player in self.players)

    def play_game(self):
        # Plays an entire game#

        self.welcome()
        self.whooz_on_first()
        self.players()

        while all(player.score < 100 for player in self.players):
            # If no winner, print current player scores and print player names#
            print('\nCurrent score --> {}'.format(self.get_all_scores()))
            print(
                '\n*** {} to play ***'.format(self.players[self.active_player].name))
            self.scorecard.reset()

            while self.keep_rolling():
                pass
            # keep updating scorecard for as long as game is rolling#
            self.players[self.active_player].add_score(self.scorecard.value)
            self.next_player()

            self.previous_player()  # The previous player has won...#
            print(' {} has won '.format(
                self.players[self.active_player].name).center(70, '*'))

        def keep_rolling(self):
            # Adds rolled dice to scorecard. Returns if human/cpu wants to continue#
            # If either player rolls 1, scorecard value is reset, and turn ends#

            try:
                dice_value = self.die.roll()
                self.scorecard.add_dice_value(dice_value)
                print('Last roll: {}, your score is now: {}'.format(
                    dice_value, self.scorecard.value))

            # Check if human (by asking) or cpu(by calculating) will keep rolling
                return self.players[self.active_player].keep_rolling(self.scorecard)

            except RollOne:
                print(
                    'I’m sorry, {}.format(self.players[self.current_player].name). You rolled one. Your opponent rolls now')
                self.box.reset()
                return False


player_Score = 0


class GAME:

    def __init__(self):

        self.players = Player()
        self.human = HUMPLAYER()
        self.computer = CPUPLAYER()
        self.die = Die()
        self.scorecard = Scorecard()


class RollOne(Exception):
    pass


class Die:
    """Single die for Pig Game"""

    def __init__(self):
        # generate random integer btwn 1 and 6#
        self.value = random.randint(1, 6)

    def roll(self):
        #return die int btwn 1-6, and raise RollOne exception if value equal to 1#

        self.value = random.randint(1, 6)
        if self.value == 1:
            raise RollOne
        return self.value

    def __str__(self):
        return "You rolled " + str(self.value) + "."

        # need help writing this line opening with name of player"
        # return("{}.format(
        #     self.players[self.active_player].name ", + you rolled a " +
        #     str(self.value) + "."


class Scorecard:

    def __init__(self):  # scorecard initialized to zero#
        self.value = 0

    def reset(self):
        self.value = 0  # scorecard reset to zero for each new game#

    def add_dice_value(self, dice_value):
        # player's throw and current score stored here#
        self.value += dice_value


class Player(object):
    # initialize name and score for human and computer player types#

    def __init__(self, name=None):
        self.name = name
        self.score = 0

    def add_score(self, player_score):  # add player score to total score#
        self.score += player_score

    def __str__(self):  # return player name and current score#

        return str(self.name) + ": " + str(self.score)


class CPUPLAYER (Player):
    cpu_names = ['Hal', 'HAL', 'HAL9000']

    def __init__(self, number):
        # assigns name to computer player from list#

        if number < len(self.cpu_names):
            name = self.cpu_names[number]
        else:
            name = 'Cpu{}'.format(number)

        # returns inherited cpu_names to computer player#
        super(CPUPLAYER, self).__init__(name)

    def keep_rolling(self, scorecard):

        # randomly determines if computer player will roll or hold#
        while scorecard.value < (10 + random.randint(1, 35)):
            print("${self.cpu.name} will roll again.")
            # print("  CPU will roll again.")#
            return True
        print("${self.cpu.name } will hold.")
        return False


class HUMPLAYER(Player):
    hum_names = ['Dave', 'Frank']

    def __init__(self, number):
        # assigns name to human player from list#

        if number < len(self.hum_names):
            name = self.hum_names[number]
        else:
            name = 'Hum{}'.format(number)

        # returns inherited hum_names to human player#
        super(HUMPLAYER, self).__init__(name)

    def __init__(self, name):
        super(HUMPLAYER, self).__init__(name)

    def keep_rolling(self, scorecard):
        # Asks human player of intent to roll or hold#

        human_decision = input_number(
            "${self.cpu.name},   1 - Roll again, 0 - Hold? ", 0, 1)

        # will roll if human enters 1, otherwise will hold#
        if human_decision == 1:
            return True
        else:
            return False


class Referee:
    def __init__(self, humans=1, computers=1):
        # Initializes game to 1 human player and 1 computer player#

        self.players = []  # assign human name and computer name to this list of players#
        # loops through potential human player names and adds to players#
        for i in range(humans):
            self.players.append(HUMPLAYER(i))
        return human

        # loops through potential computer player names and adds to players#
        for i in range(computers):
            self.players.append(CPUPLAYER(i))
        return computer

        # stores value of player count to nbr_of_players#
        self.nbr_of_players = len(self.players)

        self.die = Die()
        self.scorecard = Scorecard()


@staticmethod  # used to format welcome message#
def welcome():

    print("*" * 70)  # prints 70 inline asterisks#
    print(("Hello,  '{}'(self.human.name) and '{}'self.cpu.name").center(70))
    print("Welcome to Pig Dice!" .center(70))
    print("*" * 70)  # prints 70 inline asterisks#
    print("The objective is to be first in scoring 100 points." .center(70))
    print("On each turn you will roll a single die." .center(70))
    print("The die value will be recorded on a scoreboard." .center(70))
    print("(If the die is 1, the active player earns no points," .center(70))
    print("and the turn goes to the opposing player.)" .center(70))
    print("A human player may opt to either roll again," .center(70))
    print("or hold. If the human player holds, those points" .center(70))
    print("will be added to your total on the scoreboard." .center(70))
    print(" Good luck!".center(70, "*"))
    print(" And, playa, don't even think about disconnecting the computer! " .center(70, "*"))
    print()
    print("I will now throw the die to decide who starts" .center(70, " "))
    print()

    def whooz_on_first(self):
        # Randomly choose starting player, and print name#

        self.active_player = random.randint(
            1, self.nbr_of_players) % self.nbr_of_players

        print('{} starts'.format(self.players[self.active_player].name))

    def next_player(self):  # change active player to next player#"
        self.active_player = (self.active_player + 1) % self.nbr_of_players

    def previous_player(self):  # change active player to previous player#"
        self.active_player = (self.active_player - 1) % self.nbr_of_players

    def get_all_scores(self):  # Returns a join of all player scores#
        return ', '.join(str(player) for player in self.players)

    def play_game(self):
        # Plays an entire game#

        self.welcome()
        self.whooz_on_first()
        self.players()

        while all(player.score < 100 for player in self.players):
            # If no winner, print current player scores and print player names#
            print('\nCurrent score --> {}'.format(self.get_all_scores()))
            print(
                '\n*** {} to play ***'.format(self.players[self.active_player].name))
            self.scorecard.reset()

            while self.keep_rolling():
                pass
            # keep updating scorecard for as long as game is rolling#
            self.players[self.active_player].add_score(self.scorecard.value)
            self.next_player()

            self.previous_player()  # The previous player has won...#
            print(' {} has won '.format(
                self.players[self.active_player].name).center(70, '*'))

        def keep_rolling(self):
            # Adds rolled dice to scorecard. Returns if human/cpu wants to continue#
            # If either player rolls 1, scorecard value is reset, and turn ends#

            try:
                dice_value = self.die.roll()
                self.scorecard.add_dice_value(dice_value)
                print('Last roll: {}, your score is now: {}'.format(
                    dice_value, self.scorecard.value))

            # Check if human (by asking) or cpu(by calculating) will keep rolling
                return self.players[self.active_player].keep_rolling(self.scorecard)

            except RollOne:
                print('  Rolled one. Switching turns')
                self.scorecard.reset()
                return False

    def main():
        human_players = input_number('How many human players please? ')
        computer_players = input_number('How many computer players? ')

        referee = Referee(human_players, computer_players)
        referee.play_game()

    if __name__ == '__main__':
        main()
