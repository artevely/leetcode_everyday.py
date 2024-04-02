class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charDict = dict()
        ch = 0

        for i in range(len(s)):
            if s[i] in charDict:
                ch = charDict[s[i]]
                if ch != t[i]:
                    print("false")
                    return False
            elif t[i] not in charDict.values():
                charDict[s[i]] = t[i]
            else:
                print("false")
                return False
        
        if len(s) == len(t):
            print("true")
            return True
        else:
            print("false")
            return False
    