def validPalindrome(s):
    i = 0  # Start index
    j = len(s) - 1  # End index

    while i < j:
        if s[i] != s[j]:
            # Check if removing one of the mismatched characters makes it a palindrome
            result = s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]  # Corrected line
            print(f"Num  {s[i:j]} : {s[i:j][::-1]} and {i} , {j}")
            print(f"Num  {s[+1:j+1]} : {s[i+1:j+1][::-1]}")
            return result
        i += 1
        j -= 1

    return True  # If no mismatch is found, it's a palindrome

s = "abc"
print(validPalindrome(s))








