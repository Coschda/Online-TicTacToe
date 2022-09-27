class Game:
    def __init__(self):
        self.turn = 1
        self.grid = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

    def play(self, move, pos):
        if self.grid[pos[0]][pos[1]] == 0:
            self.grid[pos[0]][pos[1]] = move
            self.turn += 1

    def check_win(self):
        #x if player 1 wins
        #o if player 2 wins
        #-1 if game ongoing
        #0 if a tie
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != 0:
                return self.grid[i][0]

        for i in range(3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != 0:
                return self.grid[0][i]

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != 0:
            return self.grid[0][0]
        
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[1][1] != 0:
            return self.grid[1][1]
        
        comp = 0
        for i in self.grid:
            for j in i:
                if j == 0:
                    comp+=1
        
        if comp == 0:
            return 0
        
        return -1