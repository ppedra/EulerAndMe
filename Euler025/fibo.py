def fibo(lim=25):
    l = []
    l.append(0)
    l.append(1)
    for i in range(1,lim):
        l.append(l[i] + l[i-1])
    return l

if __name__ == "__main__":
    print(fibo(1000))
