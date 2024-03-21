# Problema de vectores
# La empresa "Margarita" vende papas fritas de 7 referencias distintas.
# Se necesita conocer las ventas pro referencia en un dia y el total general de ventas, tanto en cantidades como en dinero


# declarar vector
can, ref, total = [], [], []
T = 7


def inicializar():
    for i in range(T):
        can.append(0)
        ref.append(0)
        total.append(0)
    print(can)


def captura():
    for i in range(T):
        can[i] = int(input('Digite la cantidad de ventas de la referencia de papa frita '))
    return can


def referencias():
    for i in range(T):
        ref[i] = int(input('Digite valor de ventas de la referencia de papa frita '))
    return ref


def costos(can, ref):
    for i in range(T):
        total[i] = can[i]*ref[1]
    return total


def mostrar(can, ref, total):
    tgv=0
    tgc = 0
    print(can)
    print(ref)
    print(total)
    for i in range(T):
        tgc = tgc+can[i]
    for i in range(T):
        tgv = tgv+total[i]
        print("Las ventas totales en unidades es ",tgc)
        print("Las ventas totales en dinero es ",tgv)


def titulo():
    print("Empresa Margarita")


def salir():
    print("Salir Empresa Margarita")


def main():
    titulo()
    inicializar()
    can = captura()
    ref = referencias()
    total = costos(can, ref)
    mostrar(can, ref, total)
    salir()


# Bloque principal
main()
