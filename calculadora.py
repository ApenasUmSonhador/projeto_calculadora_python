numero_1=0
numero_2=0
operador=''
while True:
    numero_1= input("Digite um numero: ")
    operador= input("Digite um operador (entre: +, -,*,/, ^): ")
    numero_2= input("Digite outro numero: ")
    while not numero_1.isnumeric() or not numero_2.isnumeric():
        print("Tente novamente, os numeros foram considerados invalidos.")
        numero_1= input("Digite um numero: ")
        operador= input("Digite um operador: ")
        numero_2= input("Digite outro numero: ")
    num_1=float(numero_1)
    num_2=float(numero_2)
    operadores_validos='+-/**'
    while operador not in operadores_validos:
        print("Tente novamente, o operador foi considerado invalido.")
        numero_1= input("Digite um numero: ")
        operador= input("Digite um operador: ")
        numero_2= input("Digite outro numero: ")
    if operador == '+':
        print(f'{num_1} + {num_2} = {num_1+num_2}')
    elif operador == '-':
        print(f'{num_1} - {num_2} = {num_1-num_2}')
    elif operador == '*':
        print(f'{num_1} * {num_2} = {num_1*num_2}')
    elif operador == '/':
        print(f'{num_1} / {num_2} = {num_1/num_2}')
    elif operador == '^':
        print(f'{num_1} ** {num_2} = {num_1**num_2}')
    sair = input("Quer sair?\n [s]im [n]ao: ").lower().startswith('s')
    if sair is True:
        break
