class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        length = 0
        max_freq = 0 
        left = 0


        for right in range(len(s)):
            mp[s[right]] += 1 
            max_freq = max(max_freq, mp[s[right]])
            while abs(right-left+1) - max_freq > k:
                mp[s[left]] -=1
                left+=1 
            length = max(length, abs(right-left+1))
        return length 



        