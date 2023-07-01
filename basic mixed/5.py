from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def kThCharaterOfDecryptedString(s, k) :

	# Your code goes here
    new_s = ''
    now = ''
    d = ''

    for i in range(len(s)):
        if not s[i].isdigit():
            # print(s[i])
            now += s[i]
        else:
            d += s[i]
            if not (s[(i+1)%len(s)].isdigit()):
                new_s += now*int(d)
                now = ''
                d = ''
            # print(new_s, 'nws')
    return (new_s[k-1])
    # print(new_s)
































#taking inpit using fast I/O
def takeInput() :
	
    str1 = input().strip()
    k = int(input().strip())

    return str1, k

#main
str1, k = takeInput()
print(kThCharaterOfDecryptedString(str1, k))
