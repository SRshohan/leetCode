# Given an input string which contains open and/or close parentheses, find the minimum number of parentheses needed to be added in order to balance the input string.
#
# Input: ((( Output: 3 	((()))
# Input: ()) Output: 1 	(())
#
# Input: )(




def parenthesisMin(s):
    n = len(s)
    i = 0
    leftPart = 0
    rightPart = 0


    dict = {")": "("}
    while i < n:
        if s[i] in dict.keys():
            leftPart += 1
        elif s[i] in dict.values():
            rightPart += 1
        i += 1

    minimumParent = abs(rightPart-leftPart) -1
    if minimumParent == -1:
        return 0
    else:
        return minimumParent




print(parenthesisMin("((()))(())"))






