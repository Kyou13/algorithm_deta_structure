def bubble_sort(X):
    flag = True
    #i = 0
    #while flag:
    for i in range(0,len(X)-1):
        flag = False
        for j in range(len(X)-1,i,-1):
            if X[j-1] > X[j]:
                X[j-1], X[j] = X[j], X[j-1]
                flag = True
    i += 1
    return X

    
if __name__ == "__main__":
    X = list(map(int, input().split()))

    X = bubble_sort(X)
    print(X)
