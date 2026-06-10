class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = []
        for i in range(len(temperatures)):
            maxTemp = temperatures[i]
            found = False
            for j in range(i, len(temperatures)):
                if temperatures[j] > maxTemp:
                    maxTemp = temperatures[j]
                    results.append(j - i)
                    found = True
                    break
            if not found:
                results.append(0)
        return results