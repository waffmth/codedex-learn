class Connect4:
    def __init__(self):
        sep = '=' * 41
        print(sep)
        print(' ' * 16 + 'Connect 4')
        print(sep)
        print()
        self.__setup_done = False
        self.__finished = False
        self._winner = 0

    def setup(self):
        nrow = 5
        ncol = 5
        while True:
            try:
                nrow = int(input('How many rows (5 to 10)? '))
                if nrow < 5 or nrow > 10:
                    print('Out of range')
                else:
                    break
            except:
                print('Invalid value')
        while True:
            try:
                ncol = int(input('How many cols (5 to 10)? '))
                if ncol < 5 or ncol > 10:
                    print('Out of range')
                else:
                    break
            except:
                print('Invalid value')
        self._nrow = nrow
        self._ncol = ncol
        self._col_name = ['A', 'B', 'C', 'D',
                          'E', 'F', 'G', 'H', 'I', 'J'][:ncol]
        self._grid = [[' ' for __ in range(ncol)] for _ in range(nrow)]
        self._last = [nrow-1 for __ in range(ncol)]
        self.__setup_done = True
        self.__finished = False

    def _display(self):
        prefix = ' ' * (20 - 2*self._ncol)
        print(prefix + f'  {"   ".join(self._col_name)}')

        sep = '---'.join(['+' for _ in range(self._ncol + 1)])
        print(prefix + sep)

        for row in self._grid:
            content = f'| {" | ".join(row)} |'
            print(prefix + content)
            print(prefix + sep)

    def _input(self, player: int = 1):
        range_str = f'[{self._col_name[0]}-{self._col_name[-1]}]'
        col = input(f'Select column for player {player} {range_str}: ')
        if len(col) != 1:
            return None, 'Invalid value'
        col = col.upper()
        if col not in self._col_name:
            return None, 'Invalid value'
        col_idx = self._col_name.index(col)
        if self._last[col_idx] < 0:
            return None, 'Full!'
        return col_idx, None

    def _put(self, col_idx: int, p: int):
        r = self._last[col_idx]
        self._grid[r][col_idx] = str(p)
        self._last[col_idx] -= 1

    def _check(self):
        # Horizontal
        for c in range(self._ncol-3):
            for r in range(self._nrow):
                if self._grid[r][c] == self._grid[r][c+1] and self._grid[r][c+1] == self._grid[r][c+2] and self._grid[r][c+2] == self._grid[r][c+3]:
                    if self._grid[r][c] != ' ':
                        return int(self._grid[r][c])

        # Vertical
        for c in range(self._ncol):
            for r in range(self._nrow-3):
                if self._grid[r][c] == self._grid[r+1][c] and self._grid[r+1][c] == self._grid[r+2][c] and self._grid[r+2][c] == self._grid[r+3][c]:
                    if self._grid[r][c] != ' ':
                        return int(self._grid[r][c])

        # Diagonal
        for c in range(self._ncol-3):
            for r in range(self._nrow-3):
                if self._grid[r][c] == self._grid[r+1][c+1] and self._grid[r+1][c+1] == self._grid[r+2][c+2] and self._grid[r+2][c+2] == self._grid[r+3][c+3]:
                    if self._grid[r][c] != ' ':
                        return int(self._grid[r][c])
        for c in range(self._ncol-3):
            for r in range(3, self._nrow):
                if self._grid[r][c] == self._grid[r-1][c+1] and self._grid[r-1][c+1] == self._grid[r-2][c+2] and self._grid[r-2][c+2] == self._grid[r-3][c+3]:
                    if self._grid[r][c] != ' ':
                        return int(self._grid[r][c])
        return 0

    def play(self):
        assert self.__setup_done, "Game can't be started. Did you forget to call setup()?"
        assert not self.__finished, 'Game already finished. Call setup() again'

        player = 1
        turn = self._nrow * self._ncol
        self._display()
        while turn > 0:
            while True:
                col_idx, err = self._input(player)
                if col_idx is not None:
                    c = self._col_name[col_idx]
                    print(f'Player {player} select {c}')
                    self._put(col_idx, player)
                    break
                else:
                    print(err)
            self._display()
            winner = self._check()
            if winner > 0:
                self._winner = winner
                self.__finished = True
                return
            player = 3-player
            turn -= 1
        self.__finished = True

    def show_result(self):
        assert self.__finished, "Game isn't finished yet. Did you forget to call play()?"
        result = ' ' * 18 + 'Draw!'
        if self._winner > 0:
            result = ' ' * 14 + f'Player {self._winner} win!'

        sep = '=' * 41
        print()
        print(sep)
        print(result)
        print(sep)


if __name__ == '__main__':
    c4 = Connect4()
    c4.setup()
    c4.play()
    c4.show_result()
