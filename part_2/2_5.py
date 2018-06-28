# 最大利得を求める
# input: 整数n個
# output: 最大値1個

# O(n^2)
def rieki_1(x):
    maxv = -1
    for i in range(1, len(x)):
        for j in range(i):
            maxv = max(maxv, x[i]-x[j])
    return maxv

# O(n)
def rieki_2(x):
    minv = x[0]
    maxv = -1
    for i in range(1,len(x)):
        maxv = max(maxv, x[i]-minv) 
        minv = min(minv, x[i])

if __name__ == '__main__':
    x = list(map(int,input().split()))
    print(rieki_1(x))
