import time

def cronometro():
    try:
        segundos = int(input("Digite o tempo em segundos: "))
        print("\nIniciando o cronômetro...\n")
        for i in range(segundos, -1, -1):
            print(i)
            time.sleep(1)
        print("\nTempo encerrado!")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Exemplo de uso:
cronometro()
