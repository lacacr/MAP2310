import matplotlib.pyplot as plt
import numpy as np

def tangent_plane(function, grid_start, grid_end, interval):
    X = np.arange(grid_start[0] + interval[0], grid_end[0], interval[0])
    Y = np.arange(grid_start[1] + interval[1], grid_end[1], interval[1])
    grid = np.meshgrid(X, Y)
    U = np.ones((len(X), len(Y)))
    V = np.vectorize(function)(grid[0], grid[1])

    fig, ax = plt.subplots(figsize=(10, 10))
    q = ax.quiver(X, Y, U, V)
    ax.quiverkey(q, X=0.3, Y=1.1, U=10, label='Quiver key, length = 10', labelpos='E')

def tangent_plane_with_concavity(function, grid_start, grid_end, interval, concavity):
    X = np.arange(grid_start[0] + interval[0], grid_end[0], interval[0])
    Y = np.arange(grid_start[1] + interval[1], grid_end[1], interval[1])
    grid = np.meshgrid(X, Y)
    U = np.ones((len(X), len(Y)))
    V = np.vectorize(function)(grid[0], grid[1])
    Conc = np.vectorize(concavity)(grid[0], grid[1])
    Conc = Conc > 0

    cmap = plt.get_cmap('coolwarm')

    colors = cmap(Conc)
    rgba_colors = cmap(Conc, bytes=True)

    fig, ax = plt.subplots(figsize=(10, 10))
    q = ax.quiver(X, Y, U, V, Conc, cmap=cmap)
    ax.quiverkey(q, X=0.3, Y=1.1, U=10, label='Quiver key, length = 10', labelpos='E')