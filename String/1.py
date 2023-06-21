

def reverseStringWordWise(string):
    
    #Your code goes here
    a = string.split()
    new_string = ""
    for i in reversed(a):
        new_string += i + " " 
    return (new_string)












    


string = input()
ans = reverseStringWordWise(string)
print(ans)
        
