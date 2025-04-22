import platform

def informacoes_do_sistema():
    so = platform.system()
    versao = platform.version()
    nome_completo = platform.platform()

    print("Informações do Sistema:")
    print(f"- Sistema Operacional: {so}")
    print(f"- Versão: {versao}")
    print(f"- Detalhes completos: {nome_completo}")

# Exemplo de uso:
informacoes_do_sistema()
