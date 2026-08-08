class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        current = []

        def backtrack(i):
            if i == len(nums):
                ans.append(current.copy())
                return

            # Take nums[i]
            current.append(nums[i])
            backtrack(i + 1)

            # Undo
            current.pop()

            # Don't take nums[i]
            backtrack(i + 1)

        backtrack(0)
        return ans