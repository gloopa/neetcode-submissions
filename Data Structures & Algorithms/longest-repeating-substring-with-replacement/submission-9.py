class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        left = 0
        count = 0
        occ =0
        for right in range(len(s)):
            freqs[s[right]] += 1 
            occ = max(occ, freqs[s[right]])
            while (right-left+1) - occ > k:
                freqs[s[left]]-= 1 
                left+=1
            count = max(count, right-left+1)
        return count


            

        
        