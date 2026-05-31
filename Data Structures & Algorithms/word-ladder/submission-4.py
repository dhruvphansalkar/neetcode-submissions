from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet: set[str] = set(wordList)

        if endWord not in wordSet:
            return 0

        letters = "abcdefghijklmnopqrstuvwxyz"

        q = deque([(beginWord, 1)])
        seen: set[str] = {beginWord}

        while q:
            word, length = q.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                pre = word[:i]
                post = word[i + 1:]

                for letter in letters:
                    newWord = pre + letter + post

                    if newWord in wordSet and newWord not in seen:
                        seen.add(newWord)
                        q.append((newWord, length + 1))

        return 0