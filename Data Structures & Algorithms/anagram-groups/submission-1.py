class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        for word in strs:
            ns = ''.join(sorted(word))
            if ns not in hash_map:
                hash_map[ns] = []
            hash_map[ns].append(word)
        return list(hash_map.values())
        