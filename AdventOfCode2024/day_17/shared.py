"""Advent of Code 2024 - Day 17 - Shared input & utilities"""

test = 1

register = [0, 0, 0]
prog = []


def v_mode(v):
    if v < 4:
        return v
    else:
        return register[v - 4]


def op_0(b):
    a = register[0]
    oper = v_mode(b)
    register[0] = a // (2**oper)


def op_1(b):
    register[1] = register[1] ^ b


def op_2(b):
    register[1] = v_mode(b) % 8


def op_3(b):
    global pointer
    if register[0]:
        pointer = b


def op_4(b):
    register[1] = register[1] ^ register[2]


def op_5(b):
    output.append(v_mode(b) % 8)


def op_6(b):
    a = register[0]
    oper = v_mode(b)
    register[1] = a // (2**oper)


def op_7(b):
    a = register[0]
    oper = v_mode(b)
    register[2] = a // (2**oper)


ops = [op_0, op_1, op_2, op_3, op_4, op_5, op_6, op_7]


def run():
    global output
    output = []
    turn = 0
    global pointer
    pointer = 0
    try:
        while pointer < len(prog):
            turn += 1
            op = prog[pointer]
            b = prog[pointer + 1]
            pointer += 2
            ops[op](b)
            if turn % 100 == 0:
                print(turn)
    except Exception:
        print(f"turn:{turn}")
        print(f"pointer:{pointer}")
        print(f"register:{register}")
        print(f"len prog:{len(prog)}")

    print(output)


# tests
# If register C contains 9, the program 2,6 would set register B to 1.
register[2] = 9
ops[2](6)
res = register[1] == 1
if not res:
    print("test failed-1")
# If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
register[0] = 10
prog = [5, 0, 5, 1, 5, 4]
run()
res = output == [0, 1, 2]
if not res:
    print("test failed-2")

# If register A contains 2024, the program 0,1,5,4,3,0 would output
# 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
register[0] = 2024
prog = [0, 1, 5, 4, 3, 0]
run()
res = output == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0] and register[0] == 0
if not res:
    print(output)
    print(register[0])
    print("test failed-3")
# If register B contains 29, the program 1,7 would set register B to 26.
register[1] = 29
ops[1](7)
res = register[1] == 26
if not res:
    print("test failed-4")

# If register B contains 2024 and register C contains 43690, the program
# the program 4,0 would set register B to 44354.
register[1] = 2024
register[2] = 43690
ops[4](0)
res = register[1] == 44354
if not res:
    print("test failed-5")

# so op 1/2/4 are good.
