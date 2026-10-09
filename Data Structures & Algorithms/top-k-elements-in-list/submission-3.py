class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #given an array nums and an integer k, i need to return the k most frequent elemetns in the array
        #i can output the array in any order
        #willl the array ever be empty? 

        #so to keep track of the k most frequent elements: 
            #[1, 2, 2, 2,]
            #i can probably use Python's Counter library, where it returns element:Count, in sorted order


        from collections import Counter

        count = Counter(nums)
        most_common = count.most_common(k)

        result = []
        for num, freq in most_common: 
            result.append(num)

        return result

