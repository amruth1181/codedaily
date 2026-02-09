from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count = Counter(list(word1))
        count2 = Counter(list(word2))
        if count.keys() != count2.keys():
            return False
        return sorted(count.values()) == sorted(count2.values())
