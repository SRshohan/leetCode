def conConstruct(ransom, magazine):
    ransom = list(ransom)
    magazine = list(magazine)
    for i in range(len(ransom)):
        if ransom[i] not in magazine:
            return False
        else:
            magazine.remove(ransom[i])

    return True



ransomNote = "aa"
magazine = "aab"

print(conConstruct(ransomNote,magazine))