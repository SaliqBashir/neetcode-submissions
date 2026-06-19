class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        cut = low

        low = 0
        high = cut - 1
        while low <= high:
            mid = low + (high - low) //2

            if nums[mid] == target:
                flag = True
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        low = cut
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1