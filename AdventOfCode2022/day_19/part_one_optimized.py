"""Advent of Code 2022 - Day 19 - Part One (optimized)"""

import re
import sys
from queue import Queue

import numpy as np
import xxhash

test_case = False
timemax = 24


def process_state(q, states, bp, max_res, geodes_max):
    time, robots, resources = q.get()
    geodes_this_state = resources[3] + robots[3] * (timemax - time)
    if geodes_this_state > geodes_max:
        geodes_max = geodes_this_state

    # fast-forward in time to a new state where a new robot can be built
    # given collected resources and what could be built in that time interval
    # dogin this for all possible robots
    for i, cost in enumerate(bp):  # index of robot to be built
        time_needed = [0, 0, 0, 0]  # time needed to gather resources to build robot
        for j, item_cost in enumerate(cost):  # needed resources
            if item_cost:  # resouce is needed to build robot
                if (
                    item_cost <= resources[j]
                ):  # state already has enough of this resource to build robot
                    continue
                else:  # compute time needed to produce resource
                    if robots[j]:  # have robot(s) to produce resource
                        time_needed[j] = (item_cost - resources[j]) // robots[j] + int(
                            (item_cost - resources[j]) % robots[j] > 0
                        )
                    else:  # no robot to collect resource, storing a too-large time value to reject construction
                        time_needed[j] = timemax + 1
        dt = max(time_needed)  # choosing time from most time-consuming resource
        if (
            time + dt + 1 + 1 <= timemax
        ):  # resources can be gathered and robot can be built in available time
            # and new robot will have time to do something (+1 minute), otherwise useless
            # collect resources with initially available robots, spend to build new robot
            resources_new = resources + (dt + 1) * robots - cost
            # build new robot
            robots_new = np.copy(robots)
            robots_new[i] += 1

            # OPTIMISATIONS: The code converges to the correct results even without these optimisations,
            # but the search space becomes bery large and the execution time very slow...

            # 1) If it takes N resources to build a robot, it's usess to have M>N robots collecting that resource
            # so I can speed-up the process by avoiding to re-enque states with too many useless robots.
            # This is enough to solve Part 1 in a decent time
            if not (robots_new <= max_res)[:3].all():  # do not consider geodes
                continue

            # 2) Let's imagine that from next round only geodes robots will be added to this state (regardless
            # of whether this is possible in term of resources). If even in this overoptimistic conditions the
            # state cannot produce more geodes than the current maximum, it's useless to re-enque this state
            timeleft = timemax - (time + dt + 1)
            geodes_new_ideal = (
                (timeleft - 1) * (timeleft) // 2
            )  # triangular number for timeleft-1, since geodes
            # built at last minute cannot build anything
            geodes_final_ideal = (
                resources_new[3] + timeleft * robots_new[3] + geodes_new_ideal
            )
            if geodes_final_ideal <= geodes_max:
                continue

            # re-enque new state
            state_new = (time + dt + 1, robots_new, resources_new)
            h = xxhash.xxh64()
            # h.update(state_new[0].to_bytes(32, sys.byteorder))
            h.update(state_new[0].tobytes(order="C"))
            h.update(state_new[1])
            h.update(state_new[2])
            if states.get(h.intdigest(), 1):
                q.put(state_new)
                states[h.intdigest()] = 0
    return geodes_max


def max_geodes(bp, timemax=24):
    # compute the minimum amount of each resource needed to build any robot
    max_res = np.zeros(4, dtype=int)
    for cost in bp:
        for j in range(len(cost)):
            if cost[j] > max_res[j]:
                max_res[j] = cost[j]

    # initial state
    robots = np.array([1, 0, 0, 0], dtype=int)
    resources = np.array([0, 0, 0, 0], dtype=int)
    time = 0
    start = (time, robots, resources)

    # BFS-like search of state evolutions
    states = {}
    h = xxhash.xxh64()
    h.update(start[0].to_bytes(32, sys.byteorder))
    h.update(start[1])
    h.update(start[2])
    geodes_max = 0
    q = Queue()
    q.put(start)

    while not q.empty():
        geodes_max = process_state(q, states, bp, max_res, geodes_max)
    return geodes_max


def main():
    ###### START ########
    file = open("./input.txt")
    if test_case:
        file.close()
        file = open("./test_input.txt")
    content = file.read().split("\n")

    def format_line(line):
        line_items = re.findall("[0-9]+", line)
        return line_items[1:]

    items = tuple(map(format_line, content))
    bps = []
    for item in items:
        vals = list(map(int, item))
        # just the first parameter for now
        price = {}
        price["ore"] = np.array([vals[0], 0, 0, 0], dtype=int)
        price["clay"] = np.array([vals[1], 0, 0, 0], dtype=int)
        price["obsidian"] = np.array([vals[2], vals[3], 0, 0], dtype=int)
        price["geode"] = np.array([vals[4], 0, vals[5], 0], dtype=int)
        bps.append(price.values())
    q = 0
    for i, bp in enumerate(bps):
        g = max_geodes(bp, 24)
        print(f"| {i + 1:9d} | {g:11d} | {(i + 1) * g:7d} | ")
        q += (i + 1) * g
    print(f"\n Sum quality levels: {q}")


if __name__ == "__main__":
    main()
