class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newset = set()
        for i in range(len(nums)):
            newset.add(nums[i])
        if len(newset) != len(nums):
            return True
        else:
            return False
