class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i, n in enumerate(nums): 
            difference = target - n
            if difference in mapp: 
                return [mapp[difference], i]
            else: 
                mapp[n] = i