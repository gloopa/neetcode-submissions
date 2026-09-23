class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} #key: sorted string value: associated strings within strs 
        for string in strs:
            sort = ''.join(sorted(string))
            if sort not in anagrams:
                anagrams[sort]= [] #empty 
            anagrams[sort].append(string) 
        return list(anagrams.values())



        