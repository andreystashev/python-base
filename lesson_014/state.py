from abc import ABCMeta


class Bowling:
    # TODO так классы в данном случае не создается они должны быть внешнии каждый
    class State(metaclass=ABCMeta):

        def arrange(self, element):
            if element == 'X':
                return self.strike()
            elif element == '/':
                return self.spare()
            elif element == '-':
                return 0
            else:
                return int(element)

        def strike(self):
            pass

        def spare(self):
            pass

    class FirstMove(State):
        def strike(self):
            return 20

    class SecondMove(State):
        def spare(self):
            return 15

    one_move = FirstMove()
    two_move = SecondMove()

    def __init__(self):
        self.current_move = self.one_move
        self.prev_throw_value = 0
        self.final_result = 0

    def switch(self, element):
        one_move = self.current_move is self.one_move
        value = self.current_move.arrange(element)
        self.final_result += value
        if not one_move:
            if element == '/':
                self.final_result -= self.prev_throw_value
            self.current_move = self.one_move
        elif element != 'X':
            self.current_move = self.two_move
        self.prev_throw_value = value


# TODO что именно из этого примера вам не понятно ?
# TODO https://refactoring.guru/ru/design-patterns/state
# TODO задавайте вопросы будем разбираться поэтапно.
