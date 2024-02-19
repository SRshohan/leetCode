def wordPattern(pattern, s):
    s = s.split(" ")
    pattern = list(pattern)
    prev = 0
    hdict = {

    }

    for i in range(len(pattern)):
        if pattern[i] not in hdict.keys():
            hdict[pattern[i]] = s[i]
        elif hdict[pattern[i]] in hdict.keys():
            if hdict[pattern[i]] == hdict[pattern[prev]]:
                return False
            prev += 1
    return True






pattern = 'abba'
s = 'dog cat cat fish'

print(wordPattern(pattern,s))

