def isPalindrome(nmb, i, j):
    return str(nmb)[i - 1:j] == ''.join(reversed(list(str(nmb)[i - 1:j])))
    
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
                n = a * 100001 + b * 10010 + c * 1100   #a*100000 + b*10000 + c*1000 + c*100 + b*10 + a
                if n > 999999:
                    c = 10
                elif isPalindrome(n - 3, 2, 6) and isPalindrome(n - 2, 2, 6) and isPalindrome(n - 1, 2, 4):
                    print(n - 3)
