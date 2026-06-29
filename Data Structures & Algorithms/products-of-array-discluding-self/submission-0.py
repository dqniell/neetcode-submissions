class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)): 
            left = 0
            right = len(nums) - 1
            preProduct = 1
            postProduct = 1
            while left < i: 
                preProduct *= nums[left]
                left += 1
            while right > i: 
                postProduct *= nums[right]
                right -= 1
            result.append(preProduct * postProduct)
        return result