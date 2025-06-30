# Conversor de Temperatura

def converter_temperatura_simples():
    print("--- Conversor de Temperatura ---")
    print("Unidades: C (Celsius), F (Fahrenheit), K (Kelvin)")

    try:
        temp = float(input("Digite a temperatura: "))
        origem = input("De qual unidade? (C, F, K): ").upper()
        destino = input("Para qual unidade? (C, F, K): ").upper()

        if origem == destino:
            print(f"{temp:.2f} {origem} já está na unidade desejada.")
            return

        resultado = None

        # Converter tudo para Celsius primeiro para simplificar
        temp_celsius = 0
        if origem == 'C':
            temp_celsius = temp
        elif origem == 'F':
            temp_celsius = (temp - 32) * 5/9
        elif origem == 'K':
            temp_celsius = temp - 273.15
        else:
            print("Unidade de origem inválida. Use C, F ou K.")
            return

        # Agora converter de Celsius para a unidade de destino
        if destino == 'C':
            resultado = temp_celsius
        elif destino == 'F':
            resultado = (temp_celsius * 9/5) + 32
        elif destino == 'K':
            resultado = temp_celsius + 273.15
        else:
            print("Unidade de destino inválida. Use C, F ou K.")
            return

        if resultado is not None:
            print(f"\n{temp:.2f} {origem} é igual a {resultado:.2f} {destino}")

    except ValueError:
        print("Erro: Digite um NÚMERO para a temperatura.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Inicia o conversor
converter_temperatura_simples()