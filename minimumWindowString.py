two pointer , one gonna stay

for example:
    s = "ADOBECODEBANC", t = "ABC"


def minimumWin(s, t):
    n = len(s)
    m = len(t)
    result = ''
    mWindowc = 0

    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                result = result + s[i]
            else:
                result += s[i]
                continue






