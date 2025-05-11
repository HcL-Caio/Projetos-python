valor1 = int(input("Insira o primeiro valor (número inteiro): "))
valor2 = int(input("Insira o segundo valor (número inteiro): "))

    # Diferença entre os dois valores inseridos
    if valor1 > valor2:
        print(f"\n{valor1} é maior que {valor2}")
    elif valor1 < valor2:
        print(f"\n{valor1} é menor que {valor2}")
    else:
        print("\nOs dois valores são iguais.")
except ValueError:
    # Caso o usuário insira algo que não seja um número inteiro
    print("\nErro: Por favor, insira apenas números inteiros válidos.")
