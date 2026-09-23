class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashmap = defaultdict(int)
        result = 0 
        max_freq = 0

        for right in range(len(s)):
            hashmap[s[right]] += 1 
            max_freq = max(max_freq, hashmap[s[right]])
            while abs(right-left+1) - max_freq > k:
                hashmap[s[left]] -= 1 
                left+=1
            result = max(result, right - left+1)
        
        return result

        