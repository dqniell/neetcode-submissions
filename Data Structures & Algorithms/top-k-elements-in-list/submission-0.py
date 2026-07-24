from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []

        #most_common() returns a tuple, hence the num, freq
        for num, freq in count.most_common(k):
            #just append the number
            result.append(num)

        return result