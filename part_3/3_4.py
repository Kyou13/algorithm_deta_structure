def select_sort(X):
    for i in range(len(X)-1):
        minj = i
        for j in range(i+1,len(X)):
            if(X[j] < X[minj]):
                minj = j
        X[i],X[minj] = X[minj],X[i]
    return X

if __name__ == "__main__":
    X = list(map(int, input().split()))

    X = select_sort(X)
    print(X)
