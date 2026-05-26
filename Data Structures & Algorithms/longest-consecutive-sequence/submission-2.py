class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        currentstreak = 0
        maxstreak = 0
        for num in nums:
            if  num-1 not in nums:
                currentstreak = 1
                while num+currentstreak in nums:
                    currentstreak +=1
                maxstreak = max(currentstreak,maxstreak)
        return maxstreak


            
