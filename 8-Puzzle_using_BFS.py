import heapq

class EightPuzzle:
    def __init__(self, initial_state):
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.initial_state = initial_state

    def display_state(self, state):
        for row in state:
            print(row)

    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def heuristic_manhattan(self, state):
        h = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    goal_i, goal_j = divmod(state[i][j] - 1, 3)
                    h += abs(i - goal_i) + abs(j - goal_j)
        return h

    def is_goal_state(self, state):
        return state == self.goal_state

    def get_neighbors(self, state):
        neighbors = []
        blank_i, blank_j = self.find_blank(state)

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for move in moves:
            new_i, new_j = blank_i + move[0], blank_j + move[1]

            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in state]
                new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
                neighbors.append(new_state)

        return neighbors

    def solve(self):
        open_list = [(self.heuristic_manhattan(self.initial_state), self.initial_state)]
        heapq.heapify(open_list)
        closed_set = set()

        while open_list:
            _, current_state = heapq.heappop(open_list)

            if self.is_goal_state(current_state):
                return current_state

            closed_set.add(tuple(map(tuple, current_state)))

            for neighbor in self.get_neighbors(current_state):
                if tuple(map(tuple, neighbor)) not in closed_set:
                    heapq.heappush(open_list, (self.heuristic_manhattan(neighbor), neighbor))

        return None

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    puzzle = EightPuzzle(initial_state)
    solution = puzzle.solve()

    if solution:
        print("Solution found:")
        puzzle.display_state(solution)
    else:
        print("No solution exists.")