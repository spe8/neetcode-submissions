class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            current = nums[i]
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[nums[i]] = i