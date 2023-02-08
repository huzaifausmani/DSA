def longestCommonPrefix(strs: list[str]) -> str:
        if len(strs) > 0: # 0 so that if list contains only one word.. will return the word
            commonPrefix = strs[0]
            for word in range(1, len(strs)):
                while True:
                    try: # Not proud of this one ;(
                        if str.index((strs[word]), commonPrefix) == 0: break 
                        else: commonPrefix = commonPrefix[:-1]
                        if len(commonPrefix) == 0 : return ""
                    except:
                        commonPrefix = commonPrefix[:-1]
            return commonPrefix                        
        else : return ""
        
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))

# Lowest run time 
# def longestCommonPrefix(self, strs: List[str]) -> str:
#         prefix = min(strs, key=len)
#         words = "not_all"
#         while words != "all":
#             words = "all"
#             for elem in strs:
#                 if prefix != elem[:len(prefix)]:
#                     prefix = prefix[:-1]
#                     words = "not_all"
            
#         return prefix



# def longestCommonPrefix(strs: list[str]) -> str:
#         if len(strs) > 0:
#             commonPrefix = strs[0]
#             for word in range(1, len(strs)):
#                 while True:
#                     print(commonPrefix, strs[word])
#                     if commonPrefix != strs[word]: commonPrefix = commonPrefix[0:len(commonPrefix) - 1]
#                     else: break
#                     if len(commonPrefix) == 0 : return ""
#             return commonPrefix                        
#         else : return ""



# def longestCommonPrefix(strs: list[str]) -> str:
#         if len(strs) > 0:
#             commonPrefix = strs[0]
#             for word in range(1, len(strs)):
#                 for character in commonPrefix:
#                     if character not in strs[word]:
#                         commonPrefix = commonPrefix.replace(character, "")
#             return commonPrefix
#         else : return ""