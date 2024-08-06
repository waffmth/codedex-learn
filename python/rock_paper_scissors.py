import random


class RockPaperScissors:
    def __init__(self):
        sep = '=' * 41
        print(sep)
        print(' ' * 11 + 'Rock Paper Scissors')
        print(sep)
        print()
        self.__finished = False
        self._result = 0

    def _check(self, p: int, c: int):
        win_rule = {1: 3, 2: 1, 3: 2}
        if p == c:
            return 0
        if win_rule[p] == c:
            return 1
        return -1

    def play(self):
        print('(1) ✊   (2) ✋   (3) ✌️')
        player = 0
        while True:
            try:
                choice = int(input('Pick a number: '))
                if choice in [1, 2, 3]:
                    player = choice
                    break
            except:
                print('Invalid choice')

        computer = random.randint(1, 3)
        print()
        symbols = ['✊', '✋', '✌']
        print(f'You chose: {symbols[player - 1]}')
        print(f'CPU chose: {symbols[computer - 1]}')
        self.__finished = True
        self._result = self._check(player, computer)

    def show_result(self):
        assert self.__finished, "Game isn't finished yet. Did you forget to call play()?"
        sep = '=' * 41
        print(sep)
        if self._result == 0:
            print((' ' * 15) + "It's a tie!")
        elif self._result == 1:
            print((' ' * 13) + 'The player won!')
        else:
            print((' ' * 12) + 'The computer won!')
        print(sep)


if __name__ == '__main__':
    rps = RockPaperScissors()
    rps.play()
    rps.show_result()
