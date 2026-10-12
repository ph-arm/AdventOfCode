"""Advent of Code 2024 - Day 16 - Part Two"""

import heapq

from shared import *

INF = 1 << 60
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left


def main():
    start_cell = find_re(mt, "S")
    end_cell = find_re(mt, "E")
    assert start_cell is not None and end_cell is not None

    # Dijkstra over (row, col, facing): a step forward costs 1, a turn costs 1000.
    start_state = (start_cell[0], start_cell[1], 1)  # facing east
    best_cost: dict[tuple[int, int, int], int] = {start_state: 0}
    priority_queue: list[tuple[int, tuple[int, int, int]]] = [(0, start_state)]
    while priority_queue:
        cost, (row, col, facing) = heapq.heappop(priority_queue)
        if cost > best_cost.get((row, col, facing), INF):
            continue
        next_row = row + DIRECTIONS[facing][0]
        next_col = col + DIRECTIONS[facing][1]
        neighbors = [
            (cost + 1000, (row, col, (facing + 1) % 4)),
            (cost + 1000, (row, col, (facing - 1) % 4)),
        ]
        if mt[next_row][next_col] != "#":
            neighbors.append((cost + 1, (next_row, next_col, facing)))
        for next_cost, next_state in neighbors:
            if next_cost < best_cost.get(next_state, INF):
                best_cost[next_state] = next_cost
                heapq.heappush(priority_queue, (next_cost, next_state))

    end_row, end_col = end_cell
    best_score = min(
        best_cost.get((end_row, end_col, facing), INF) for facing in range(4)
    )

    # Walk the shortest-path DAG backwards from every optimal end state and
    # gather the tiles that lie on at least one best path.
    on_best_path = {
        (end_row, end_col, facing)
        for facing in range(4)
        if best_cost.get((end_row, end_col, facing)) == best_score
    }
    to_visit = list(on_best_path)
    while to_visit:
        row, col, facing = to_visit.pop()
        state_cost = best_cost[(row, col, facing)]
        prev_row = row - DIRECTIONS[facing][0]
        prev_col = col - DIRECTIONS[facing][1]
        predecessors = (
            ((row, col, (facing + 1) % 4), 1000),  # undo a turn
            ((row, col, (facing - 1) % 4), 1000),
            ((prev_row, prev_col, facing), 1),  # undo a forward step
        )
        for prev_state, step_cost in predecessors:
            if (
                prev_state not in on_best_path
                and best_cost.get(prev_state, INF) + step_cost == state_cost
            ):
                on_best_path.add(prev_state)
                to_visit.append(prev_state)

    return len({(row, col) for row, col, _facing in on_best_path})


if __name__ == "__main__":
    print(main())
