from collections import defaultdict
from heapq import heappop, heappush
from time import perf_counter

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
base = 20
# data = list(map(str.strip, f.read().split("\n")))
data = [list(map(int, list(line))) for line in f.read().split("\n")]


def profiler(s: str):
    def decorator(method):
        print(s)

        def wrapper_method(*arg, **kw):
            t = perf_counter()
            ret = method(*arg, **kw)
            print(
                "Method "
                + method.__name__
                + " took : "
                + f"{perf_counter() - t:2.5f}"
                + " sec"
            )
            return ret

        return wrapper_method

    return decorator


def process_item(item, res, data, maxl):
    x, y, d, r, c, t = item
    t = t.copy()
    t.append((x, y))
    if d == 1:  # right
        if x + 1 < len(data[0]):
            if (data[y][x + 1] + c) >= maxl:
                return []
            if res[y, x + 1][d, r + 1] <= (data[y][x + 1] + c):
                return []
            res[y, x + 1][d, r + 1] = data[y][x + 1] + c
            return [[data[y][x + 1] + c, x + 1, y, 1, r + 1, data[y][x + 1] + c, t]]

    if d == 2:  # down
        if y + 1 < len(data):
            if (data[y + 1][x] + c) >= maxl:
                return []
            if res[y + 1, x][d, r + 1] <= (data[y + 1][x] + c):
                return []
            res[y + 1, x][d, r + 1] = data[y + 1][x] + c
            return [[data[y + 1][x] + c, x, y + 1, 2, r + 1, data[y + 1][x] + c, t]]

    if d == 4:  # left
        if x - 1 >= 0:
            if (data[y][x - 1] + c) >= maxl:
                return []
            if res[y, x - 1][d, r + 1] <= (data[y][x - 1] + c):
                return []
            res[y, x - 1][d, r + 1] = data[y][x - 1] + c
            return [[data[y][x - 1] + c, x - 1, y, 4, r + 1, data[y][x - 1] + c, t]]

    if d == 8:  # up
        if y - 1 >= 0:
            if (data[y - 1][x] + c) >= maxl:
                return []
            if res[y - 1, x][d, r + 1] <= (data[y - 1][x] + c):
                return []
            res[y - 1, x][d, r + 1] = data[y - 1][x] + c
            return [[data[y - 1][x] + c, x, y - 1, 8, r + 1, data[y - 1][x] + c, t]]
    return []


def process_dec(item, res, data, maxl):
    maxll = maxl
    c, x, y, d, r, c, t = item
    q = []
    for i in [1, 2, 4, 8]:
        if i & d and r == 3:
            continue
        if i & d:
            q += process_item((x, y, i, r, c, t), res, data, maxl)
            continue
        if d == 1 and i == 4:
            continue
        if d == 2 and i == 8:
            continue
        if d == 4 and i == 1:
            continue
        if d == 8 and i == 2:
            continue
        q += process_item((x, y, i, 0, c, t), res, data, maxl)

    for i in q:
        if i[1] == (len(data[0]) - 1) and i[2] == (len(data) - 1) and i[0] < maxll:
            maxll = i[0]
    return q, maxll


def process_input(data):
    # x,y,dir,rec dir, current lost
    queue = [
        [0, 0, 0, 1, 0, 0, []],
        [0, 0, 0, 2, 0, 0, []],
    ]  # x:0 ,y:0, r:1 d:2,l:4,u:8
    maxl = 0
    for i in range(1, len(data)):
        maxl += data[i][i] + data[i - 1][i]
    res = defaultdict(lambda: defaultdict(lambda: maxl))
    c = 0
    while 1:
        item = heappop(queue)
        n, maxl = process_dec(item, res, data, maxl)
        for neighbor in n:
            heappush(queue, neighbor)
        if queue == []:
            break
        if c % 1000000 == 0:
            print(maxl)
            print(len(queue))
            print(queue[-1])
        c += 1
    return maxl


@profiler("recording")
def main():
    res = process_input(data)
    print(f"score {res}")


if __name__ == "__main__":
    main()
