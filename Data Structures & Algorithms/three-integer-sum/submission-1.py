class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 1): 
            if nums[i] > 0: 
                break; 
            elif i > 0 and nums[i] == nums[i-1]: 
                continue
            low, high = i+1, len(nums) - 1
            while low < high: 
                currSum = nums[i] + nums[low] + nums[high]
                if currSum == 0: 
                    ans.append([nums[i], nums[low], nums[high]])
                    low = low + 1
                    high = high - 1
                    while low < high and nums[low] == nums[low - 1]: 
                        low += 1
                    while low < high and nums[low] == nums[high + 1]: 
                        high -= 1
                elif currSum < 0: 
                    low += 1
                else: 
                    high -= 1

        return ans
