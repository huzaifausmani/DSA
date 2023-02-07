# mine
def isPalindrome(x: int):
    for i in range(int(len(str(x))/2)):
        if str(x)[i] != str(x)[len(str(x)) - (i + 1)]:
            return False
    return True

# memory 
def isPalindrome(self, x: int) -> bool:
    if x<0:
        return False
    inputNum = x
    newNum = 0
    while x>0:
        newNum = newNum * 10 + x%10
        x = x//10
    return newNum == inputNum

# runtime
def isPalindrome(self, x: int) -> bool:
    x=str(x)
    if x==x[::-1]:
        return True
    return False