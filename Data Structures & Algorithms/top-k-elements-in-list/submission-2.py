import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        
        #iterate through count.items() bc that contains the num:count of Counter
        for num, freq in count.items():
            #push it onto the heap
            heapq.heappush(heap, (freq, num))
            
            #if the length of the heap is greater than k, we are no longer tracking top k, 
            #so we need to pop the smallest k
            if len(heap) > k:
                heapq.heappop(heap)
        
        #printing out the result
        result = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)
        
        return result