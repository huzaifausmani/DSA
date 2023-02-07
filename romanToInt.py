def romanToInt(s: str) -> int:
        mapping, toReturn, i = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }, 0, 0
        while not(i >= len(s)):
            if i == len(s) - 1: return toReturn + mapping[s[i]]
            if mapping[s[i]] < mapping[s[i + 1]]:
                toReturn = toReturn + (mapping[s[i + 1]] - mapping[s[i]])
                i = i + 2
            else:
                toReturn = toReturn + mapping[s[i]]
                i = i + 1
            if i >= len(s): return toReturn
        return toReturn

print(romanToInt("CD"))