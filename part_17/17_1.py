import numpy as np
def coin_2zi(x,coins):
    # x円より高いコインは除外
    for c,i in enumerate(coins):
        if i > x:
            del(coins[c])
    coins.sort()

    db = np.zeros((len(coins)+1,x+1))
    for i in range(1,x+1):
        db[0][i] = 9999

    for i in range(1,len(coins)+1):
        for j in range(1,x+1):
            # min(使わない、使う)
            db[i][j] = min(db[i-1][j],db[i][j-coins[i-1]]+1)
    return db[-1][-1]

def coin_1zi(x, coins):
    db = np.zeros(x+1)
    for i in range(1,len(db)):
        db[i] = 999
    for i in range(0,len(coins)):
        for j in range(coins[i],x+1):
            db[j] = min(db[j], db[j-coins[i]]+1)
    return db[-1]

if __name__ == "__main__": 
    x = int(input())
    coins = list(map(int, input().split()))
    print(coin_1zi(x, coins))
    
