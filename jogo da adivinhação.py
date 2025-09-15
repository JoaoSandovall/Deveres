import random

print("\nBem-vindo ao jogo da adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

numero_secreto = random.randint(1, 100)

tentativas = 0
max_tentativas = 10

while True:
    tentativas += 1
    if tentativas > max_tentativas:
        print(f"Suas tentativas acabaram! \n O número era: {numero_secreto}")
        break
    try:
        palpite = int(input("Digite seu palpite: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue
    
    if palpite < numero_secreto:
        print("Número muito baixo!")
    elif palpite > numero_secreto:
        print("Número muito alto!")
    else:
        print(f"Parabéns! Você acertou. O número era {numero_secreto}.")
        break