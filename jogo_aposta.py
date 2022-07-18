from random import randint
maqnum = randint(0, 21)
def maquina():
    usunum = int(input("Que tal uma aposta!? Insira um número entre 0 e 20: \n"))
    while True:
        if(maqnum > usunum):
            print("\naumente a sua aposta. \n")
            repetir = str(input("\nquer repetir o jogo? s ou n: \n"))
            if(repetir == 'n' or repetir == 'N'):
                print("\nbye")
                exit()
            if(repetir == 's' or 'S'):
                usunum = int(input("\ninsira um número entre 0 e 20: \n"))
        if(maqnum < usunum):
            print("\ndiminua sua aposta. \n")
            repetir = str(input("\nquer repetir o jogo? s ou n: \n"))
            if(repetir == 'n' or repetir == 'N'):
                print("\nbye")
                exit()
            if(repetir == 's' or 'S'):
                usunum = int(input("\ninsira um número entre 0 e 20: \n"))
        if(maqnum == usunum):
            print("\nacertou! parabéns.")
            exit()
maquina()