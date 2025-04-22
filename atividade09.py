import random
import string

def gerar_senha_forte(tamanho=10):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choices(caracteres, k=tamanho))
    print(f"Senha gerada: {senha}")

# Exemplo de uso:
gerar_senha_forte()
