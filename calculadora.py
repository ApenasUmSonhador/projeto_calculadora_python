'''
Planos para o futuro:
    1.Aceitar outros operadores como: log, sqrt e binomio de newtown.
    2.Pedir mais ideias para usuários.
'''
import math
tutorial = True
continuar = True
operadores_1num= ['!','sen', 'cos', 'tg', 'cossec', 'sec', 'cotg']
operadores_2num = ['+', '-','/','*','%','^', 'hiper']
numero_1=0
numero_2=0
operador=''

tutorial= input("Deseja ver o tutorial de como funciona a calculadora?\n [s]im [n]ao: ").strip().lower().startswith('s')
if tutorial is True:
    print(f'Essa calculadora foi desenvolvida utilizando a linguagem de programação Python3, portanto, para usufruir da melhor maneira possível, deve-se seguir algumas regras.\
        \n1.Serão pedidos números para a realização das operações. Nesses espaços digite APENAS números, salvo 2 exceções:\
        \n Angulos: adote sempre os angulos em graus.\
        \n Negativos: use o " - " antes de digitar os números (exemplo: -14);\
        \n Decimais: utilize o " . " para separar a parte inteira de um número de sua parte racional(exemplo: 3.14)  \
        \n2.Será pedido o operador matemático de interesse, para usar de maneira devida digite APENAS UM operador por vez, utilizando operadores entre: {operadores_1num} e {operadores_2num} \
        \n3.Após a operação, será apresentado o resultado e a pergunta se quer sair ou não da calculadora. Para continuar digite s ou sim, para sair; digite n ou não, para continuar utilizando a calculadora.\
        \n4.Nos locais em que existem decisoes de sim ou nao, caso coloque algo invalido, adotaremos como um "NAO". \
        \n5.Ocorra algum erro, será perguntado se deseja sair da calculadora e caso permaneça, recomeça tudo novamente.')
while continuar is True:
    numero_1= input("Digite um numero: ").strip()
    if not numero_1.isnumeric():
        print("Tente novamente, o numero foi considerado invalido.")
     #Operaçoes que dependem APENAS de um numero.
    else:
        operador= input("Digite um operador: ").strip().lower()
        if operador in operadores_1num:
            if operador == '!':
                num_1=int(numero_1)
                resultado = 1
                for i in range(num_1):
                    resultado *= (i+1)
                print(f'{num_1}! = {resultado}')
            elif operador =='sen':
                num_1 = float(numero_1)
                num_2= math.radians(num_1)
                print(f'sen({num_1}) = {math.sen(num_2)}')
            elif operador =='cos':
                num_1 = float(numero_1)
                num_2= math.radians(num_1)
                print(f'cos({num_1}) = {math.cos(num_2)}')
            elif operador =='tg':
                num_1 = float(numero_1)
                num_2= math.radians(num_1)
                print(f'tg({num_1}) = {math.tg(num_2)}')
            elif operador =='sec':
                num_1 = float(numero_1)
                num_2= math.radians(num_1)
                print(f'sec({num_1}) = {1/math.cos(num_2)}')
            elif operador =='cossec':
                num_1 = float(numero_1)
                num_2= math.radians(num_1)
                print(f'cossec({num_1}) = {1/math.sen(num_2)}')
            elif operador =='cotg':
                num_1 = float(numero_1)
                num_2= math.radians(num_1)
                print(f'cotg({num_1}) = {1/math.tg(num_2)}')
    #Operaçoes que dependem de 2 numeros.
        elif operador in operadores_2num:
            numero_2= input("Digite outro numero: ").strip()
            if not numero_2.isnumeric():
                print("Tente novamente, o numero foi considerado invalido.")
            else:
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
                elif operador == 'hiper':
                    num_2= int(num_2)
                    indice = num_1
                    for i in range(0,num_2):
                        num_1= num_1**indice
                    print(f'{numero_1} hiper {num_2} = {num_1}')
        else:
            print("Tente novamente, o operador foi considerado invalido.")
    sair = input("Deseja sair?\n [s]im [n]ao: ").strip().lower().startswith('s')
    if sair is True:
        continuar = False
