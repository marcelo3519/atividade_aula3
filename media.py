from statistics import mean

def media (n1,n2,n3,n4):
    notas  =  []
    notas.append(n1)
    notas.append(n2)
    notas.append(n3)
    notas.append(n4)
    media  = mean(notas)
    print(media)

