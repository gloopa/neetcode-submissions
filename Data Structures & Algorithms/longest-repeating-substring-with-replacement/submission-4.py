class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        left = 0
        length = 0
        max_sum = 0
        for right in range(len(s)):
            hashmap[s[right]] += 1 
            max_sum = max(max_sum, hashmap[s[right]])
            while abs(right-left+1) - max_sum > k:
                hashmap[s[left]] -= 1 
                left+=1
            length = max(length, abs(right-left+1))
        return length
        