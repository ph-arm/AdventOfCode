"""Advent of Code 2023 - Day 24 - Part Two"""

from fractions import Fraction

test = 0
INPUT = "./input.txt"
if test:
    INPUT = "./input_sample.txt"
with open(INPUT) as fh:
    data = [line.strip() for line in fh if line.strip()]


def parse(lines):
    hail = []
    for line in lines:
        left, right = line.split("@")
        px, py, pz = (int(v) for v in left.split(","))
        vx, vy, vz = (int(v) for v in right.split(","))
        hail.append(((px, py, pz), (vx, vy, vz)))
    return hail


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def pair_rows(ha, hb):
    """Three linear rows obtained by subtracting the (P-Pi)x(V-Vi)=0 relations."""
    pa, va = ha
    pb, vb = hb
    w = sub(vb, va)  # coefficients of P via P x w
    u = sub(pb, pa)  # coefficients of V via u x V
    mp = [[0, w[2], -w[1]], [-w[2], 0, w[0]], [w[1], -w[0], 0]]
    mv = [[0, -u[2], u[1]], [u[2], 0, -u[0]], [-u[1], u[0], 0]]
    c = sub(cross(pa, va), cross(pb, vb))
    rows = [mp[k] + mv[k] for k in range(3)]
    rhs = [-c[k] for k in range(3)]
    return rows, rhs


def solve_linear(matrix, rhs):
    n = len(matrix)
    aug = [
        [Fraction(matrix[i][j]) for j in range(n)] + [Fraction(rhs[i])]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next(r for r in range(col, n) if aug[r][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [v / pv for v in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] != 0:
                factor = aug[r][col]
                aug[r] = [aug[r][k] - factor * aug[col][k] for k in range(n + 1)]
    return [aug[i][n] for i in range(n)]


def main():
    hail = parse(data)
    # Two hailstone pairs give six linear equations in (rock pos, rock vel).
    rows1, rhs1 = pair_rows(hail[0], hail[1])
    rows2, rhs2 = pair_rows(hail[0], hail[2])
    sol = solve_linear(rows1 + rows2, rhs1 + rhs2)
    return int(sol[0] + sol[1] + sol[2])


if __name__ == "__main__":
    result = main()
    if result is not None:
        print(result)
