class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #given an array nums and an integer k, i need to return the k most frequent elemetns in the array
        #i can output the array in any order
        #willl the array ever be empty? 

        #we can use a heap! 
        #since heaps of size k can store the smallest k at a given time when we itertae trough the array
        #do we want to use a min heap or a max heap? 
        #breakdown what they both do
            #a min heap keeeps the smallest on top, max opposite
            #what do we need in this problem? for efficincy, we want to be able to pop off the smallest and add another
            #so we need a min heap! 

        import heapq

        count = {}
        for num in nums: 
            if num in count: 
                count[num] +=1 
            else: 
                count[num] = 1
        
        heap = []
        for num in count.keys(): 
            heapq.heappush(heap, (count[num], num)) #push in that order since we want to compare by freq
            if len(heap) > k: 
                heapq.heappop(heap)

        result = []
        for i in range(k): 
            result.append(heapq.heappop(heap)[1]) #takes second item
        return result

        

