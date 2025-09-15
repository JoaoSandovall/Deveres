import random

print("\nVamos jogar o jogo da forca!")
print("Tente adivinhar a palavra secreta, letra por letra.")

palavras = ["Meg", "Python", "Desenvolvimento", "Programação", "DEV"]
palavra_secreta = random.choice(palavras)

letras_acertadas  = []
letras_tentadas = []
tentativas = 6

while tentativas > 0:
    palavra_exibida = ""
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavras_exibida += letra + " "
        else:
            palavra_exibida += "_ "
            
    print("\nPalavra: ", palavra_exibida)
    
    if "_" not in palavra_exibida:
        print(f"Parabéns! Você acertou a palavra.\na palavra era: {palavra_secreta}")
        break
    
    print(f"Você tem {tentativas}")
    tentativa = input("Digite uma letra: ").strip()
    if len(tentativa)!= 1 or not tentativa.isalpha():
        print("Por favor, insira uma única letra válida.")
        continue
    
    if tentativa in letras_tentadas:
        print("Você já tentou essa letra. Tente outra.")
        continue