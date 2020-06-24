#
##
#import numpy as np
#a=np.zeros([6,6],dtype=int)
#for i in range(6):
#    for j in range(6):
#        a[i][j]=int(input())
#        j=j+1
#    i=i+1
#        
##
##aa=[[1,2,3,4,5,6],
##    [1,2,3,4,5,6],
##    [1,2,3,4,5,6],
##    [1,2,3,4,5,6],
##    [1,2,3,4,5,6],
##    [1,2,3,4,5,6]]
#
##for i in range(m-3+1):
##    for j in range(n-3+1):
##        for a in range(3):
##            for b in range(3):
##                sum += img[i+a][j+b] * filter[a][b]
##        img1[i][j] = sum
##        sum=0
#
#
#
#def getmax(arr):
#    max1=0
#    for k in range(4):
#        for l in range(4):
#            h=np.zeros([3,3],dtype=int)
#            for i in range(3):
#                for j in range(3):
##                    if i!=1 and j!=0:
##                        pass
##                    elif i!=1 and j!=2:
##                         pass
##                    else:
#                    h[i][j]=arr[k+i][l+j]
#                h[1][0]=0
#                h[1][2]=0
#                        
#            su=np.sum(h)
#            
##            print(h)
##            print(su)
#            if su>=max1:
#                max1=su
#                
#    return max1
#
#
#x1=getmax(aa)
#print(x1)



#
#import numpy as np
#
a=[[0,-4,-6,0,-7,-6],
   [-1,-2,-6,-8,-3,-1],
   [-8,-4,-2,-8,-8,-6],
   [-3,-1,-2,-5,-7,-4],
   [-3,-5,-3,-6,-6,-6],
   [-3,-6,0,-8,-6,-7]]

        
#
#aa=[[1,2,3,4,5,6],
#    [1,2,3,4,5,6],
#    [1,2,3,4,5,6],
#    [1,2,3,4,5,6],
#    [1,2,3,4,5,6],
#    [1,2,3,4,5,6]]

#for i in range(m-3+1):
#    for j in range(n-3+1):
#        for a in range(3):
#            for b in range(3):
#                sum += img[i+a][j+b] * filter[a][b]
#        img1[i][j] = sum
#        sum=0
def getsum(w):
    su=0
    for i in range(3):
        for j in range(3):
            su=su+w[i][j]
    return su


def getmax(arr):
    max1=-10000
    for k in range(4):
        for l in range(4):
            
            h=[[0,0,0],
               [0,0,0],
               [0,0,0]]
            for i in range(3):
                for j in range(3):
#                    if i!=1 and j!=0:
#                        pass
#                    elif i!=1 and j!=2:
#                         pass
#                    else:
                    h[i][j]=arr[k+i][l+j]
                h[1][0]=0
                h[1][2]=0
                        
            
            
#            print(h)
#            print(su)
            su=getsum(h)
            
            if su>=max1:
                max1=su
                
    return max1


x1=getmax(a)
print(x1)
