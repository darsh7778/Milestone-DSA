def palindrome(left, right, s):
    if left >= right:
        return True
    
    if s[left] != s[right]:
        return False
    
    return palindrome(left+1, right-1, s)

s = ['n', 'i', 't', 'i', 'n']
n = len(s) -1
result = palindrome(0, n, s)
print(result)