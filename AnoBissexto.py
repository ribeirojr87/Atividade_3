def verificar_ano_bissexto():
    print("--- Verificador de Ano Bissexto ---")

    try:
        ano = int(input("Digite o ano (ex: 2024): "))

        # Um ano é bissexto se:
        # 1. É divisível por 4 E NÃO é divisível por 100
        # OU
        # 2. É divisível por 400
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"O ano {ano} É bissexto!")
        else:
            print(f"O ano {ano} NÃO é bissexto.")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um NÚMERO inteiro para o ano.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Inicia o verificador
verificar_ano_bissexto()