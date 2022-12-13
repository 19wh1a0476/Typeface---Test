def helper(s1,s2,i,j):
    if i>=len(s1):
        return len(s2)-j
    if j>=len(s2):
        return len(s1)-i
    if s1[i]==s2[j]:
        return helper(s1,s2,i+1,j+1)
    replace = 1 + helper(s1,s2,i+1,j+1)
    delete = 1 + helper(s1,s2,i+1,j)
    insert = 1 + helper(s1,s2,i,j+1)
    return min(replace,delete,insert)

def EditDistance(s1,s2):
    return helper(s1,s2,0,0)
print(EditDistance("fram", "farm"))
