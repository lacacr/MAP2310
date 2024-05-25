import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

def tangent_plane(function, grid_start, grid_end, interval):
    X = np.arange(grid_start[0] + interval[0], grid_end[0], interval[0])
    Y = np.arange(grid_start[1] + interval[1], grid_end[1], interval[1])
    grid = np.meshgrid(X, Y)
    U = np.ones((len(X), len(Y)))
    V = np.vectorize(function)(grid[0], grid[1])
    Norm = np.sqrt(U**2 + V**2)

    fig, ax = plt.subplots(figsize=(10, 10))
    q = ax.quiver(X, Y, U/Norm, V/Norm)
    ax.quiverkey(q, X=0.3, Y=1.1, U=10, label='Quiver key, length = 10', labelpos='E')

def tangent_plane_with_concavity(function, grid_start, grid_end, interval, concavity):
    X = np.arange(grid_start[0] + interval[0], grid_end[0], interval[0])
    Y = np.arange(grid_start[1] + interval[1], grid_end[1], interval[1])
    grid = np.meshgrid(X, Y)
    U = np.ones((len(X), len(Y)))
    V = np.vectorize(function)(grid[0], grid[1])
    Norm = np.sqrt(U**2 + V**2)
    Conc = np.vectorize(concavity)(grid[0], grid[1])
    Conc = Conc > 0

    cmap = ListedColormap(['blue', 'red'])

    colors = cmap(Conc)
    rgba_colors = cmap(Conc, bytes=True)

    fig, ax = plt.subplots(figsize=(10, 10))
    q = ax.quiver(X, Y, U/Norm, V/Norm, Conc, cmap=cmap)
    ax.quiverkey(q, X=0.3, Y=1.1, U=10, label='Quiver key, length = 10', labelpos='E')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Plano tangente com concavidade')

    cbar = plt.colorbar(q, ax=ax, ticks=[0.25, 0.75], shrink=0.2)
    cbar.set_label('Concavidade')
    cbar.set_ticklabels(["f''<0", "f''>0"])