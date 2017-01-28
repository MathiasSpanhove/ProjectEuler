__author__ = 'Mathias'

import timeit


def find_lattice_paths(dim):
    dim += 1
    grid = [[1 for i in range(dim)] for j in range(dim)]

    for i in range(1, dim):
        for j in range(1, dim):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[dim - 1][dim - 1]


start = timeit.default_timer()
print(find_lattice_paths(20))
print(timeit.default_timer() - start)
