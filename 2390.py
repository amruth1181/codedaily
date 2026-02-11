class Solution:
    def removeStars(self, s: str) -> str:
        sti = list(s)

        e = []
        for i in range(len(s)):
            if sti[i] != '*':
                e.append(sti[i])
            else:
                e.pop()

        return "".join(e)