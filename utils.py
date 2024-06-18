import matplotlib.pyplot as plt

from source import Grid


def visualize_grid(grid: Grid):
    """Visualize the grid using matplotlib."""
    plt.imshow(grid, cmap="gray")
    plt.show()
