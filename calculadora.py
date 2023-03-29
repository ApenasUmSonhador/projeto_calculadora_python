'''
Planos para o futuro:
    1.Aceitar outros operadores como: log, sqrt, binomio de newtown,cos, sen,tg,cotg,cossec,tetração,e fatorial.
    2.Pedir mais ideias para usuários.
'''
tutorial = True
continuar = True
operadores_validos='+-/*^%'
numero_1=0
numero_2=0
operador=''

tutorial= input("Deseja ver o tutorial de como funciona a calculadora?\n [s]im [n]ao: ").strip().lower().startswith('s')
if tutorial is True:
    print('Essa calculadora foi desenvolvida utilizando a linguagem de programação Python3, portanto, para usufruir da melhor maneira possível, deve-se seguir algumas regras.\
        \n1.Serão pedidos números para a realização das operações. Nesses espaços digite APENAS números, salvo 2 exceções:\
        \n Negativos: use o " - " antes de digitar os números (exemplo: -14);\
        \n Decimais: utilize o " . " para separar a parte inteira de um número de sua parte racional(exemplo: 3.14)  \
        \n2.Será pedido o operador matemático de interesse, para usar de maneira devida digite APENAS UM operador por vez, utilizando os símbolos apresentados no próprio texto que pede o operador. \
        \n3.Após a operação, será apresentado o resultado e a pergunta se quer sair ou não da calculadora. Para continuar digite s ou sim, para sair; digite n ou não, para continuar utilizando a calculadora.\
        \n4.Nos locais em que existem decisoes de sim ou nao, caso coloque algo invalido, adotaremos como um "NAO".')

while continuar is True:
    numero_1= input("Digite um numero: ").strip()
    operador= input("Digite um operador (entre: +, -,*,/, ^): ").strip()
    numero_2= input("Digite outro numero: ").strip()
    while not numero_1.isnumeric() or not numero_2.isnumeric():
        print("Tente novamente, os numeros foram considerados invalidos.")
        numero_1= input("Digite um numero: ").strip()
        operador= input("Digite um operador: ").strip()
        numero_2= input("Digite outro numero: ").strip()
    while operador not in operadores_validos or len(operador)>1:
        print("Tente novamente, o operador foi considerado invalido.")
        numero_1= input("Digite um numero: ").strip()
        operador= input("Digite um operador: ").strip()
        numero_2= input("Digite outro numero: ").strip()
    num_1=float(numero_1)
    num_2=float(numero_2)
    if operador == '+':
        print(f'{num_1} + {num_2} = {num_1+num_2}')
    elif operador == '-':
        print(f'{num_1} - {num_2} = {num_1-num_2}')
    elif operador == '*':
        print(f'{num_1} * {num_2} = {num_1*num_2}')
    elif operador == '/':
        print(f'{num_1} / {num_2} = {num_1/num_2}')
    elif operador == '^':
        print(f'{num_1} ^ {num_2} = {num_1**num_2}')
    elif operador == '%':
        print(f'{num_1} % {num_2} = {num_1%num_2}')
    sair = input("Quer sair?\n [s]im [n]ao: ").strip().lower().startswith('s')
    if sair is True:
        continuar = False
