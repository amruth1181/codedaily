class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        for i in range(k):
            if s[i] in ("a", "e", "i", "o", "u"):
                count += 1
        maxc = count
        for i in range(1, len(s) - k + 1):
            if s[i + k - 1] in ("a", "e", "i", "o", "u"):
                count += 1
            if s[i - 1] in ("a", "e", "i", "o", "u"):
                count -= 1
            if count > maxc:
                maxc = count

        return maxc


