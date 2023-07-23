def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    p = 0
    l = len(s)
    ans = 0
    while p < l:
        if s[p] == "I":
            if (p + 1 < l) and (s[p + 1] == "V"):
                ans += 4
                p += 1
            elif (p + 1 < l) and (s[p + 1] == "X"):
                ans += 9
                p += 1
            else:
                ans += 1
        elif s[p] == "V":
            ans += 5
        elif s[p] == "X":
            if (p + 1 < l) and (s[p + 1] == "L"):
                ans += 40
                p += 1
            elif (p + 1 < l) and (s[p + 1] == "C"):
                ans += 90
                p += 1
            else:
                ans += 10
        elif s[p] == "L":
            ans += 50
        elif s[p] == "C":
            if (p + 1 < l) and (s[p + 1] == "D"):
                ans += 400
                p += 1
            elif (p + 1 < l) and (s[p + 1] == "M"):
                ans += 900
                p += 1
            else:
                ans += 100
        elif s[p] == "D":
            ans += 500
        elif s[p] == "M":
            ans += 1000

        p += 1

    return ans

def romanToInt_2(s):
    """
    :type s: str
    :rtype: int
    """
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    decrisers = {
        "I": ["V", "X"],
        "X": ["L", "C"],
        "C": ["D", "M"]
    }
    
    p = 0
    l = len(s)
    ans = 0
    while p < l:
        if (p + 1 < l) and \
            s[p] in decrisers and \
            s[p + 1] in decrisers[s[p]]:
            ans  -= roman[s[p]]
        else:
            ans += roman[s[p]]
            
        p += 1
    
    return ans
    
print(romanToInt_2("II") == 2)
print(romanToInt_2("XXVII") == 27)
print(romanToInt_2("IV") == 4)
print(romanToInt_2("V") == 5)
print(romanToInt_2("VI") == 6)
print(romanToInt_2("X") == 10)
print(romanToInt_2("IX") == 9)
print(romanToInt_2("XI") == 11)


print(romanToInt_2("IV"))