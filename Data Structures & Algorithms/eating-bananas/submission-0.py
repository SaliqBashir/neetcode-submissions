from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = high
        while low <= high:
            mid = low + (high - low) // 2
            hours = 0
            for i in range(len(piles)):
                hours += ceil(piles[i]/mid)
            if hours <= h:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result