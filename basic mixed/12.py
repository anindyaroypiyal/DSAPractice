def multiplyStrings(a, b):
    # Write your code here
    # Return the product of both given numbers
    aa = toInt(a)
    bb = toInt(b)

    return (aa * bb)
    


def toInt(s):
    num = 0
    for i in s:
        num = num * 10 + (ord(i) - 48)
    return num