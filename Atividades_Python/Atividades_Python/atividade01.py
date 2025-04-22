import math

def calculadora_cientifica(numero):
    if numero <= 0:
        print("Para logaritmo e raiz quadrada, o número deve ser positivo.")
    else:
        print(f"Raiz quadrada de {numero}: {math.sqrt(numero)}")
        print(f"Seno de {numero} (em radianos): {math.sin(numero)}")
        print(f"Cosseno de {numero} (em radianos): {math.cos(numero)}")
        print(f"Logaritmo natural de {numero}: {math.log(numero)}")

# Exemplo de uso:
try:
    valor = float(input("Digite um número: "))
    calculadora_cientifica(valor)
except ValueError:
    print("Por favor, digite um número válido.")
