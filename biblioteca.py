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
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    
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
    print("\nLivros disponíveis para serem emprestados")
    
    livro_encontrado[]
    
    for livro in biblioteca:
        if livro["disponível"]
        f
    
    titulo_emprestar = input("\nDigite o título do livro que deseja pegar emprestado: ")
    livro_encontrado = False
    
    for livro in biblioteca:
        if livro.titulo.lower() == titulo_emprestar.lower():
            livro_encontrado = True
            
            if livro.disponivel:
                livro.disponivel = False
                print(f"O livro '{livro.titulo}' foi emprestado.")
            else:
                print(f"O livro '{livro.titulo}' já está emprestado.")
            break
                    
    if not livro_encontrado:
        print("Livro não encontrado.")
    
while True:
    
    print("\n--Menu da Biblioteca--\n")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. emprestar livro")
    print("4. Devolver livro")
    print("5. Sair\n")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        adicionar_livro() 
    elif escolha == '2':
        listar_livros()
    elif escolha == '3':
        emprestar_livro()
    elif escolha == '5':
        print("Programa encerrado.")
        break        