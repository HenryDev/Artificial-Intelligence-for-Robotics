# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making a right turn, no turn, and a left turn


# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):
    policy2D = [[' ' for _ in row] for row in grid]
    value = []
    policy = []
    for _ in range(len(forward)):
        value.append([[999 for _ in row] for row in grid])
        policy.append([[' ' for _ in row] for row in grid])
    refresh = True
    while refresh:
        refresh = False
        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                for heading in range(len(forward)):
                    if row == goal[0] and cell == goal[1]:
                        if value[heading][row][cell] != 0:
                            value[heading][row][cell] = 0
                            policy[heading][row][cell] = '*'
                            refresh = True
                    elif grid[row][cell] == 0:
                        for a in range(len(action)):
                            new_heading = (heading + action[a]) % len(forward)
                            new_x = row + forward[new_heading][0]
                            new_y = cell + forward[new_heading][1]
                            if len(grid) > new_x >= 0 <= new_y < len(grid[row]) and grid[new_x][new_y] == 0:
                                new_value = value[new_heading][new_x][new_y] + cost[a]
                                if new_value < value[heading][row][cell]:
                                    value[heading][row][cell] = new_value
                                    policy[heading][row][cell] = action_name[a]
                                    refresh = True
    x = init[0]
    y = init[1]
    orientation = init[2]
    policy2D[x][y] = policy[orientation][x][y]
    while policy[orientation][x][y] != '*':
        if policy[orientation][x][y] == '#':
            new_orientation = orientation
        elif policy[orientation][x][y] == 'R':
            new_orientation = (orientation - 1) % len(forward)
        elif policy[orientation][x][y] == 'L':
            new_orientation = (orientation + 1) % len(forward)
        x += forward[new_orientation][0]
        y += forward[new_orientation][1]
        orientation = new_orientation
        policy2D[x][y] = policy[orientation][x][y]
    return policy2D
