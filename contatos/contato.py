def adicionar_contato():
    while True:
        nome = input("Digite o nome do contato: ")
        if not nome.strip():
            print("O nome não pode ser vazio. Tente novamente.")
            continue
        
        telefone = input("Digite o telefone do contato: ")
        if not telefone.strip():
            print("O telefone não pode ser vazio. Tente novamente.")
            continue
        
        if not telefone.isdigit():
            print("O telefone deve conter apenas números. Tente novamente.")
            continue
            
        
        with open('contatos/contatos.txt', 'a') as arquivo:
            arquivo.write(f"{nome.strip()},{telefone.strip()}\n")
            
        print(f"Contato '{nome.strip()}' adicionado com sucesso.")
        break

def visualizar_contato():
    contatos_lidos = []
    try:
        with open('contatos/contatos.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            
            if not linhas:
                print("Ainda não existem contatos salvos.")
                return contatos_lidos
            
            print("\n--- Lista de Contatos ---")
            for linha in linhas:
                linha_limpa = linha.strip()
                partes = linha_limpa.split(',')
                
                if len(partes) == 2:
                    nome = partes[0]
                    telefone = partes[1]
                    contatos_lidos.append({"nome": nome, "telefone": telefone})
                    print(f"Nome: {nome}, Telefone: {telefone}")
        return contatos_lidos
        
    except FileNotFoundError:
        print("Ainda não existem contatos salvos.")
        return contatos_lidos

def deletar_contato():
    lista_de_contatos = visualizar_contato()
    
    if not lista_de_contatos:
        return
    
    nome_deletar = input("\nDigite o nome que deseja deletar: ")
    encontrado = False
    nova_lista = []
    for contato in lista_de_contatos:
        if contato["nome"].lower() != nome_deletar.lower():
            nova_lista.append(contato)
        else:
            encontrado = True
            
    if encontrado:
        with open('contatos/contatos.txt', 'w') as arquivo:
            for contato in nova_lista:
                arquivo.write(f"{contato['nome']},{contato['telefone']}\n")
            print(f"O contato '{nome_deletar}' foi excluído com sucesso.")
    else:
        print(f"O contato '{nome_deletar}' não foi encontrado.")
      
while True:
    print("\n--- Gerenciador de Contatos ---")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Deletar contato")
    print("4. Sair\n")
    
    escolha = input("Digite sua escolha: ")
    
    if escolha == '1':
        adicionar_contato()
    elif escolha == '2':
        visualizar_contato()
    elif escolha == '3':
        deletar_contato()
    elif escolha == '4':
        print("Programa encerrado.")
        break
    
    else:
        print("Opção inválida. Por favor, digite 1, 2 ou 3.")