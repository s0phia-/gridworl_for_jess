import random
import numpy as np
from math import prod
import copy


grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

win_state = [8, 8]


class GridWorld:
    def __init__(self, random_actions=0, win_state=win_state, layout=grid):
        """
        :param random_actions: probability of the env ignoring the chosen action and selecting a move at random
        :param win_state: coordinates of goal state
        :param layout: 0,1 depiction of grid, where 1s are edges
        """
        self.grid = np.array(layout)
        self.grid_shape = self.grid.shape
        self.num_rows = self.grid_shape[0]
        self.num_cols = self.grid_shape[1]
        self.num_states = self.num_rows * self.num_cols
        self.win_state = win_state
        if random_actions is False:
            self.prob_random_action = 0
        else:
            self.prob_random_action = random_actions
        self.state = self.get_random_state()

    def get_random_state(self):
        """
        :return: a random state which doesn't land on any of the grid edges (1s)
        """
        valid_state = False
        assert np.sum(self.grid) != prod(self.grid_shape)
        while not valid_state:
            state = random.randrange(self.grid_shape[0]), random.randrange(self.grid_shape[1])
            if self.grid[state] == 0:
                valid_state = True
        return state

    def step(self, action):
        """
        :param action: should be 0 (left), 1 (right), 2 (up), 3 (down)
        :return: state action led to
        """
        h, v = self.state
        if random.random() < self.prob_random_action:
            action = random.choice([0, 1, 2, 3])
        if action == 0:  # left
            state = h-1, v
        if action == 1:  # right
            state = h+1, v
        if action == 2:  # up
            state = h, v-1
        if action == 3:  # down
            state = h, v+1
        if self.grid[state] == 1:  # if new state is a wall, go to the old state
            state = h, v
        self.state = state
        done = (state == win_state)
        reward = done*10 - (1-done)  # reward is 10 if done, otherwise -1
        return state, reward, done, ""

    def render(self):
        """
        print text version of gridworld, with 2 indicating the present state the agent is in
        """
        grid_with_state = copy.copy(self.grid)
        grid_with_state[self.state] = 2
        print(grid_with_state)

    def random_grid_square_values(self):
        """
        :return: a random set of values to plot, for demo
        """
        # create random values matrix in the shape of the gridworld
        random_vals = np.random.rand(self.num_rows, self.num_cols)

        # throw away any states that land on a wall, since I don't care about them
        random_vals_walls_removed = self.remove_walls(random_vals)

        return random_vals_walls_removed

    def remove_walls(self, matrix):
        """
        The walls in the gridworld (1 values in GridWorld.grid) aren't needed for the calc I do, so I remove them,
        they will be added back in when plotting
        """
        wall_states = np.isin(self.grid, 1)
        clean_matrix = matrix[~wall_states]
        return clean_matrix
