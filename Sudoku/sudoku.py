
        
class Sudoku:
    def __init__(self, grid):
        self.grid = grid
        self.seen = set()

    def __str__(self):
        ret = ''
        for row in self.grid:
            fmt = ' '.join(str(i) for i in row)
            ret += fmt + '\n'
        return ret

    @property
    def boxes(self):
        indices = [(x % 3, x // 3) for x in range(9)]  
        return [[(self.grid[x*3+i][y*3+j], (x*3+i, y*3+j))
                    for i, j in indices] 
                        for x, y in indices]  
        
    @classmethod
    def open(cls, path):
        grid = []
        with open(path) as g:
            for row in g.read().splitlines():
                values = [int(i) for i in list(row)]
                grid.append(values)
        return cls(grid)

    def find_next_cell(self):
        for x, row in enumerate(self.grid):
            for y, cell in enumerate(row):
                if self.grid[x][y] == 0:
                    return (x, y)
        return False

    def in_box(self, val, x, y):
        for box in self.boxes:
            for value in box:
                if value[1] == (x, y):
                    if val in [i[0] for i in box]:
                        return True

    def valid_numbers(self, x, y):
        length = len(self.grid)
        for i in range(1, length+1):
            if all(i != self.grid[x][e] for e in range(length)):
                if all(i != self.grid[e][y] for e in range(length)):
                    if not self.in_box(i, x, y):
                        yield i

    def solve(self, x=0, y=0):
        pos = self.find_next_cell()
        if pos is False:
            return True
        else:
            x, y = pos
        for val in self.valid_numbers(x, y):
            self.grid[x][y] = val
            if self.solve(x, y) is True:
                return True
            else:
                self.grid[x][y] = 0

        return 'No Solution.'
        
if __name__ == '__main__':
    grid = Sudoku.open('sudoku.txt')
    print(grid.solve())
    print(grid)


