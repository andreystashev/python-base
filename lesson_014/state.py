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


# from __future__ import annotations
# from abc import ABC, abstractmethod
#
#
# class Context:
      # TODO это параметр класса в котором как раз мы и храним состояние
      # TODO None потому что пока в момент состоние не определено!
#     _state = None - это должно означать отсутствие броска?
# TODO тут параметр экземпляра принимает объект класса типа State
# TODO можно вообще анатации не использовать но сними тут более менее все явно что бы не запустаться
#     def __init__(self, state: State) -> None: значение этой записи не пойму, но мне получается нужно тоже самое
#                                                с импортом annotations прописать в коде заменив только название метода?
#         self.transition_to(state)

# TODO как раз метод который меняет состояние у объекта Context, на вход как и писал выше
# TODO приходи состояние типа класса State, сюда мы передали первое состояние
# TODO и сразу вызываем в ините это метод
#     def transition_to(self, state: State): запись state: State непонятна, сюда получается должен попадать класс
#                                                 первого броска при создании класса контекст?
#         print(f"Context: Transition to {type(state).__name__}")
# TODO тут все еще идут манипуляции  чтобы состояние поменять, состояние которое мы получили на вход
# TODO присваиваем переменной класса
#         self._state = state здесь state является первым броском и заменяет отсутствие броска?
# TODO у состоние которое мы приняли есть метод который определен декоратором property
# TODO вот он как раз нужен чтобы обращаться через точку к context, а за ровно отвечает сеттер,
# TODO и мы возвращаем самих себя тоесть экземпляр класса контекст.
#         self._state.context = self вот тут непонятен смысл строки
#
# TODO это наши две функции первого броска и второго черз них мы будет обращать к
# TODO функциям которые определны в интерфейсе State как состояния
#     def request1(self):здесь это сделано чтобы при первом броске _state становилась вторым броском?
#         self._state.handle1()

# TODO все верно при первом броске тут ничего не определяем, и на оборот при втором броске
# TODO в request1 ничего не переопределяем
#     def request2(self): a здесь если первый бросок, то ничего не будет происходить, а если второй, то _state принимает значение первого?
#         self._state.handle2()
#
#
# class State(ABC):
#
# TODO это у нас интерфейс где классам определяется их логика и что можно, вот проперти
# TODO отвечает за то чтобы к параметру можно было обратиться через точку
#     @property здесь непонятно зачем 2 первых метода
#     def context(self) -> Context:
#         return self._context
#
# TODO сеттр отвечает за то что можно присвоить, за знак равно.
#     @context.setter
#     def context(self, context: Context) -> None:
#         self._context = context
#
# TODO декораторы нужны для того чтобы нам показать что это методы абстрактного класса и их
# TODO нужно переопределять в коде.
#     @abstractmethod  здесь не понятно зачем декораторы, у меня без них в strike и spare выводился результат
#     def handle1(self) -> None:
#         pass
#
#     @abstractmethod
#     def handle2(self) -> None:
#         pass
#
#
# TODO все верно, первый брок отвечает за все символы которые могут быть при первом броске
# TODO страйк, число, ничего не сбил, после каждой проверки ВОТ ТУТ ПЕРЕДАЕМ управление
# TODO второму состоянию

# class ConcreteStateA(State): получается 1 бросок(FirstMove(State) из моего кода), в него нужно что-то включать кроме страйка?
#     def handle1(self) -> None:
#         print("ConcreteStateA handles request1.")
#         print("ConcreteStateA wants to change the state of the context.")
# TODO это как раз механизм передачи состояния
#         self.context.transition_to(ConcreteStateB()) вот здесь я так понял моя ошибка что нет такого вызова
#
# TODO по скольку у нас это абстрактные классы в методе стайте, его нужно обязательно
# TODO переопределять, но нам там ничего не нужно мы в нем верно просто напишем pass
#     def handle2(self) -> None:
#         print("ConcreteStateA handles request2.") здесь получается нужно pass ставить тобы не прерывать рассчеты?
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
# TODO первое состоние передается с чего начинать
#     context = Context(ConcreteStateA()) здесь сразу передается первый бросок
# TODO все верно тут должен быть цикл, пока есть что проверять можно сделать такое условие
#     context.request1()здесь он расчитывается и передается второй
#     context.request2()
# TODO для начала все что написано можно оставить, это полное описание и реализация на простом
# TODO примере паттрна состояния.
