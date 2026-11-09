import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
     
        bit = [0] * (k + 1)

        for i in range(1, k + 1):
            bit[i] = i & -i

        def update(i, delta):
            i += 1
            while i <= k:
                bit[i] += delta
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total
        def find_kth(target):
            idx = 0
            step = 1 << (k.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= k and bit[nxt] < target:
                    idx = nxt
                    target -= bit[nxt]

                step >>= 1

            return idx

        busy = []

        handled = [0] * k

        for i in range(len(arrival)):

            while busy and busy[0][0] <= arrival[i]:
                finish, server = heapq.heappop(busy)
                update(server, 1)
            total = query(k)

            if total == 0:
                continue

            start = i % k
            before = query(start)
            if total > before:
                server = find_kth(before + 1)
            else:
                server = find_kth(1)
            update(server, -1)
            handled[server] += 1
            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )
        maximum = max(handled)

        return [
            i for i in range(k)
            if handled[i] == maximum
        ]