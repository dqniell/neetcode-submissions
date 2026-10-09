class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        
        for i, j in enumerate(nums): 
            difference = target - j
            if difference in num_map:
                return [num_map[difference], i]
            else: 
                num_map[j] = i

        return []


