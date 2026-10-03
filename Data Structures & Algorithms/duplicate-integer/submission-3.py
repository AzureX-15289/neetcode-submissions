class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        for i in nums:
            if i in hashTable:
                return True
            else: 
                hashTable[i]  = 1
        return False
        