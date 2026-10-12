"""Advent of Code 2023 - Day 24 - Part One"""

test = 0
if test:
    INPUT = "./input_sample.txt"
    LOW, HIGH = 7, 27
else:
    INPUT = "./input.txt"
    LOW, HIGH = 200000000000000, 400000000000000
with open(INPUT) as fh:
    data = [line.strip() for line in fh if line.strip()]


def parse(lines):
    hail = []
    for line in lines:
        left, right = line.split("@")
        px, py, pz = (int(v) for v in left.split(","))
        vx, vy, vz = (int(v) for v in right.split(","))
        hail.append((px, py, pz, vx, vy, vz))
    return hail


def crosses(a, b, lo, hi):
    """True if the 2D forward paths of a and b meet inside [lo, hi]^2."""
    ax, ay, _, avx, avy, _ = a
    bx, by, _, bvx, bvy, _ = b
    det = avy * bvx - avx * bvy
    if det == 0:  # parallel
        return False
    dx, dy = bx - ax, by - ay
    t = (bvx * dy - bvy * dx) / det
    s = (avx * dy - avy * dx) / det
    if t < 0 or s < 0:  # crossing in the past for either stone
        return False
    x = ax + t * avx
    y = ay + t * avy
    return lo <= x <= hi and lo <= y <= hi


def main():
    hail = parse(data)
    count = 0
    for i in range(len(hail)):
        for j in range(i + 1, len(hail)):
            if crosses(hail[i], hail[j], LOW, HIGH):
                count += 1
    return count


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
