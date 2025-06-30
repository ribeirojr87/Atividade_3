# Solicita a idade ao usuário
try:
    idade = int(input("Por favor, digite sua idade: "))

    # Classifica a idade com base nas categorias
    if 0 <= idade <= 12:
        categoria = "Criança"
    elif 13 <= idade <= 17:
        categoria = "Adolescente"
    elif 18 <= idade <= 59:
        categoria = "Adulto"
    elif idade >= 60:
        categoria = "Idoso"
    else:
        categoria = "Idade inválida (não pode ser negativa)"

    # Exibe a classificação
    print(f"Você se encaixa na categoria: {categoria}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para a idade.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")