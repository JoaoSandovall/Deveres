while True:
    senha = input("Digite a senha a ser verificada: ")

    if not senha:
        print("Senha não pode ser vazia. Tente novamente.")
        continue
    
    senha_tamanho = len(senha)
    senha_maiuscula = any(c.isupper() for c in senha)
    senha_minuscula = any(c.islower() for c in senha)
    senha_numero = any(c.isdigit() for c in senha)
    
    if senha_tamanho < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
    elif not senha_maiuscula:
        print("Senha fraca: deve conter pelo menos uma letra maiúscula.")
    elif not senha_minuscula:
        print("Senha fraca: deve conter pelo menos uma letra minúcula.")
    elif not senha_numero:
        print("Senha fraca: deve conter pelo menos um número.")
    else:
        print("Senha forte!")
        break