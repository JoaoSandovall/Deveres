while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        resultado = numero1 / numero2
        print(f"Seu resultado é: {resultado}.")
            
    except ValueError:
        print("ERROR: Digite apenas número.")
        
    except ZeroDivisionError:
        print("ERRO: Não é possível dividir por zero.")
    