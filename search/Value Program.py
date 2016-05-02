# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    value = [[99 for _ in row] for row in grid]
    refresh = True
    value[goal[0]][goal[1]] = 0
    while refresh:
        refresh = False
        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                if grid[row][cell] == 0:
                    for i in delta:
                        x = row + i[0]
                        y = cell + i[1]
                        if len(grid) > x >= 0 <= y < len(grid[row]):
                            new_value = value[x][y] + cost
                            if new_value < value[row][cell]:
                                value[row][cell] = new_value
                                refresh = True

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return value
