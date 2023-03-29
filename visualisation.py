import numpy as np
import math
import matplotlib.pyplot as plt


def plot_gridworld_heat(state_values_to_plot, grid):
    """
    USE THIS ONE: plot a heatmap of the value of grid squares
    :param vector: a flattened version of the grid square values
    :param grid: the 0,1 grid first input when creating a GridWorld object (Gridworld.grid)
    """
    full_grid = add_in_walls(state_values_to_plot, grid)
    original_dim = grid.shape  # get dims to turn back into grid
    full_grid_sq = full_grid.reshape(original_dim)
    plot_as_heat(full_grid_sq)


def add_in_walls(not_walls, grid):
    """
    Add the walls back in to the grid so the clusters can be visualised in context
    :param not_walls: the values you want to plot
    :param grid: the original 0,1 grid used to make the gridworld
    """
    wall_states = np.isin(grid, 1)

    # flatten wall states matrix and matrix to add walls to
    flat_matrix = np.array(not_walls).flatten()
    wall_states_flat = wall_states.flatten()

    # add in walls to flattened matrix
    flat_with_walls = np.array(flat_matrix, dtype=float)
    for i, b in enumerate(wall_states_flat):
        if b:
            flat_with_walls = np.insert(flat_with_walls, i, np.nan)
    return flat_with_walls


def plot_as_heat(grid_clusters):
    """
    Plot the gridworld with clusters as a heatmap. Walls will be identified on the heatmap
    :param grid_clusters: gridworld with walls as nan, and clusters as real numbers
    """
    # wall states now have a value of NAN, change it to -1 so the heatmap plots them as black
    grid_clusters = np.nan_to_num(grid_clusters, nan=-1)
    # plot heatmap
    plt.imshow(grid_clusters, cmap='hot', interpolation='nearest')
    plt.show()
