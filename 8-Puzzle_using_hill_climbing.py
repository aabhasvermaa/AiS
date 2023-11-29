import random

class EightPuzzle:
    def __init__(self):
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state
        self.current_state = self.generate_random_state()  # Initial state

    def generate_random_state(self):
        numbers = list(range(9))
        random.shuffle(numbers)
        state = [[numbers[3 * i + j] for j in range(3)] for i in range(3)]
        return state

    def display_state(self, state):
        for row in state:
            print(row)

    def heuristic(self, state):
        # Misplaced Tiles heuristic
        h = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0 and state[i][j] != self.goal_state[i][j]:
                    h += 1
        return h

    def hill_climbing(self):
        while True:
            neighbors = self.get_neighbors()
            if not neighbors:
                print("Local maxima reached. Could not find a better solution.")
                break

            best_neighbor = min(neighbors, key=lambda x: self.heuristic(x))
            if self.heuristic(best_neighbor) >= self.heuristic(self.current_state):
                print("Reached local maxima. Current state:")
                self.display_state(self.current_state)
                break

            self.current_state = best_neighbor
            print("Current state (h =", self.heuristic(self.current_state), "):")
            self.display_state(self.current_state)

    def get_neighbors(self):
        neighbors = []
        empty_i, empty_j = self.find_empty_tile(self.current_state)

        # Define possible moves (up, down, left, right)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for move in moves:
            new_i, new_j = empty_i + move[0], empty_j + move[1]

            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row[:] for row in self.current_state]  # Create a copy of the current state
                new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
                neighbors.append(new_state)

        return neighbors

    def find_empty_tile(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

if __name__ == "__main__":
    puzzle = EightPuzzle()
    print("Initial state:")
    puzzle.display_state(puzzle.current_state)
    print("Goal state:")
    puzzle.display_state(puzzle.goal_state)
    puzzle.hill_climbing()