class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            sort = ''.join(sorted(string)) #sorted string value 
            if sort not in hashmap:
                hashmap[sort] = [] 
            hashmap[sort].append(string)
        return list(hashmap.values())

        