class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        visited = set(beginWord)

        while queue:
            curr_word, length = queue.popleft()

            for i in range(len(curr_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = curr_word[:i] + c + curr_word[i+1:]

                    if next_word == endWord:
                        return length + 1

                    if next_word in wordSet and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, length + 1))

        return 0