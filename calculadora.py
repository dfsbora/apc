import sys

# operacao
# num1
# num2

operacao = sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])


def soma(a,b):
	resultado = a+b
	print(resultado)

def subtracao(a,b):
	print(a-b)

def multiplicacao(a,b):
	return a*b

def divisao1(a,b):
	if b == 0:
		print("indeterminado")
	else:
		resultado = a/b
		print(resultado)

def divisao2(a,b):
	try:
		resultado = a/b 
	except:
		print("ZeroDivisionError")

def potencia(a,b):
	return a**b 


if operacao == "soma":
	soma(num1,num2)
elif operacao == "sub": 
	subtracao(num1, num2)
elif operacao == "div":
	divisao1(num1, num2)

