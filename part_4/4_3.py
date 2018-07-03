def conv(x):
    try:
        return int(x)
    except:
        return x

if __name__ == "__main__":
    A = []
    while True:
        n = input()
        if n == 'fin':
            break
        if n == "+":
            a = A.pop()
            b = A.pop()
            A.append(a+b)
        elif n == "*":
            a = A.pop()
            b = A.pop()
            A.append(a*b)
        elif n == "-":
            b = A.pop()
            a = A.pop()
            A.append(a-b)

        else:
            A.append(int(n))
            
    print(A)

