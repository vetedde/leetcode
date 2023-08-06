def validPalindrome(palindrome):
    """
    :type s: str
    :rtype: bool
    """
    l = len(palindrome)
    p1 = 0
    p2 = l - 1
    mistake = 0

    while p1 < p2:
        if palindrome[p1] != palindrome[p2]:
            if mistake == 1:
                return False

            mistake = 1
            if 0 < p1 + 1 < l and palindrome[p1 + 1] == palindrome[p2]:
                p1 += 1
            elif 0 < p2 - 1 < l and palindrome[p1] == palindrome[p2 - 1]:
                p2 -= 1
            else:
                return False

        p1 += 1
        p2 -= 1

    return True

# print(validPalindrome("abbc") == False)
# print(validPalindrome("abba") == True)
# print(validPalindrome("abbka") == True)
# print(validPalindrome("abkbkc") == False)
print(validPalindrome(("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")))
