class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        clones = {}

        def dfs(current):
            if current in clones:
                return clones[current]

            # Create a copy of the current node
            copy = Node(current.val)
            clones[current] = copy

            # Clone all neighbors
            for neighbor in current.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)