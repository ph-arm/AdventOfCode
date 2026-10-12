"""Advent of Code 2024 - Day 23 - Part Two"""

from shared import *


def main():
    def check_cand(c, set_keys):
        for i in set_keys:
            if c not in conn[i]:
                return False
        return True

    def expand(set_key):
        c = list(set_key)[0]
        result = set()
        for i in conn[c]:
            if i not in set_key and check_cand(i, set_key):
                curr = list(set_key)
                curr.append(i)
                curr.sort()
                result.add(tuple(curr))
        return result

    # Rebuild triangles (same logic as part_one)
    res = set()
    for i in conn.keys():
        for connec in conn[i]:
            for j in conn[connec]:
                if i in conn[j]:
                    f = [i, j, connec]
                    f.sort()
                    res.add(tuple(f))

    curr = set(res)

    ll = 3
    while 1:
        next_curr = set()
        for item in curr:
            expanded = expand(item)
            if expanded:
                next_curr.update(expanded)
        if not next_curr:
            break
        curr = next_curr
        ll += 1
    return ",".join(sorted(list(curr)[0]))


if __name__ == "__main__":
    print(main())
