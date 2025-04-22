from datetime import datetime

def descobrir_dia_semana():
    data_str = input("Digite uma data (dd/mm/aaaa): ")
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        dias_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 
                       'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
        dia_semana = dias_semana[data.weekday()]
        print(f"A data {data_str} cai em uma {dia_semana}.")
    except ValueError:
        print("Formato inválido. Digite a data no formato dd/mm/aaaa.")

# Exemplo de uso:
descobrir_dia_semana()
