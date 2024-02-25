def isValid(s):
    dict = {"(" : ")",
            "{" : "}",
            "[" : "]"}
    n = len(s)

    stack = []


    for i in range(n):
        if s[i] in dict.keys():
            stack.append(s[i])
        else:
            if not stack: # When stack is empty
                return False

            topElement = stack.pop()

            if dict[topElement] != s[i]:
                return False

    return True




s = "()[]}"

print(isValid(s))




