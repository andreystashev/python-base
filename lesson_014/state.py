from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def strike(self):
        pass

    @abstractmethod
    def spare(self):
        pass

    @staticmethod
    def count(element):
        if element == '-':
            return 0
        if element != '0':
            return int(element)


class Bowling:
    def __init__(self):
        self.state = None
        self.move_counter = 0
        self.total_score = 0

    def change_state(self, state):
        self.state = state

    def char_state(self, element):
        if element == 'X':
            self.total_score += self.state.strike()
        elif element == '/':
            self.total_score += self.state.spare()
        elif element.isdigit() or element == '-':
            self.total_score += self.state.count(element)

    def split(self, game_result):
        frame = game_result[self.move_counter] + game_result[self.move_counter + 1] \
            if game_result[self.move_counter] != 'X' else game_result[self.move_counter]
        yield frame
        self.move_counter += 1 if len(frame) == 2 else 0

    def switch(self, game_result):
        while self.move_counter < len(game_result):
            frame_generation = self.split(game_result)
            for frame in frame_generation:
                if len(frame) == 1:
                    self.change_state(FirstMove())
                    self.char_state(frame[0])
                elif frame[1] == '/' and frame[0].isdigit() and frame[0] != '0':
                    self.change_state(SecondMove())
                    self.char_state(frame[1])
                else:
                    self.change_state(FirstMove())
                    self.char_state(frame[0])
                    self.change_state(SecondMove())
                    self.char_state(frame[1])
                self.move_counter += 1


class FirstMove(State):
    def strike(self):
        return 20

    def spare(self):
        pass


class SecondMove(State):
    def strike(self):
        pass

    def spare(self):
        return 15


class MarketMove1(FirstMove):
    def strike(self):
        return 10

    def spare(self):
        raise ValueError('В первом броске не может быть спэра')


class MarketMove2(SecondMove):
    def strike(self):
        raise ValueError('Во втором броске не может быть страйка')

    def spare(self):
        return 10


class MarketBowling(Bowling):

    def __init__(self):
        super().__init__()
        self.frame_count = 0

    def split(self, game_result):
        if self.move_counter + 1 == len(game_result) and game_result[self.move_counter] == 'X':
            frame = game_result[self.move_counter]
        elif self.move_counter + 2 == len(game_result) and (
                game_result[self.move_counter + 1] == '/' or game_result[self.move_counter + 1] == 'X'):
            frame = game_result[self.move_counter] + game_result[self.move_counter + 1]
        else:
            frame = game_result[self.move_counter] + game_result[self.move_counter + 1] + game_result[
                self.move_counter + 2] \
                if game_result[self.move_counter] == 'X' or game_result[self.move_counter + 1] == '/' \
                else game_result[self.move_counter] + game_result[self.move_counter + 1]
        self.frame_count += 1
        if self.frame_count > 10:
            raise ValueError('Нельзя играть больше 10 фреймов')
        yield frame
        if self.move_counter != len(game_result):
            if len(frame) == 2 and frame != 'XX' or game_result[self.move_counter] == '/':
                self.move_counter += 1
        else:
            self.move_counter += 0

    def switch(self, game_result):
        while self.move_counter < len(game_result):
            frame_generation = self.split(game_result)
            for frame in frame_generation:
                if len(frame) == 3:
                    if frame[0] == 'X' and frame[2] == '/':
                        self.change_state(MarketMove1())
                        self.char_state(frame[0])
                        self.change_state(MarketMove2())
                        self.char_state(frame[2])
                    elif frame[1] == '/' and frame[0].isdigit() and frame[0] != '0':
                        self.change_state(MarketMove2())
                        self.char_state(frame[1])
                        self.change_state(MarketMove1())
                        self.char_state(frame[2])
                    else:
                        self.change_state(MarketMove1())
                        self.char_state(frame[0])
                        self.char_state(frame[1])
                        self.char_state(frame[2])
                elif len(frame) == 1:
                    self.change_state(MarketMove1())
                    self.char_state(frame[0])
                elif frame[1] == '/' and frame[0].isdigit() and frame[0] != '0':
                    self.change_state(MarketMove2())
                    self.char_state(frame[1])
                elif frame[0] == 'X' and frame[1] == 'X':
                    self.change_state(MarketMove1())
                    self.char_state(frame[0])
                    self.char_state(frame[1])
                else:
                    if frame[0].isdigit() and frame[1].isdigit():
                        if int(frame[0]) + int(frame[1]) >= 10:
                            pass

                    self.change_state(FirstMove())
                    self.char_state(frame[0])
                    self.change_state(SecondMove())
                    self.char_state(frame[1])
                self.move_counter += 1
# result = '1212121212XX121112'
# bow = Bowling()
# bow.switch(game_result=result)
# print(bow.total_score)

# from __future__ import annotations
# from abc import ABC, abstractmethod
#
#
# class Context:
#  это параметр класса в котором как раз мы и храним состояние
#  None потому что пока в момент состоние не определено!
#     _state = None - это должно означать отсутствие броска?
#  тут параметр экземпляра принимает объект класса типа State
#  можно вообще анатации не использовать но сними тут более менее все явно что бы не запустаться
#     def __init__(self, state: State) -> None: значение этой записи не пойму, но мне получается нужно тоже самое
#                                                с импортом annotations прописать в коде заменив только название метода?
#         self.transition_to(state)

#  как раз метод который меняет состояние у объекта Context, на вход как и писал выше
#  приходи состояние типа класса State, сюда мы передали первое состояние
#  и сразу вызываем в ините это метод
#     def transition_to(self, state: State): запись state: State непонятна, сюда получается должен попадать класс
#                                                 первого броска при создании класса контекст?
#         print(f"Context: Transition to {type(state).__name__}")
#  тут все еще идут манипуляции  чтобы состояние поменять, состояние которое мы получили на вход
#  присваиваем переменной класса
#         self._state = state здесь state является первым броском и заменяет отсутствие броска?
#  у состоние которое мы приняли есть метод который определен декоратором property
#  вот он как раз нужен чтобы обращаться через точку к context, а за ровно отвечает сеттер,
#  и мы возвращаем самих себя тоесть экземпляр класса контекст.
#         self._state.context = self вот тут непонятен смысл строки
#
#  это наши две функции первого броска и второго черз них мы будет обращать к
#  функциям которые определны в интерфейсе State как состояния
#     def request1(self):здесь это сделано чтобы при первом броске _state становилась вторым броском?
#         self._state.handle1()

# все верно при первом броске тут ничего не определяем, и на оборот при втором броске
#  в request1 ничего не переопределяем
#     def request2(self): a здесь если первый бросок, то ничего не будет происходить, а если второй, то _state принимает значение первого?
#         self._state.handle2()
#
#
# class State(ABC):
#
#  это у нас интерфейс где классам определяется их логика и что можно, вот проперти
#  отвечает за то чтобы к параметру можно было обратиться через точку
#     @property здесь непонятно зачем 2 первых метода
#     def context(self) -> Context:
#         return self._context
#
# сеттр отвечает за то что можно присвоить, за знак равно.
#     @context.setter
#     def context(self, context: Context) -> None:
#         self._context = context
#
# декораторы нужны для того чтобы нам показать что это методы абстрактного класса и их
# нужно переопределять в коде.
#     @abstractmethod  здесь не понятно зачем декораторы, у меня без них в strike и spare выводился результат
#     def handle1(self) -> None:
#         pass
#
#     @abstractmethod
#     def handle2(self) -> None:
#         pass
#
#
#  все верно, первый брок отвечает за все символы которые могут быть при первом броске
#  страйк, число, ничего не сбил, после каждой проверки ВОТ ТУТ ПЕРЕДАЕМ управление
#  второму состоянию

# class ConcreteStateA(State): получается 1 бросок(FirstMove(State) из моего кода), в него нужно что-то включать кроме страйка?
#     def handle1(self) -> None:
#         print("ConcreteStateA handles request1.")
#         print("ConcreteStateA wants to change the state of the context.")
# это как раз механизм передачи состояния
#         self.context.transition_to(ConcreteStateB()) вот здесь я так понял моя ошибка что нет такого вызова
#
#  по скольку у нас это абстрактные классы в методе стайте, его нужно обязательно
#  переопределять, но нам там ничего не нужно мы в нем верно просто напишем pass
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
#  первое состоние передается с чего начинать
#     context = Context(ConcreteStateA()) здесь сразу передается первый бросок
#  все верно тут должен быть цикл, пока есть что проверять можно сделать такое условие
#     context.request1()здесь он расчитывается и передается второй
#     context.request2()
#  для начала все что написано можно оставить, это полное описание и реализация на простом
#  примере паттрна состояния.
