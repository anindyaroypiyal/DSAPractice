message="sadasd"
res = ''

count = 0
res += message[0]
prev = message[0]
for i in range(len(message)):
    
    if (message[i] == prev):
        count += 1
        prev = message[i]
    else:
        res += str(count) + message[i]
        count = 1
        prev = message[i]
res += str(count)
print (res)