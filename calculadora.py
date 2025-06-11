# Criador Douglas Magalhães de Vasconcelos
# Calculadora basica em python3 usando clases (class) e funções (def)

from Calculadora import funcoes_aritmeticas as Calc

def calculadora():
    while True:
        try:
            escolha = input("Escolha uma opção aritmetica (1/2/3/4 ou '0' para sair): ")

            if escolha == '0':
                print("Programa encerrado com sucesso!")
                break

            if escolha in ['1','2','3','4']:
                number_1 = float(input("Digite um número: "))
                number_2 = float(input("Digite um número: "))
                calc = Calc(number_1, number_2)
            else:
                raise ValueError("Entrada invalida!")
            
            if escolha == '1':
                resultado = calc.somar()
                print(f"- A soma de {number_1} + {number_2} = {resultado:0.2f}\n")
            elif escolha == '2':
                resultado = calc.subtrair()
                print(f"- A subtração de {number_1} - {number_2} = {resultado:0.2f}\n")
            elif escolha == '3':
                resultado = calc.multiplicar()
                print(f"- A multiplicação de {number_1} * {number_2} = {resultado:0.2f}\n")
            elif escolha == '4':
                resultado = calc.dividir()
                if resultado is not None:
                    print(f"- A divisão de {number_1} / {number_2} = {resultado:0.2f}\n")
        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
        calculadora()
