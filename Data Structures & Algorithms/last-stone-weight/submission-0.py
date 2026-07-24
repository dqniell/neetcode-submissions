class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        difference = 0

        while len(stones) > 1: 
            stones.sort()
            one = stones.pop()
            two = stones.pop()
            difference = one - two

            if difference: 
                stones.append(difference)
        
        if stones: 
            return stones[0]
        else: 
            return 0

