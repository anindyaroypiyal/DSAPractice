def combinations(s):

    # Write your code here
    res = []
    digitToChar = {"2":"abc",
                   "3":"def",
                   "4":"ghi",
                   "5":"jkl",
                   "6":"mno",
                   "7":"pqrs",
                   "8":"tuv",
                   "9":"wxyz" }
    
    def backTrack(i, curStr):
        if len(curStr) == len(s):
            res.append(curStr)
            return
        
        for c in digitToChar[s[i]]:
            backTrack(i+1, curStr+c)
    
    backTrack(0, "")
    return res
