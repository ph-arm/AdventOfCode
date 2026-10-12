import math
from time import perf_counter

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
f = open(INPUT)
base = 20
data = list(map(str.strip, f.read().split("\n")))


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


def n_generate(elist, items):
    ordered_list = items
    other_elements = [0] * (len(elist) - (sum(items) + len(items) - 1))

    n = len(ordered_list) + len(other_elements)  # Total length of the combination
    print(n)
    print(len(other_elements))
    num_combinations = math.comb(n, len(other_elements))
    print(num_combinations)
    return 0


def process(line):
    s, items = line.split(" ")
    items = list(map(int, items.split(",")))
    c = []
    for i in s:
        if i == ".":
            c.append(0)
        elif i == "?":
            c.append(2)
        elif i == "#":
            c.append(1)
    found = 0
    sum(items) * 5
    target = sum([int(i) * (base**k) for k, i in enumerate(items * 5)])
    tries = 0
    for n in n_generate(c * 5, items * 5):
        tries += 1
        if tries % 1000000 == 0:
            print(tries)
        if n == target:
            found += 1
    return found


@profiler("recording")
def main():
    res = 0
    for line in data[:10]:
        print(line)
        res += process(line)
    print(res)


if __name__ == "__main__":
    main()
