class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordGraph = {word: [] for word in wordList}
        wordGraph[beginWord] = []
        
        wordSet: set[str] = set(wordList)
        wordSet.add(beginWord)
        
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for word in wordSet:
            for i in range(len(word)):
                pre, curr, post = word[:i], word[i], word[i+1:]
                for letter in letters:
                    newWord = word[:i] + letter + word[i+1:]
                    if newWord != word and newWord in wordSet:
                        wordGraph[word].append(newWord)
        print(wordGraph)
        
        q = deque()
        q.append((beginWord, 1))
        seen: set[str] = set()
        seen.add(curr)
        while q:
            curr, size = q.popleft()
            if curr == endWord:
                return size
            for nxt in wordGraph[curr]:
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, size + 1))
                
        
        return 0


