class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter

        heap = []
        count = Counter(nums)

        for num, freq in count.items(): 
            heapq.heappush(heap, (freq, num))
            if len(heap) > k: 
                heapq.heappop(heap)
        
        result = []
        #need to unpack the heap
        for freq, num in heap: 
            result.append(num)
        return result