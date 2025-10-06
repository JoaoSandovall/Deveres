import math

def iniciar_simulacao():
    print("\n--- Calculadora de Investimetos Simples ---")
    
    try:
        capital_inicial = float(input("Qual o capital inicial? R$ "))
        taxa_juros_percentual = float(input("Qual a taxa de juros MENSAL (ex: 0.5 para 0.5%)? "))
        periodo_meses = int(input("Por quantos meses deseja simular (ex: 12)? "))
    except ValueError:
        print("\nERRO: Por favor, digite apenas números válidos.")
        return
    
    taxa_juros_decimal = taxa_juros_percentual / 100
    saldo_atual = capital_inicial
    
    print(f"Mês 0: Saldo Inicial R$ {saldo_atual:.2f}")
    
    for mes in range(1, periodo_meses + 1):
        juros_ganhos = saldo_atual * taxa_juros_decimal
        
        saldo_atual += juros_ganhos
        saldo_atual = round(saldo_atual, 2)
        
        print(f"Mês {mes}: Saldo R$ {saldo_atual:.2f}")
        
        print(f"\n--- Resultado Final ---")
        print(f"Capital Inicial: R$ {capital_inicial:.2f}")
        print(f"Saldo Final: R$ {saldo_atual:.2f}")
        print(f"Total de Juros Ganhos: R$ {(saldo_atual - capital_inicial):.2f}")

iniciar_simulacao()