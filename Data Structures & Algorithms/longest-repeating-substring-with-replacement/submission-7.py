class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        left = 0
        length = 0
        max_occ = 0 

        for right in range(len(s)):
            hashmap[s[right]] += 1
            max_occ = max(max_occ, hashmap[s[right]])
            while (right-left+1) - max_occ > k:
                hashmap[s[left]]-=1
                left+=1
            length = max(length, right-left+1)
        
        return length
        