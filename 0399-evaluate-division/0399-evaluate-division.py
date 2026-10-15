class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}

        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}

            graph[a][b] = value
            graph[b][a] = 1.0 / value

        def calculate(start, end):
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            stack = [(start, 1.0)]
            visited = set()

            while stack:
                node, product = stack.pop()

                if node == end:
                    return product

                if node in visited:
                    continue

                visited.add(node)

                for neighbor, value in graph[node].items():
                    if neighbor not in visited:
                        stack.append((neighbor, product * value))

            return -1.0

        return [calculate(a, b) for a, b in queries]