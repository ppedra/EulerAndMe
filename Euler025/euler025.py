def fibo_index():
    l = []
    l.append(0)
    l.append(1)
    cont=1
    while True:
        l.append(l[cont] + l[cont-1])
        if len(str(l[cont+1]))>=1000: 
            return (cont+1)
        cont += 1

if __name__ == "__main__":
    print(fibo_index())