
# Conversor de Temperaturas

from ASCII_Arts import print_sol # Import da ASCII Art




def menu_temperaturas(): # Menu

    print_sol()




    print("_________Menu________")
    print("Celsius P/ Fahrenheit = *1*")
    print("Fahrenheit P/ Celsius = *2*")
    print("Celsius P/ Kelvin     = *3*")
    print("Kelvin P/ Celsius     = *4*")
    print("Fahrenheit P/ Kelvin  = *5*")
    print("Kelvin P/ Fahrenheit  = *6*")
    print("     *Sair = 0*")




def seletor(): # Função para chamar o menu e habilitar funções de sair e ValueError
    while True:
        menu_temperaturas()
        opcao = input("  Digite uma opção: ") # Input para selecionar opção




        if opcao == "0":
            print("Over...")
            break




        valor = float(input("Digite o valor que deseja converter: ")) # Input para o valor desejado




        if opcao == "1": # Celsius para Fahrenheit
            resultado = (valor * 9/5 + 32)
            print(f"   ----{resultado:.2f}°F----")

        elif opcao =="2": # Fahrenheit para Celsius
            resultado = ((valor - 32) * 5/9)
            print(f"   ----{resultado:.2f}°C----")

        elif opcao == "3": # Celsius para Kelvin
            resultado = (valor + 273.15)
            print(f"   ----{resultado:.2f}K----")

        elif opcao == "4": # Kelvin para Celsius
            resultado = (valor - 273.15)
            print(f"   ----{resultado}°C----")

        elif opcao == "5": # Fahrenheit para Kelvin
            resultado =((valor - 32) * 5/9 + 273.15)
            print(f"   ----{resultado:.2f}K----")

        elif opcao == "6": # Kelvin para Fahrenheit
            resultado = ((valor - 273.15) * 9/5 + 32)
            print(f"   ----{resultado}°F----")



if __name__ == "__main__":
    seletor()
