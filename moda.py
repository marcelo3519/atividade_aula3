from statistics import mode
def moda (n1,n2,n3,n4):
    notas = []
    notas.append(n1)
    notas.append(n2)
    notas.append(n3)
    notas.append(n4)
    moda = mode(notas)
    print(moda)