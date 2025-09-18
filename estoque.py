estoque = {
    "pão": 2.50,
    "leite": 5.00,
    "carne": 20.00,
    "frutas": 10.00,
    "café": 8.00
}

carrinho = {}

def adicionar_produto():
    
    print("\nProdutos disponíves:")
    for produto, preco in estoque.items():
        print(f"{produto.capitalize()}: R${preco:.2f}")
        
    nome_produto = input("\nDigite o nome do produto que deseja adicionar ao carrinho: ").lower()
    
    if nome_produto in estoque:
        try:
            quantidade = int(input(f"Quantos {nome_produto} Você deseja adicionar? "))
            
            if quantidade >= 0:
                if nome_produto in carrinho:
                    carrinho[nome_produto] += quantidade
                else:
                    carrinho [nome_produto] = quantidade
                print(f"{quantidade} {nome_produto}(s) adicionado(s) ao carrinho.")
                
            else:
                print("Quantidade inválida. deve ser número positivo.")
        except ValueError:
            print("Quantidade inválida. deve ser um número inteiro.")
    else:
        print("Produto não encontrado no estoque.")

    
while True:
    print("\nMenu de Opções: ")
    print("1. Adicionar produto")
    print("2. visualizar produtos")
    print("3. Calcular total de vendas")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        adicionar_produto()
    elif escolha == '4':
        print("Programa encerrado.")
        break