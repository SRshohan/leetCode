def licenseKeyFormatting(s, key):
    # Remove dashes and convert to uppercase
    replace_s = s.replace('-', '').upper()
    # Calculate the length of the first group
    mod = len(replace_s) % key
    # Initialize the list to hold the parts of the formatted string
    parts = []

    # If there's a first group, add it to the list
    if mod:
        parts.append(replace_s[:mod])

    # Iterate over the rest of the string in chunks of size 'key'
    for i in range(mod, len(replace_s), key):
        parts.append(replace_s[i:i + key])

    # Join the parts with dashes and return
    return "-".join(parts)


# Test the function with different inputs
s1 = "2-5g-3-J"
print(licenseKeyFormatting(s1, 2))  # Expected output: "2-5G-3J"

s2 = "2-5g-3-J"
print(licenseKeyFormatting(s2, 4))  # Expected output: "25G3-J"
