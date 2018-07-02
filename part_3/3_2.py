def insert_sort(X):
    for i in range(1,len(X)):
        v = X[i]
        j = i - 1
        while j >= 0 and X[j] > v:
            X[j+1] = X[j]
            j -= 1
        X[j+1] = v
    return X

if __name__ == "__main__":
    X = list(map(int, input().split()))

    X = insert_sort(X)
    print(X)
