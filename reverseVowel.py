def reverV(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []


    for i in range(len(s)):
        if s[i] in vowels:
            result.append(s[i])

    result.reverse()
    s_list = list(s)
    k = 0
    for i in range(len(s)):
        if s_list[i] in vowels:
            s_list[i] = result[k]
            k += 1
    return "".join(s_list)
s = "hello"

print(reverV(s))




