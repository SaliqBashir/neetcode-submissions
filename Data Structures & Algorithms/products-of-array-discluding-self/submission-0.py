class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        product = 1
        for i in range(len(nums)):
            output[i] = 1
            for j in range(len(nums)):
                if i == j:
                    pass
                else:
                    output[i] *= nums[j]
        return output
                    