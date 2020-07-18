'''
def LCS(A,B):
    n1 = len(A)
    n2 = len(B)
    if n1<n2:
        temp = n1
        n1 = n2
        n2 = temp

    matrix =[[0 for i in range(0,n1)] for j in range(0,n2)]
    i = 1
    j = 1
    col = n1-1
    row = n2-1

    while i<=row:
        if A[i]==B[j]:
            matrix[i][j] = 1 + matrix[i-1][j-1]
        else:
            matrix[i][j]= max(matrix[i-1][j],matrix[i][j-1])
        if i>=col:
            i = 0
            j = j+1
        else:
            i = i+1
    print(matrix[n1-1][n2-1])

LCS(input(),input())

'''

def get_child(s1,s2):
    n1 = len(s1)
    n2 = len(s2)

    arr = [[0 for i in range(0,n1+1)] for j in range(0,n2+1)]
    #print(arr)

    for i in range(1,n2+1):
        for j in range(1,n1+1):
            #print(i,j)
            if s1[j-1]==s2[i-1]:
                arr[i][j] = 1 + arr[i-1][j-1]
            else:
                arr[i][j]= max(arr[i-1][j],arr[i][j-1])
    
    ans = max(max(arr))
    #print(arr)

    
    print(ans)



s1 = input()
s2 = input()

get_child(s1,s2)



