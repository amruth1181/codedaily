from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        counts = Counter(arr)
        return len(counts) == len(set(counts.values()))


def uniqueOccurrences(arr):
    # Count occurrences of each value
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1

    # Check if all occurrence counts are unique
    occurrences = list(count.values())
    return len(occurrences) == len(set(occurrences))