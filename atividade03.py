from datetime import datetime

def agenda_digital():
    agora = datetime.now()
    data_formatada = agora.strftime("Hoje é dia %d/%m/%Y e agora são %H:%M.")
    print(data_formatada)

    compromissos = []

    while True:
        resposta = input("Deseja agendar um compromisso? (sim/não): ").strip().lower()
        if resposta != "sim":
            break

        titulo = input("Digite o título do compromisso: ")
        data = input("Digite a data do compromisso (dd/mm/aaaa): ")
        
        compromisso = f"{titulo} - {data}"
        compromissos.append(compromisso)
        print(f"Compromisso '{compromisso}' agendado com sucesso!\n")

    print("\nSeus compromissos agendados:")
    for c in compromissos:
        print(f"- {c}")

# Exemplo de uso:
agenda_digital()
