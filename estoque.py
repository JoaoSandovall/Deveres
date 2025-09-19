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

def visualizar_produtos():
    print("\n--Produtos no Carrinho--\n")
    
    if not carrinho:
        print("O Carrinho está vazio.")
        return
    total_carrinho = 0
    for produto, quantidade in carrinho.items():
        preco_unitario = estoque[produto]
        subtotal_produto = preco_unitario * quantidade
        print(f"Produto: {produto.capitalize()} | Quantidade: {quantidade} | preço unitário: R${preco_unitario:.2f} | subtotal: R${subtotal_produto:.2f}")
        total_carrinho += subtotal_produto
        
    print(f"\nTotal do carrinho: R${total_carrinho:.2f}")
    print("\n------------------------\n")
    
while True:
    print("\n--Menu de Opções--\n")
    print("1. Adicionar produto")
    print("2. visualizar produtos e total do carrinho")
    print("3. finalizar compras\n")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        adicionar_produto()
    elif escolha == '2':
        visualizar_produtos()
    elif escolha == '4':
        print("Programa encerrado.")
        break