import os

def organizador_de_pastas():
    nome_pasta = input("Digite o nome da nova pasta: ").strip()

    try:
        # Cria a pasta no diretório atual
        os.makedirs(nome_pasta, exist_ok=True)
        print(f"Pasta '{nome_pasta}' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar a pasta: {e}")
        return

    print("\nArquivos e diretórios no local atual:")
    itens = os.listdir()

    for item in itens:
        print(f"- {item}")

# Exemplo de uso:
organizador_de_pastas()
