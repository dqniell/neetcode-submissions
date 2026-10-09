class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #i am given an array of ints
        #i need to return the length of the longest consecutive sequence of elements that can be formed
        # [2, 20, 4, 10, 3, 4, 5]
        # [2, 3, 4, 5] -> 4

        #will the array ever be empty?
        #will the array always contain an answer?

        #here is what im thinking: 
            #a consecutive number means back to back, so like 2, 3, 4
            #for that to happen, if its the start of a sequence, (i-1) dne, (i+1) exists
                #we can probably just check to see if there is a (i-1) or (i+1)
            #i can use a set to do o(1) lookup

        numSet = set(nums)
        longest = 0

        for num in numSet: 
            if (num - 1) not in numSet: 
                #start of a sequence
                length = 1
                while (num + length) in numSet: 
                    length += 1
                longest = max(length, longest)
        return longest

        
