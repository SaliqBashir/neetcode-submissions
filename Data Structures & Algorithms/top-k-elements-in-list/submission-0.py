class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        times = {}
        for element in nums:

            if element not in times:
                times[element] = 0
            
            times[element] += 1

        items = sorted(times.items(), key=lambda x: x[1], reverse=True)
        output = []
        for i in range(k):
            output.append(items[i][0])
        return output