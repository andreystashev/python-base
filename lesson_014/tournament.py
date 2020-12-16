from bowling import get_score


class Tournament:
    def __init__(self, initial_file, result_file, state):
        self.initial_file = initial_file
        self.result_file = result_file
        self.winner = []
        self.name_count_game = {}
        self.name_count_win = {}
        self.state = state

    def writing(self):
        result_file = open(self.result_file, mode='a+', encoding='utf-8')
        with open(self.initial_file, mode='r', encoding='utf-8') as file:
            for line in file:
                line = line.strip('\n')
                try:
                    if '\t' in line:
                        line = line.split('\t')
                        name = line[0]
                        scope = line[1]
                        digit_scope = get_score(scope,state=self.state)
                        new_line = f'{name}\t{scope}\t{digit_scope}'
                        result_file.write(f'{new_line}\n')
                        self.winner_info(name, digit_scope)
                        self.count_game(name)
                    elif 'winner is' in line:
                        winner_line = f'winner is {self.winner[0]}'
                        result_file.write(f'{winner_line}\n')
                        self.count_win(self.winner[0])
                        self.winner.clear()
                    else:
                        result_file.write(f'{line}\n')
                except ValueError as exc:
                    new_line = f'{name}\t{scope}\t{exc.args}'
                    result_file.write(f'{new_line}\n')
                except IndexError:
                    new_line = f'{name}\t{scope}\t(Не верное кол-во фреймов.)'
                    result_file.write(f'{new_line}\n')
        result_file.close()

    def winner_info(self, name, total_score):
        if not self.winner:
            self.winner.append(name)
            self.winner.append(total_score)
        elif self.winner[1] < total_score:
            self.winner.clear()
            self.winner.append(name)
            self.winner.append(total_score)

    def count_game(self, name):
        if name in self.name_count_game:
            self.name_count_game[name] += 1
        else:
            self.name_count_game[name] = 1

    def count_win(self, name):
        if name in self.name_count_win:
            self.name_count_win[name] += 1
        else:
            self.name_count_win[name] = 1

    def create_table(self):
        format_chars = ['+', '-', 'Игрок', 'сыграно матчей', 'всего побед']
        head_line = f'{format_chars[0]:-<11}{format_chars[0]:-<19}{format_chars[0]:-<15}{format_chars[0]}'
        words_line = f'|{format_chars[2]:^10}|{format_chars[3]:^18}|{format_chars[4]:^14}|'
        print(head_line)
        print(words_line)
        print(head_line)
        for key, value in self.name_count_game.items():
            win_size = self.name_count_win[key]
            line = f'|{key:^10}|{value:^18}|{win_size:^14}|'
            print(line)
        print(head_line)
