class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums): 
            looking_for = target - num
            if num in nums_dict: 
                return [nums_dict[num], i]
            nums_dict[looking_for] = i