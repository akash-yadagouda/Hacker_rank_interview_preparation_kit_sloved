def LCS(i,j,A,B):
    if i>(n1-1) or j>(n2-1):
        return 0
    elif A[i]==B[j]:
        return 1 + LCS(i+1,j+1,A,B)
    else:
        return max(LCS(i+1,j,A,B),LCS(i,j+1,A,B))
    
A = input()
n1 = len(A)
B = input()
n2 = len(B)

print(LCS(0,0,A,B))

