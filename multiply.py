# Input: num1 = "2", num2 = "3"
# Output: "6"
# Note: You must not use any built-in BigInteger library
# or convert the inputs to integer directly.
def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    multipication = [0] * (len(num1) + len(num2))
    print(multipication)

    num1 = num1[::-1]
    num2 = num2[::-1]




    for i in range(len(num2)):
        for j in range(len(num1)):
            digitMul = int(num2[i]) * int(num1[j])

            sum = digitMul + multipication[i+j]

            carry = sum//10
            multipication[i+j] = sum % 10
            multipication[i + j + 1] += carry
            print(f"Multiplying {num2[i]} by {num1[j]}, digitmul : {digitMul},  sum: {sum}, carry: {carry}, intermediate result: {multipication} also i and j : {i} and {j}")

    while len(multipication) > 1 and multipication[-1] == 0:
        multipication.pop()

    multipication.reverse()
    results = "".join(map(str,multipication))
    return results



num1 = "2"
num2 = "3"

print(multiply(num1, num2))
