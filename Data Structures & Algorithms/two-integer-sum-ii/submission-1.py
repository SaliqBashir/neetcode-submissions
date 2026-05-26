class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in numbers:
                j = numbers.index(complement)
                if i < j:
                    break
        if i > j:
            return
        i += 1
        j += 1
        result.extend([i, j])
        return result