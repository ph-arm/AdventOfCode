# %%
import copy
import math

# f = open("./input.txt", "r")
f = open("./input_test.txt", "r")
# f = open("./par.txt", "r")
lines = f.read()
f.close()
mt = lines.split("\n")
mt = [list(i) for i in mt]


# %%
def find_re(mt, X):
    for i, c in enumerate(mt):
        for j, d in enumerate(c):
            if d == X:
                return i, j


reinder = find_re(mt, "S")
moves = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
move_k = list(moves.keys())
visited = [[[1000000000000 for i in mt[0]] for j in mt] for l in move_k]


def move_re(pos, dir, score):
    i, j = pos
    queue = []
    ci = move_k.index(dir)
    for move in range(3):
        mi, mj = moves[move_k[(ci + move) % 4]]
        if mt[i + mi][j + mj] == "#":
            continue
        sc = score
        sc += 1000 * move
        sc += 1
        if sc < visited[(ci + move) % 4][i + mi][j + mj]:
            visited[(ci + move) % 4][i + mi][j + mj] = min(
                sc, visited[(ci + move) % 4][i + mi][j + mj]
            )
            queue.append([(i + mi, j + mj), move_k[(ci + move) % 4], sc])
    mi, mj = moves[move_k[(ci - 1) % 4]]
    if mt[i + mi][j + mj] == "#":
        return queue
    sc = score
    sc += 1000
    sc += 1
    if (sc) < visited[(ci - 1) % 4][i + mi][j + mj]:
        visited[(ci - 1) % 4][i + mi][j + mj] = min(
            sc, visited[(ci - 1) % 4][i + mi][j + mj]
        )
        queue.append([(i + mi, j + mj), move_k[(ci + move) % 4], sc])
    return queue


# sort the queue by score:
queue = [(reinder, "R", 0)]
end = find_re(mt, "E")
while len(queue):
    pos, dir, score = queue.pop(0)
    cur = move_re(pos, dir, score)
    queue += cur
    queue.sort(key=lambda x: x[2])
print(visited[0][end[0]][end[1]])
print(visited[1][end[0]][end[1]])
print(visited[2][end[0]][end[1]])
print(visited[3][end[0]][end[1]])

# %%
