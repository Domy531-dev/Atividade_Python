import random

def simulador_de_dado():
    while True:
        input("Pressione Enter para lançar o dado...")
        resultado = random.randint(1, 6)
        print(f"Você tirou: {resultado}")

        repetir = input("Deseja jogar novamente? (sim/não): ").strip().lower()
        if repetir != "sim":
            print("Encerrando o simulador. Obrigado por jogar!")
            break

# Exemplo de uso:
simulador_de_dado()
