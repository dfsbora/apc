import sys
from math import sqrt
operacao=sys.argv[1] #o tipo de operação
num1 =int(sys.argv[2]) #a
num2=int(sys.argv[3]) #b
num3=int(sys.argv[4])#c

def raiz1(a,b,c):
    if a !=0:
        resultado= -b+sqrt(b**2-4*a*c)/2*a
        print(resultado)
    else:
        print("Não é uma função quadrática")


def raiz2(a,b,c):
    if a !=0:
        resultado= -b-sqrt(b**2-4*a*c)/2*a
        print(resultado)
    else:
        print("Não é uma função quadrática")


def x_do_vértice(a,b):
    if a!=0:
        resultado= -b/2*a
        print(resultado)
    else:
        print("Não é quadrática")

def y_do_vértice(a,b,c):
    if a!=0:
        resultado= -sqrt(b**2-4*a*c)/4*a
        print(resultado)
    else:
        print("Não é quadrática")

if operacao=="raiz1":
    raiz1(num1,num2,num3)

elif operacao=="raiz2":
    raiz2(num1,num2,num3)

elif operacao=="xv":
    x_do_vértice(num1,num2)

elif operacao=="yv":
    y_do_vértice(num1,num2,num3)

else:
    print("Digte uma operação válida")
