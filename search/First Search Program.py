# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    no_viable_path = 'fail'
    checklist = [[0 for _ in grid[0]] for _ in grid]
    checklist[init[0]][init[1]] = 1
    g_value = 0
    row, column = init
    open_list = [[g_value, row, column]]
    while len(open_list) != 0:
        open_list.sort()
        smallest_g_value = open_list[0]
        open_list.remove(smallest_g_value)
        if smallest_g_value[1] == goal[0] and smallest_g_value[2] == goal[1]:
            return smallest_g_value
        g_value, row, column = smallest_g_value
        for i in delta:
            possible_expansion_x = row + i[0]
            possible_expansion_y = column + i[1]
            is_expansion_feasible = 0 <= possible_expansion_x < len(grid) and 0 <= possible_expansion_y < len(grid[0])
            if is_expansion_feasible:
                has_not_been_checked = checklist[possible_expansion_x][possible_expansion_y] == 0
                is_not_blocked = grid[possible_expansion_x][possible_expansion_y] == 0
                if has_not_been_checked and is_not_blocked:
                    checklist[possible_expansion_x][possible_expansion_y] = 1
                    open_list.append([g_value + cost, possible_expansion_x, possible_expansion_y])
    return no_viable_path
