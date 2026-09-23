class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} #key: sorted, value(s): word in strs
        for string in strs: 
            sort = ''.join(sorted(string)) # sorted value 
            if sort not in hashmap:
                hashmap[sort] = [] 
            hashmap[sort].append(string)
        
        return list(hashmap.values())


        
        