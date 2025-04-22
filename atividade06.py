import statistics

def analisador_de_dados():
    entrada = input("Digite uma lista de números separados por vírgula: ")
    try:
        # Converte a string em uma lista de números float
        numeros = [float(num.strip()) for num in entrada.split(',')]

        media = statistics.mean(numeros)
        mediana = statistics.median(numeros)
        moda = statistics.mode(numeros)

        print(f"\nMédia: {media}")
        print(f"Mediana: {mediana}")
        print(f"Moda: {moda}")
    except ValueError:
        print("Erro: Certifique-se de digitar apenas números separados por vírgula.")
    except statistics.StatisticsError:
        print("Erro: Não foi possível calcular a moda (pode haver múltiplos valores com mesma frequência).")

# Exemplo de uso:
analisador_de_dados()
