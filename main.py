from Env.gridWorld import GridWorld
from EigenOptions.visualisation import plot_gridworld_heat


if __name__ == '__main__':
    # create gridworld environment. The grid shape and winning state are in the file gridWorld.py
    grid = GridWorld()
    # print as 0,1 grid
    grid.render()
    # some random values as a demo
    important_values_to_plot = grid.random_grid_square_values()
    # plot the random values
    plot_gridworld_heat(important_values_to_plot, grid.grid)
