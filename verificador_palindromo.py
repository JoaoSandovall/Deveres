palindromo = input("\nDigite uma palavra ou frase para identificar o palindromo: ")

palindromo_limpo = palindromo.replace(" ", "").lower()

if palindromo_limpo == palindromo_limpo[::-1]:
    print(f"\n A palavra ou frase '{palindromo}' é um palindromo!")
else:
    print(f"Essa palavra não é um palindromo.")