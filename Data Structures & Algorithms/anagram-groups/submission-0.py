class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            sort = ''.join(sorted(string))
            if sort not in anagrams:
                anagrams[sort] = []
            anagrams[sort].append(string)
        return list(anagrams.values())
            

        