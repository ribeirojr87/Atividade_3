# Solicita o peso e a altura ao usuário
try:
    peso = float(input("Por favor, digite seu peso em kg (ex: 70.5): "))
    altura = float(input("Por favor, digite sua altura em metros (ex: 1.75): "))

    # Verifica se os valores são válidos (não negativos)
    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser valores positivos. Por favor, tente novamente.")
    else:
        # Calcula o IMC
        imc = peso / (altura ** 2)

        # Classifica o IMC de acordo com a tabela padrão
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"

        # Exibe o resultado
        print(f"\nSeu IMC é: {imc:.2f}") # O :.2f formata para 2 casas decimais
        print(f"Sua classificação é: {classificacao}")

except ValueError:
    print("Entrada inválida. Por favor, digite números para peso e altura.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")