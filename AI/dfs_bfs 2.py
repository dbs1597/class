class State:
    def __init__(self, board, goal, moves = 0):
        self.board = board
        self.moves = moves
        self.goal = goal

    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)

    def expand(self, moves):
        result = []
        i = self.board.index(0)
        if not i in [0, 1, 2]:
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [0, 3, 6]:
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [2, 5, 8]:
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [6, 7, 8]:
            result.append(self.get_new_board(i, i-1, moves))
        return result
        
    def _str_(self):
        return (str(self.board[:3]) + "" + str(self.board[3:6]) + "" + str(self.board[6:]) + "" + "------------------")


def dfs():
    pass


def bfs():
    pass


if __name__ == "__main__":
    puzzle = [1, 2, 3, 0, 4, 6, 7, 5, 8]

    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
#    ex2 = State(puzzle, goal, 0)
#
#    example = State()
#    example.board = puzzle
#    example.goal = goal

    open_queue = []
    open_queue.append(State(puzzle, goal))

    closed_queue = []
    moves = 0
    while len(open_queue) != 0:

        current = open_queue.pop(0)
        print(current)
        print("check")
        if current.board == goal:
            print("Sucess")
            break
        moves = current.moves + 1
        closed_queue.append(current)
        for state in current.expand(moves):
            if (state in closed_queue) or (state in open_queue):
                continue
            else:
                open_queue.append(state)
