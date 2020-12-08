from abc import ABCMeta


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


class Bowling:
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

#

# TODO Не могу осознать как это состояние применяется в коде. В описании используется другой язык, всю суть статьи трудно понять.
#  Сама работа паттерна очевидна, но в этой задаче тоже есть некая путаница. Сейчас постараюсь на примере задать вопросы из этой задачи
#
# from __future__ import annotations
# from abc import ABC, abstractmethod
#
#
# class Context:
#     _state = None todo это должно означать отсутствие броска?
#
#     def __init__(self, state: State) -> None: todo значение этой записи не пойму, но мне получается нужно тоже самое
#                                                с импортом annotations прописать в коде заменив только название метода?
#         self.transition_to(state)


#     def transition_to(self, state: State): todo запись state: State непонятна, сюда получается должен попадать класс
#                                                 первого броска при создании класса контекст?
#         print(f"Context: Transition to {type(state).__name__}")
#         self._state = state todo здесь state является первым броском и заменяет отсутствие броска?
#         self._state.context = self todo вот тут непонятен смысл строки
#
#     def request1(self): todo здесь это сделано чтобы при первом броске _state становилась вторым броском?
#         self._state.handle1()
#
#     def request2(self): todo a здесь если первый бросок, то ничего не будет происходить, а если второй, то _state принимает значение первого?
#         self._state.handle2()
#
#
# class State(ABC):
#
#     @property todo здесь непонятно зачем 2 первых метода
#     def context(self) -> Context:
#         return self._context
#
#     @context.setter
#     def context(self, context: Context) -> None:
#         self._context = context
#
#     @abstractmethod   todo здесь не понятно зачем декораторы, у меня без них в strike и spare выводился результат
#     def handle1(self) -> None:
#         pass
#
#     @abstractmethod
#     def handle2(self) -> None:
#         pass
#
#
# class ConcreteStateA(State): todo здесь получается 1 бросок(FirstMove(State) из моего кода), в него нужно что-то включать кроме страйка?
#     def handle1(self) -> None:
#         print("ConcreteStateA handles request1.")
#         print("ConcreteStateA wants to change the state of the context.")
#         self.context.transition_to(ConcreteStateB()) todo вот здесь я так понял моя ошибка что нет такого вызова
#
#     def handle2(self) -> None:
#         print("ConcreteStateA handles request2.") todo здесь получается нужно pass ставить тобы не прерывать рассчеты?
#
#
# class ConcreteStateB(State):
#     def handle1(self) -> None:
#         print("ConcreteStateB handles request1.")
#
#     def handle2(self) -> None:
#         print("ConcreteStateB handles request2.")
#         print("ConcreteStateB wants to change the state of the context.")
#         self.context.transition_to(ConcreteStateA())
#
#
# if __name__ == "__main__":
#     # Клиентский код.
#
#     context = Context(ConcreteStateA()) todo здесь сразу передается первый бросок
#     context.request1()todo здесь он расчитывается и передается второй
#     context.request2()todo здесь второй расчитывается и передается первый. И эти 2 вызова нужно в цикл обернуть получается
# todo еще если убирать/упрощать какие-то сомнительные части кода, то он все-равно в некоторых случаях продолжает работать и возникает
#  вопрос что в нем 100% должно быть, а чего недолжно.