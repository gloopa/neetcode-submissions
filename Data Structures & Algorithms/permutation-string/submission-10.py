class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freqs = Counter(s1) 
        k = len(s1)
        s2freqs = Counter()
        left = 0 

        for right in range(len(s2)): 
            s2freqs[s2[right]] += 1 

            if right - left + 1 > k:
                s2freqs[s2[left]] -= 1
                if s2freqs[s2[left]] == 0:
                    del s2freqs[s2[left]]
                left+=1 

            
            if right - left + 1 == k and s1freqs == s2freqs:
                return True 
            
        
        return False

        