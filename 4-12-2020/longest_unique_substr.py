'''
Date: 4/12/2020
By: ApplesHaveFeelings

URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''

def lengthOfLongestSubstring (string):
    maxSubString = ""
    currSubString = ""
    for i in range(0,len(string)-1):
        if (len(string) - i < len(maxSubString)): return len(maxSubString)
        currSubString+=string[i]#put first letter in currSubString
        for j in range(i+1,len(string)):
          if string[j] not in currSubString: 
            currSubString+=string[j]
            print("currSubString is {}".format(currSubString))
          else:
            if len(currSubString) > len(maxSubString):
                maxSubString = currSubString
            currSubString = ""
            break
          if j == len(string)-1: return len(currSubString)
        print()
    print("maxSubString is {}".format(maxSubString))

    return len(maxSubString)
          
print(lengthOfLongestSubstring("abcalmoqrsabcaa"))
