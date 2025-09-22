class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

biblioteca = [
    livro("1984", "George Orwell"),
    livro("O senhor dos anéis", "J.R.R. Tolkien"),
    livro("O pequeno príncipe", "Antoine de Saint-Exupéry"),
    livro("Dom Quixote", "Miguel de Cervantes"),
    livro("A divina comédia", "Dante Alighieri"),
    livro("Hamlet", "William Shakespeare"),
]
    
def adicionar_livro():
    
    titulo = ""
    while not titulo:
        titulo = input("Digite o título do livro: ")
        if not titulo: 
            print ("O titulo não pode ser vázio. Tente novamente.")
    
    autor = ""
    while not autor:
        autor = input("Digite o nome do autor do livro: ")
        if not autor:
            print("O autor não pode ser vázio. Tente novamente.")
            
    novo_livro = livro(titulo, autor)
    biblioteca.append(novo_livro)
    print(f"O livro: '{titulo}' de '{autor}' foi adicionado à biblioteca.")

def listar_livros():
    print("\n--Lista de livros na biblioteca--\n")
    if not biblioteca:
        print("Não existem livros disponíveis no momento.") 
    
    for livro in biblioteca:
        status = "Disponível" if livro.disponivel else "emprestado" 
        print(f"Título: {livro.titulo} | Autor: {livro.autor} | Status: {status}")

def emprestar_livro():
    print("\n--- Livros Disponíveis para Empréstimo ---")
    livros_disponiveis = False
    for livro in biblioteca:
        if livro.disponivel:
            livros_disponiveis = True
            status = "Disponível"
            print(f"Título: {livro.titulo} | Autor: {livro.autor} | Status: {status}")
    
    if not livros_disponiveis:
        print("Não existe nenhum livro disponível no momento.")
        return 

    titulo_emprestar = input("\nDigite o título do livro que deseja pegar emprestado: ")
    livro_encontrado = False 
    
    for livro in biblioteca:
        if livro.titulo.lower() == titulo_emprestar.lower():
            livro_encontrado = True
            
            if livro.disponivel:
                livro.disponivel = False
                print(f"O livro '{livro.titulo}' foi emprestado com sucesso.")
            else:
                print(f"O livro '{livro.titulo}' já está emprestado.")
            
            break
            
    if not livro_encontrado:
        print("Livro não encontrado.")
        
def devolver_livro():
    print("\n--- Livros Emprestados para Devolução ---")
    livros_emprestados = False
    for livro in biblioteca:
        if not livro.disponivel:
            livros_emprestados = True
            print(f"Título: {livro.titulo} | Autor: {livro.autor}")
    
    if not livros_emprestados:
        print("Não há livros emprestados no momento.")
        return

    titulo_devolver = input("\nDigite o título do livro que deseja devolver: ")
    livro_encontrado = False
    
    for livro in biblioteca:
        if livro.titulo.lower() == titulo_devolver.lower():
            livro_encontrado = True
            
            if not livro.disponivel:
                livro.disponivel = True
                print(f"O livro '{livro.titulo}' foi devolvido com sucesso.")
            else:
                print(f"O livro '{livro.titulo}' não está emprestado.")
            
            break
            
    if not livro_encontrado:
        print("Livro não encontrado.")

while True:
    print("\n--Menu da Biblioteca--\n")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Sair\n")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        adicionar_livro() 
    elif escolha == '2':
        listar_livros()
    elif escolha == '3':
        emprestar_livro()
    elif escolha == '4':
        devolver_livro()
    elif escolha == '5':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Digite a escolha certa (de 1 à 5).")