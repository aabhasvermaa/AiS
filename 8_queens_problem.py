import heapq

# Define a function to calculate the heuristic value for a state
def calculate_heuristic(state):
    heuristic = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                heuristic += 1
    return heuristic

# Define the A* search function
def solve_queens(n):
    initial_state = tuple([-1] * n)  # Initial empty board
    open_list = [(0, initial_state)]  # Priority queue for open states (cost + heuristic, state)
    closed_set = set()  # Set to store explored states

    while open_list:
        _, current_state = heapq.heappop(open_list)

        if current_state not in closed_set:
            closed_set.add(current_state)

            if current_state.count(-1) == 0:  # All queens placed, solution found
                return current_state

            for i in range(n):
                if i not in current_state:
                    for j in range(n):
                        new_state = list(current_state)
                        new_state[i] = j
                        new_state = tuple(new_state)
                        if new_state not in closed_set:
                            cost = calculate_heuristic(new_state) + n - new_state.count(-1)
                            heapq.heappush(open_list, (cost, new_state))

    return None  # No solution found

# Main function
if __name__ == "__main__":
    n = 8  # Change this to the desired board size
    solution = solve_queens(n)
    
    if solution:
        print("Solution found:")
        for row in solution:
            print("." * row + "Q" + "." * (n - row - 1))
    else:
        print("No solution found.")
