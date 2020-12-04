from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def throw(self, throw_result):
        pass


class First_move(State):
    def __init__(self, game):
        self.game = game

    def throw(self, throw_result):
        if throw_result == 'X':
            self.game.score += 20
        else:
            if throw_result.isdigit():
                self.game.first_move_points = int(throw_result)
                self.game.state = self.game.second_move
            elif throw_result == '-':
                self.game.state = self.game.second_move


class Second_move(State):
    def __init__(self, game):
        self.game = game

    def throw(self, throw_result):
        if throw_result == '/':
            self.game.score += 15
        elif throw_result.isdigit():
            self.game.score += self.game.first_move_points + int(throw_result)

        self.game.first_move_points = 0
        self.game.state = self.game.first_move


class Bowling:
    def __init__(self):
        self.first_move = First_move(self)
        self.second_move = Second_move(self)

        self.score = 0
        self.first_move_points = 0

        self.state = self.first_move

    def throw(self, throw_result):
        self.state.throw(throw_result)


