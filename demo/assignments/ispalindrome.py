def ispalindrome(s):
    return s == s[::-1]


print(ispalindrome('abc'), ispalindrome('abba'))
