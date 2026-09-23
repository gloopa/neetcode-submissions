class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for string in strs:
            sort = ''.join(sorted(string))
            if sort not in seen:
                seen[sort] = [] #doesnt have anagram yet  
            seen[sort].append(string) 
        
        return list(seen.values())

        