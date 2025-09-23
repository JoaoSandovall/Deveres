import random

print("\nVamos jogar o jogo da forca!")
print("Tente adivinhar a palavra secreta, letra por letra.")

palavras = ["meg", "python", "desenvolvimento", "programacao", "dev"]
palavra_secreta = random.choice(palavras)

letras_acertadas = []
letras_tentadas = []
tentativas = 6

while tentativas > 0:
    palavra_exibida = ""
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_exibida += letra + " "
        else:
            palavra_exibida += "_ "
            
    print("\nPalavra: ", palavra_exibida)
    
    if "_" not in palavra_exibida:
        print(f"Parabéns! Você acertou a palavra.\nA palavra era: {palavra_secreta}")
        break
        
    palpite = input("Adivinhe uma letra: ").lower()
    
    if palpite in letras_tentadas:
        print("Você já tentou essa letra. Tente outra.")
        continue
    
    letras_tentadas.append(palpite)
    
    if palpite in palavra_secreta:
        letras_acertadas.append(palpite)
        print("Boa! Você acertou uma letra.")
        
    else:
        tentativas -= 1
        print(f"Letra incorreta. Você tem {tentativas} tentativas restantes.")
        
    if tentativas == 0:
        print(f"Fim de jogo! A palavra era: {palavra_secreta}")