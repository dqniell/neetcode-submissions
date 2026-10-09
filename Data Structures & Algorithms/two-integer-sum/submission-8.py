class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        #{needed complement : index of current number}
        for i, num in enumerate(nums): 
            difference = target - num
            if num in nums_dict: #means that there already is a complement
                return [nums_dict[num], i]
            nums_dict[difference] = i