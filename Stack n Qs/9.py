from collections import deque
def isValidParenthesis(expression):

    # Write your code here.
    p_checker = deque()

    for i in expression:
        if i == '(' or i == '{' or i == '[':
            p_checker.append(i)
        elif i == ')' and p_checker[-1] == '(':
            p_checker.pop() 
        elif i == '}' and p_checker[-1] == '{':
            p_checker.pop() 
        elif i == ']' and p_checker[-1] == '[':
            p_checker.pop()
    if len(p_checker) == 0:
        return True
    else: return False




# Main Code

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)

    if ans:
        print("Balanced")
        
    else:
        print("Not Balanced")
