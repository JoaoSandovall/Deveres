import random

OPCOES = ["Pedra", "Papel", "Tesoura"]
jogada_usuario = ""
pontuacao_usuario = 0
pontuacao_computador = 0

while True:
    print("\nJogo jokempo\n") 
    print(f"Você: {pontuacao_usuario}   |   Computador: {pontuacao_computador}\n")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura\n")
     
    escolha_numero = input("Escolha Pedra, papel ou tesoura: ").strip()
    
    if escolha_numero == '1':
        jogada_usuario = "Pedra"
    elif escolha_numero == '2':
        jogada_usuario = "Papel"
    elif escolha_numero == '3':
        jogada_usuario = "Tesoura"
    else:
        print("Opção inválida, tente novamente")
        continue

    jogada_computador = random.choice(OPCOES)
    print(f"\nVocê escolheu: {jogada_usuario.capitalize()}")
    print(f"Computador escolheu: {jogada_computador.capitalize()}")

    if jogada_usuario == jogada_computador:
        print("Deu empate, ninguém fez ponto.")
    
    elif (jogada_usuario == "Pedra" and jogada_computador == "Tesoura") or \
         (jogada_usuario == "Papel" and jogada_computador == "Pedra") or \
         (jogada_usuario == "Tesoura" and jogada_computador == "Papel"):
        print("Você ganhou a rodada!")
        pontuacao_usuario += 1
    
    else:
        print("O computador ganhou a rodada!")
        pontuacao_computador += 1
    
    if pontuacao_computador == 3 or pontuacao_usuario == 3:
        print("\n--- FIM DE JOGO ---\n")
        print(f"Placar final: Você: {pontuacao_usuario}   |   Computador: {pontuacao_computador}")
        if pontuacao_usuario == 3:
            print("Parabéns, você venceu o jogo!\n")
        else:
            print("O computador ganhou, tente novamente.\n")
        break