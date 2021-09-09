import sys

valores = sys.argv

# valores = [nome.py  2  7  33  4  2 ]


def soma(a,b):
	resultado = a+b
	return resultado

#num1 = int(argumentos[1])
#num2 = int(argumentos[2])

print("voce esta executando: ", sys.argv[0])

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
acumulativo = soma(num1, num2)



for i in range(3, len(valores)):
	acumulativo = soma(acumulativo, int(valores[i]))


print("soma: ", acumulativo)



