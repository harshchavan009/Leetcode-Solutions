class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node.children:
                return

            nxt = node.children[ch]

            # Found a complete word
            if nxt.word is not None:
                result.append(nxt.word)
                nxt.word = None  # avoid duplicates

            # Mark cell as visited
            board[r][c] = '#'

            if r > 0 and board[r - 1][c] != '#':
                dfs(r - 1, c, nxt)

            if r + 1 < rows and board[r + 1][c] != '#':
                dfs(r + 1, c, nxt)

            if c > 0 and board[r][c - 1] != '#':
                dfs(r, c - 1, nxt)

            if c + 1 < cols and board[r][c + 1] != '#':
                dfs(r, c + 1, nxt)

            # Restore cell
            board[r][c] = ch

            # Trie pruning
            if not nxt.children and nxt.word is None:
                del node.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result