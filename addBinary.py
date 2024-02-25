def addBinary(a,b):
    sum = []
    secBin = -1
    dict = {2:10,3:11}
    carry = 0

    for i in range(-1, len(a), -1):
        total = int(a[i]) + int(b[secBin]) + carry
        if sum[i] == 2 or 3:
            carry = dict[sum[i]] // 10
            total = dict[sum[i]] % 10
        if secBin != 0:
            secBin -= 1
        sum.append(total)

    sum = sum.reverse()
    return ''.join(sum)







a = "11"
b = "1"


for i in range(8, -1, -1):
    print(i)

