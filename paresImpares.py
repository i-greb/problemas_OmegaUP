def _main(N, p) -> None:
    pares=[]
    impares=[]

    for x in N:
        if (x % 2 == 0):
            pares.append(x)
        else:
            impares.append(x)
        if p==0:
            for x in pares:
                print(x, end=" ")
        else:
            for x in impares:
                print(x, end="")



if __name__ == '__main__':
    N=[3,6,5,10,14,23,43,36]
    p=0
    _main(N,p)

