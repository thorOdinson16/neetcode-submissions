class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        while left <= right:
            if nums[mid] == target:
                return mid
            elif (nums[left] <= nums[mid]):
                if (target >= nums[left] and target < nums[mid]):
                    right = mid-1
                else:  
                    left = mid+1
            elif (nums[right] >= nums[mid]):
                if (target <= nums[right] and target > nums[mid]):
                    left = mid+1
                else:
                    right = mid-1
            mid = (left + right)//2
        return -1
