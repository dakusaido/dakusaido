class GameOneZero(object):

    def __init__(self):
        self.error_coin = 0
        self.end_number = None
        self.count = None
        self.column = None
        self.line = None
        self.player_kaf = [0]
        self.player_count = 0
        self.lst = [
            [[], [], []],
            [[], [], []],
            [[], [], []]
        ]

    def make_game(self):
        print(self.lst[0], self.lst[1], self.lst[2], sep='\n')
        print('Please select a cell\n')
        self.run_game()

    def run_game(self):
        self.check_lst()
        if self.player_count == 0 and self.error_coin != 1:
            self.player_kaf = [0]
            self.player_count = 1
        elif self.player_count == 1 and self.error_coin != 1:
            self.player_kaf = [1]
            self.player_count = 0

        self.error_coin = 0
        print(self.player_kaf)
        self.line = int(input('Select line ')) - 1
        self.column = int(input('Select column ')) - 1

        if 0 <= self.line < 3 and 0 <= self.column < 3:
            if not self.lst[self.line][self.column]:
                self.lst[self.line][self.column] = self.player_kaf
                self.make_game()
            else:
                print('This cell is occupied!')
                self.error_coin = 1
                self.run_game()
        else:
            print('number -- 1, 2 or 3!!!')
            self.error_coin = 1
            self.run_game()

    def end_game(self):
        print(f'Player {self.player_kaf} Win!')
        self.end_number = input('If you want to exit, enter "zero" ')
        if self.end_number == 'zero':
            exit()
        self.lst = [
            [[], [], []],
            [[], [], []],
            [[], [], []]
        ]
        self.make_game()

    def check_lst(self):

        for x in range(2):

            # victory across the line
            if self.lst[0][0] == [x] and self.lst[0][1] == [x] and self.lst[0][2] == [x] or \
                    self.lst[1][0] == [x] and self.lst[1][1] == [x] and self.lst[1][2] == [x] or \
                    self.lst[2][0] == [x] and self.lst[2][1] == [x] and self.lst[2][2] == [x]:
                self.end_game()
                break

            # victory along the entire diagonal
            if self.lst[0][0] == [x] and self.lst[1][1] == [x] and self.lst[2][2] == [x] or \
                    self.lst[0][2] == [x] and self.lst[1][1] == [x] and self.lst[2][0] == [x]:
                self.end_game()
                break

            # victory in the whole column
            if self.lst[0][0] == [x] and self.lst[1][0] == [x] and self.lst[2][0] == [x] or \
                    self.lst[0][1] == [x] and self.lst[1][1] == [x] and self.lst[2][1] == [x] or \
                    self.lst[0][2] == [x] and self.lst[1][2] == [x] and self.lst[2][2] == [x]:
                self.end_game()
                break


if __name__ == '__main__':
    obj = GameOneZero()
    obj.make_game()
