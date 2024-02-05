def licenseKeyFormatting(s, key):
    replace_s = s.replace('-', '').upper()
    print(replace_s)
    mod = len(replace_s) % key
    parts = []
    if mod:
        parts.append(replace_s[:mod])

    for i in range(mod, len(replace_s), key):
        parts.append(replace_s[i:i+key])
    return "-".join(parts)



s = "2-5g-3-J"
print(licenseKeyFormatting(s, 2))



