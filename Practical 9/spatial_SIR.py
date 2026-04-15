# Spatial SIR model on a 2D grid
# This code simulates the spread of an infectious disease using a spatial SIR model on a 2D grid. Each cell in the grid can be in one of three states: susceptible (0), infected (1), or recovered (2). The simulation starts with a random outbreak of infection and evolves over time based on the infection and recovery probabilities. The code visualizes the spread of the disease across the grid at each time step, allowing us to observe how the infection propagates spatially.  
import numpy as np
import matplotlib.pyplot as plt

grid = np.zeros((100, 100))

outbreak = np.random.choice(range(100), 2)
grid[outbreak[0], outbreak[1]] = 1

beta = 0.3
gamma = 0.05

for t in range(100):

    new_grid = grid.copy()

    infected = np.argwhere(grid == 1)

    for cell in infected:
        x, y = cell

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:

                nx, ny = x + dx, y + dy

                if 0 <= nx < 100 and 0 <= ny < 100:

                    if grid[nx, ny] == 0:
                        if np.random.rand() < beta:
                            new_grid[nx, ny] = 1

        if np.random.rand() < gamma:
            new_grid[x, y] = 2

    grid = new_grid

    plt.imshow(grid, cmap='viridis')
    plt.title(f"Time {t}")
    plt.pause(0.1)

plt.show()
