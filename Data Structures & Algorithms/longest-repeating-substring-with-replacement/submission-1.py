class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_freq = 0 
        left = 0
        length = 0

        for right in range(len(s)):
            freq[s[right]] += 1 
            max_freq = max(max_freq, freq[s[right]])
            while (right - left+1) - max_freq > k: 
                freq[s[left]]-=1
                left+=1 
            length = max(length, right-left+1)
            
        
        return length

                

        
