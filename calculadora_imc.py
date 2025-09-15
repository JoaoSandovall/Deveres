peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))

if altura <= 0:
    print("A altura não pode ser zero ou negativa.")
else:
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif 18.5 <= imc < 24.9:
        print("Você está com o peso ideal.")
    elif 25 <= imc < 29.9:
        print("Você está com sobrepeso.")
    else:
        print("Você está com obesidade.")