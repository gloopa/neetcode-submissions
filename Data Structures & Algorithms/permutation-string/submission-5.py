class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        word = Counter(s1)
        res = ""
        chars = set(s1)
        left = 0
        count = 0
        isvalid = False 
        for right in range(len(s2)):
            if right - left + 1 == len(s1):
                if Counter(s2[left:right+1]) == word:
                    return True
                else:
                    left+=1 
            
        return False



           






        



