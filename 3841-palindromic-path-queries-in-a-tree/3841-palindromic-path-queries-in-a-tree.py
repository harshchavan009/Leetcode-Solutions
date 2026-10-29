class Solution:
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        suneravilo = (n, edges, s, queries)

        LOG = n.bit_length()
        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        path_xor = [0] * n

        # Iterative DFS to avoid recursion-depth errors
        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            node, par, state = stack.pop()

            if state == 0:
                parent[node] = par
                tin[node] = timer
                timer += 1

                bit = 1 << (ord(s[node]) - ord('a'))
                path_xor[node] = (
                    (path_xor[par] if par != -1 else 0) ^ bit
                )

                stack.append((node, par, 1))

                for nei in reversed(graph[node]):
                    if nei != par:
                        depth[nei] = depth[node] + 1
                        stack.append((nei, node, 0))
            else:
                tout[node] = timer - 1

        # Binary lifting table for LCA
        up = [[0] * n for _ in range(LOG)]
        up[0] = [
            parent[i] if parent[i] != -1 else i
            for i in range(n)
        ]

        for j in range(1, LOG):
            prev = up[j - 1]
            curr = up[j]

            for i in range(n):
                curr[i] = prev[prev[i]]

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            j = 0

            while diff:
                if diff & 1:
                    u = up[j][u]
                diff >>= 1
                j += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return up[0][u]

        # Fenwick tree supporting range XOR updates
        bit_tree = [0] * (n + 2)

        def bit_update(i, value):
            while i < len(bit_tree):
                bit_tree[i] ^= value
                i += i & -i

        def bit_query(i):
            result = 0

            while i > 0:
                result ^= bit_tree[i]
                i -= i & -i

            return result

        chars = list(s)
        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(new_char) - ord('a'))
                change = old_mask ^ new_mask

                if change:
                    chars[u] = new_char

                    # Update the XOR masks of all nodes in u's subtree
                    bit_update(tin[u] + 1, change)
                    bit_update(tout[u] + 2, change)

            else:
                u = int(parts[1])
                v = int(parts[2])

                lca = get_lca(u, v)

                # Current root-to-node XOR masks
                mask_u = path_xor[u] ^ bit_query(tin[u] + 1)
                mask_v = path_xor[v] ^ bit_query(tin[v] + 1)

                # XOR mask of the complete path, including the LCA
                lca_mask = 1 << (ord(chars[lca]) - ord('a'))
                mask = mask_u ^ mask_v ^ lca_mask

                # At most one character may occur an odd number of times
                answer.append((mask & (mask - 1)) == 0)

        return answer