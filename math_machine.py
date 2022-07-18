import math
def potencia():
    base = int(input("\nvalor da base: "))
    exp = int(input("\nvalor do expoente: "))
    potencia = 1
    cont = 1
    while cont <= exp:
        potencia *= base
        cont += 1
    return print("\no valor final é igual a", potencia)

def porcentagem():
    num = float(input("\ndigite o número: \n"))
    porc = float(input("\ndigite a porcentagem que quer desse número: \n"))
    calculo = (porc/100) * num
    return print("\na % é igual a ", calculo)

def areas():
    print("\nqual a figura que quer calcular a área? \n")
    print("1 - retângulo")
    print("2 - triângulo")
    print("3 - círculo")
    figura = str(input("\nescolha a sua opção: \n"))
    
    if(figura == '1'):
        altura = float(input("\ndigite a altura do retângulo: \n"))
        base = float(input("\ndigite a base do retângulo: \n"))
        area_ret = base * altura
        return print("\na área é igual a ", area_ret)
    elif(figura == '2'):
        altura = float(input("\ndigite a altura do triângulo: \n"))
        base = float(input("\ndigite a base do triângulo: \n"))
        area_tri = (base * altura) / 2
        return print("\na área é igual a ", area_tri)
    elif(figura == '3'):
        raio = float(input("\ndigite o raio do círculo: \n"))
        area_circ = math.pi * raio ** 2
        return print("\na área é igual a ", area_circ)

print("\nbem vindo ao programa matemático !!!")

def menu():
    print("\nescolha entre as opções abaixo: \n")
    print("1 - porcentagem")
    print("2 - áreas")
    print("3 - potência")
    opc = str(input("\ndigite a sua opção: \n"))

    if(opc == '1'):
        porcentagem()
    if(opc == '2'):
        areas()
    if(opc == '3'):
        potencia()

while True:
    menu()
    saida = str(input("\ndeseja sair do programa? \n\n1 - sim \n0 - não \n"))
    while saida != '1' and saida != '0':
        saida = str(input("\nescolha uma opção válida!: \n"))
    if(saida == '1'):
        print("\nobrigado por usar o nosso programa !!! <3")
        break
