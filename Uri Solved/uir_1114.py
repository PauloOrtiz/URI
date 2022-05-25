Senha = False

while not Senha:

    Acesso = int(input())

    if(Acesso == 2002):
        print("Acesso Permitido")
        Senha = True
    else:
        print("Senha Invalida")