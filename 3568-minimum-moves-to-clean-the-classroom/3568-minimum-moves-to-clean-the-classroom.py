from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        # Find S and assign a bit to every litter cell
        litter_id = {}
        sr = sc = -1
        litter_count = 0

        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]

                if ch == 'S':
                    sr, sc = r, c
                elif ch == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1

        # No litter
        if litter_count == 0:
            return 0

        full_mask = (1 << litter_count) - 1

        # best[(r, c, mask)] = maximum energy with which
        # we have reached this state.
        best = {}

        start_key = (sr, sc, full_mask)
        best[start_key] = energy

        # BFS: (row, col, remaining_energy, mask)
        q = deque([(sr, sc, energy, full_mask)])

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        moves = 0

        while q:
            level_size = len(q)

            for _ in range(level_size):
                r, c, curr_energy, mask = q.popleft()

                # Skip an outdated state
                key = (r, c, mask)
                if best.get(key, -1) > curr_energy:
                    continue

                # All litter collected
                if mask == 0:
                    return moves

                # Cannot move when energy is zero
                if curr_energy == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # Every move costs 1 energy
                    new_energy = curr_energy - 1

                    # Reset area restores full energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # Collect litter if present
                    new_mask = mask

                    if classroom[nr][nc] == 'L':
                        bit = litter_id[(nr, nc)]
                        new_mask &= ~(1 << bit)

                    new_key = (nr, nc, new_mask)

                    # If we have already reached this position
                    # with equal or greater energy, this state
                    # can never be better.
                    if new_energy <= best.get(new_key, -1):
                        continue

                    best[new_key] = new_energy
                    q.append((nr, nc, new_energy, new_mask))

            moves += 1

        return -1