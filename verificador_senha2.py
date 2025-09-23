while True:
    senha = input("Digite a senha: ")
    
    if not senha:
        print("Senha não pode ser vázia. Tente novamente.")
        continue
    
    senha_tamanho = len(senha)
    senha_maiuscula = any(c.isupper() for c in senha)
    senha_minuscula = any(c.islower() for c in senha)
    senha_numero = any(c.isdigit() for c in senha)
    
    if senha_tamanho < 8:
        print("Senha pequena, no mínimo 8 digitos.")
    elif not senha_maiuscula:
        print("A senha precisa de pelo menos uma letra maiuscúla.")
    elif not senha_minuscula:
        print("A senha precisa de pelo menos uma letra minúscula.")
    elif not senha_numero:
        print("A senha precisa de pelo menos um número.")
    
    else:
        print("Senha forte!")
        break