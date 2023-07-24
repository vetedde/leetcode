# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def isValid(string):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    pairs = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    open = pairs.values()
    close = pairs.keys()

    for s in string:
        if s in open:
            stack.append(s)
        else:
            if stack and stack[-1] == pairs[s]:
                stack.pop()
            else:
                return False

    return not bool(stack)

print(isValid("()") == True)
print(isValid("(") == False)
print(isValid("(]") == False)
