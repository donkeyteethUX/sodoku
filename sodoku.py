import numpy as np
from itertools import product

p = np.array([
                    [5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,9]])

def solve(puzzle = p):
    for (i, j) in [x for x in product(range(9),range(9)) if not puzzle[x[0], x[1]]]:
        for v in filter(lambda x: not (x in np.concatenate([puzzle[(i//3)*3:(i//3*3)+3,(j//3)*3:(j//3*3)+3].flatten(),puzzle[:,j],puzzle[i]])), range(1, 10)):
            puzzle[i, j] = v
            p = solve(puzzle)
            if 0 in p.flatten():
                puzzle[i, j] = 0
        return puzzle
    return puzzle

if __name__ == '__main__':
    print(solve())