# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that
# returns two grids. The first grid, value, should
# contain the computed value of each cell as shown
# in the video. The second grid, policy, should
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']  # Use these when creating your policy grid.


# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid, goal, cost_step, collision_cost, success_prob):
    failure_prob = (1.0 - success_prob) / 2.0  # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for _ in range(len(grid[0]))] for _ in range(len(grid))]
    policy = [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    value[goal[0]][goal[1]] = 0
    policy[goal[0]][goal[1]] = '*'
    refresh = True
    while refresh:
        refresh = False
        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                if grid[row][cell] == 0:
                    for d in range(len(delta)):
                        x = row + delta[d][0]
                        y = cell + delta[d][1]
                        x_right = row + delta[d - 1][0]
                        y_right = cell + delta[d - 1][1]
                        x_left = row + delta[(d + 1) % len(delta)][0]
                        y_left = cell + delta[(d + 1) % len(delta)][1]
                        if len(grid) > x >= 0 <= y < len(grid[row]):
                            if len(grid) > x_right >= 0 <= y_right < len(grid[row]):
                                right_side = failure_prob * value[x_right][y_right]
                            else:
                                right_side = failure_prob * collision_cost
                            if len(grid) > x_left >= 0 <= y_left < len(grid[row]):
                                left_side = failure_prob * value[x_left][y_left]
                            else:
                                left_side = failure_prob * collision_cost
                            new_value = value[x][y] * success_prob + left_side + right_side + cost_step
                            if new_value < value[row][cell]:
                                value[row][cell] = new_value
                                policy[row][cell] = delta_name[d]
                                refresh = True
    return value, policy


# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0]) - 1]  # Goal is in top right corner
cost_step = 1
collision_cost = 100
success_prob = 0.5

value, policy = stochastic_value(grid, goal, cost_step, collision_cost, success_prob)
for row in value:
    print row
for row in policy:
    print row

# Expected outputs:
#
# [57.9029, 40.2784, 26.0665,  0.0000]
# [47.0547, 36.5722, 29.9937, 27.2698]
# [53.1715, 42.0228, 37.7755, 45.0916]
# [77.5858, 100.00, 100.00, 73.5458]
#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
