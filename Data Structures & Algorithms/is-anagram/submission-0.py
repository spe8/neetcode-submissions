class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydictA = dict()
        mydictB = dict()
        for char in s:
            if char not in mydictA:
                mydictA[char] = 0
            mydictA[char] += 1
        for char in t:
            if char not in mydictB:
                mydictB[char] = 0
            mydictB[char] += 1
        if mydictA == mydictB:
            return True
        else:
            return False
            
        