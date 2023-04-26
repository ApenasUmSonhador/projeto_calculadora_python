#Importando bilbliotecas:
from math import tan, sin, cos, radians ; from os import name, system
#Declarando Variáveis:
#Booleanos usados nos loops.
algoritmo = True; conversor = False; calculadora = False; complementando = False

#Calculadora:
#Lista com operadores que necessitam apenas de 1 número.
OPERADORES_1NUM = ['!','sen', 'cos', 'tg', 'cossec', 'sec', 'cotg'] 
#Lista com operadores que necessitam de 2 números.
OPERADORES_2NUM = ['+', '-','/','*','%','^','raiz', 'hiper'] 
#Inicializando números e operador.
numero_1 = 0; numero_2 = 0; operador='' 

#Conversor:
#Escolha das Operações:
CONVERSOES = ['A', 'B',' C', "D"]
#Lista com Bases que são aceitas.
TIPOS_DE_BASE = [2,8,10,16]
#Inicializando bases
binario = ""; octal = ""; decimal = ""; hexadecimal = ""; gray = ""; complementar_1 =""; complementar_2 =""; bcd=""


#Declarando funções:
def limpar():#Responsável por limpar o terminal.
    #Conferindo qual o tipo de sistema operacional:
    if name == "nt":#Windows
        system('cls')
        
    else:#Linux
        system('clear')

def operacao_1num(numero_1):#Responsável por realizar as operações com 1 número.
    if operador == '!':#Operação Fatorial.
        num_1=int(numero_1)
        resultado = 1
        
        for i in range(num_1):
            resultado *= (i+1)
            
        print(f'{num_1}! = {resultado}')

    else:#Operações trigométricas:
        num_1 = float(numero_1)
        num_2= radians(num_1)

        if operador =='sen':#Operação Seno.
            print(f'sen({num_1}) = {sin(num_2)}')
            
        elif operador =='cos':#Operação Cosseno.
            print(f'cos({num_1}) = {cos(num_2)}')
            
        elif operador =='tg':#Operação Tangente.
            print(f'tg({num_1}) = {tan(num_2)}')
            
        elif operador =='sec':#Operação Secante.
            print(f'sec({num_1}) = {1/cos(num_2)}')
                
        elif operador =='cossec':#Operação Cossecante.
            print(f'cossec({num_1}) = {1/sin(num_2)}')
            
        elif operador =='cotg':#Operação Cotangente.
            print(f'cotg({num_1}) = {1/tan(num_2)}')
        
def operacao_2num(numero_1):#Responsável por realizar as operações com 2 números.
    numero_2= input("Digite outro número: ").strip()
    
    if numero_2.isnumeric():
        num_1=float(numero_1)
        num_2=float(numero_2)

        #Operação Soma.
        if operador == '+':
            print(f'{num_1} + {num_2} = {num_1+num_2}')

        #Operação Subtração.
        elif operador == '-':
            print(f'{num_1} - {num_2} = {num_1-num_2}')

        #Operação Multiplicação.
        elif operador == '*':
            print(f'{num_1} * {num_2} = {num_1*num_2}')

        #Operação Divisão.
        elif operador == '/':
            print(f'{num_1} / {num_2} = {num_1/num_2}')

        #Operação Potênciação.
        elif operador == '^':
            print(f'{num_1} ^ {num_2} = {num_1**num_2}')

        #Operação Modular.
        elif operador == '%':
            print(f'{num_1} % {num_2} = {num_1%num_2}')

        #Operação Radiciação.
        elif operador == 'raiz':
            print(f'A {num_2}ª raiz de {num_1} = {num_1**(1/num_2)}')
        
        #Operação Tetração.
        elif operador == 'hiper':
            num_2= int(num_2)
            indice = num_1
            i = 0
            while i < num_2:
                num_1= num_1**indice
                print(f'{numero_1} hiper {num_2} = {num_1}')
                i+=1

        #Tratando possível erro na entrada da variável "operador".
        else:
            print("Tente novamente, o operador foi considerado invalido.")

    #Tratando possível erro na entrada da variável "numero_2".
    else:
        print("Tente novamente, o número foi considerado invalido.")

#Responsável por converter Decimal -> Binário.            
def decimal_para_binario(decimal):
    binario = ""
    while decimal > 0:
        if decimal % 2 == 1:
            binario = "1" + binario
            
        else:
            binario = "0" + binario
            
        decimal //= 2
        
    return binario

#Responsável por converter Decimal -> Octal.
def decimal_para_octal(decimal):
    octal = ""

    while decimal > 0:
        if decimal % 8 != 0:
            octal = str(decimal % 8) + octal
        else:
            octal = "0" + octal
        decimal //= 8
    return octal

#Responsável por converter Decimal -> Hexadecimal.
def decimal_para_hexadecimal(decimal):
    hexadecimal = ""

    while decimal > 0:
        if decimal % 16 == 15:
            hexadecimal = "F" + hexadecimal

        elif decimal % 16 == 14:
            hexadecimal = "E" + hexadecimal

        elif decimal % 16 == 13:
            hexadecimal = "D" + hexadecimal

        elif decimal % 16 == 12:
            hexadecimal = "C" + hexadecimal

        elif decimal % 16 == 11:
            hexadecimal = "B" + hexadecimal

        elif decimal % 16 == 10:
            hexadecimal = "A" + hexadecimal

        else:
            if decimal % 16 != 0:
                hexadecimal = str(decimal % 16) + hexadecimal

            else:
                hexadecimal = "0" + hexadecimal

        decimal //= 16

    return hexadecimal

#Responsável por converter Binário -> Decimal.
def binario_para_decimal(binario):
    decimal = 0
    binario = binario[::-1]

    for i in range(len(binario)):
        decimal += int(binario[i]) *  (2** i)

    return decimal

#Responsável por converter Octal -> Decimal.
def octal_para_decimal(octal):
    decimal = 0
    octal = octal[::-1]

    for i in range(len(octal)):
        decimal += int(octal[i])* (8 ** i)

    return decimal

#Responsável por converter Hexadecimal -> Decimal.
def hexadecimal_para_decimal(hexadecimal):
    decimal = 0
    hexadecimal = hexadecimal[::-1]

    for i in range(len(hexadecimal)):
        if hexadecimal[i] == "A":
            decimal += 10 * (16 ** i)

        elif hexadecimal[i] == "B":
            decimal += 11 * (16 ** i)

        elif hexadecimal[i] == "C":
            decimal += 12 * (16 ** i)

        elif hexadecimal[i] == "D":
            decimal += 13 * (16 ** i)

        elif hexadecimal[i] == "E":
            decimal += 14 * (16 ** i)

        elif hexadecimal[i] == "F":
            decimal += 15 * (16 ** i)

        else:
            decimal += int(hexadecimal[i]) * (16 ** i)

    return decimal

#Responsável por converter Binário -> Gray.
def binario_para_gray(binario):
    gray = binario[0]
    for i in range(0,len(binario)-1):
        if ((binario[i]=="1" or binario[i+1]=="1") and (not binario[i]=="1" or not binario[i+1]=="1")):
            gray = gray + "1"
        else:
            gray = gray + "0"
        i+=1
    return gray

#Responsável por converter Binário -> Complementar 1.
def binario_para_complementar_1(binario):
    complementar_1 = ""
    for i in range(0,len(binario)):
        if binario[i]=="1":
            complementar_1 = complementar_1 + "0"
        else:
            complementar_1 = complementar_1 + "1"
    return complementar_1

#Responsável por converter Binário -> Complementar 2
def complementar_1_para_complementar_2(complementar_1):
    complementar_2= ""
    complementar_1 = complementar_1[::-1]
    complementando = False
    for i in range(0,len(complementar_1)):
        if complementando == False:
            if(complementar_1[i]=="1"):
                complementar_2 = complementar_2 + "0"
                if i == len(complementar_1)-1:
                    complementar_2 = complementar_2 + "1"
            else:
                complementar_2 = complementar_2 + "1"
                complementando = True
        else:
            complementar_2 = complementar_2 + complementar_1[i]
    complementar_2 = complementar_2[::-1]
    return complementar_2

#Responsável por converter Decimal -> BCD.
def decimal_para_bcd(decimal):
    bcd = ""
    decimal = str(decimal)
    for i in range(len(decimal)):
        bcd = "0"*(4-i) + decimal_para_binario(int(decimal[i])) + bcd
    bcd = bcd[::-1]
    return bcd

def tira_0_esquerda(numero):
    numero_tratado = numero
    for i in range(0,len(numero)):
        if numero_tratado[0] == "0":
            numero_tratado=""
            for u in range(i,len(numero)):
                numero_tratado += numero[u]
        else:
            return numero_tratado


#Tutorial:
#Inicializando booleano que define se será ou não exibido o tutorial.
tutorial = False 
texto_tutorial ='\
Esse algoritmo foi desenvolvida utilizando a linguagem de programação Python3, portanto, para usufruir da melhor maneira possível, deve-se seguir algumas regras.\
        \nNos locais em que existem decisões de sim ou nao, caso coloque algo invalido, adotaremos como um "NÃO". \
        \n0: Como escolher o que utilizar:\
        \n0.1: Para escolher utilizar a Calculadora, quando pedido, digite "A". \
        \n0.2: Para escolher utilizar a Conversor, quando pedido, digite "B". \
        \n\n1: Como utilizar a Calculadora: \
        \n1.1: Serão pedidos números para a realização das operações. Nesses espaços digite APENAS números, salvo 2 exceções:\
        \n     Angulos: adote sempre os angulos em graus.\
        \n     Negativos: use o " - " antes de digitar os números (exemplo: -14);\
        \n     Decimais: utilize o " . " para separar a parte inteira de um número de sua parte racional(exemplo: 3.14)  \
        \n1.2: Será pedido o operador matemático de interesse, para usar de maneira devida digite APENAS UM operador por vez, utilizando operadores entre: [!,sen, cos, tg, cossec, sec, cotg] e [+, -, /, *, %, ^, raiz, hiper]. \
        \n1.3: Após a operação, será apresentado o resultado e a pergunta se quer sair ou não da calculadora. Para continuar digite "s", caso contrário digite "n".\
        \n1.4: Ocorra algum erro, será perguntado se deseja sair da calculadora e caso permaneça, recomeça tudo novamente.\
        \n\n2: Como utilizar o Conversor: \
        \n2.1: Quando pedido, digite, utilizando APENAS números, qual o tipo de base estará o número a ser convertido. \
        \n2.2: Quando pedido, digite, utilizando APENAS os bits que a base aceita (exemplo: Binario - utilize apenas 0s e 1s),  o número que será convertido para as outras bases.\
        \n2.3. Serão exibidos os números pós-conversão.\
        \n2.4. Quando pedido, digite, utilizando apenas UMA letra ("n" ou "s"), se deseja continuar convertendo ou não, se quiser continuar digite "s", caso contrário digite "n".\n' 
tutorial= input("Deseja ver o tutorial de como utilizar o algoritmo?\n [S]im [N]ao: ").strip().lower().startswith('s')

if tutorial is True:
    limpar()
    print(texto_tutorial)
else:
    limpar()

#Algoritmo:
while algoritmo is True:
    conversor = input("O que deseja utilizar? \n [A]Calculadora [B]Conversor de bases\n").strip().lower().startswith('b')
    limpar()
    
    #Calculadora:
    if conversor is False: 
        calculadora = True
        
        #Loop para caso o usuário queira continuar utilizando a Calculadora.
        while calculadora is True:
            #Reiniciando as variavéis:
            numero_1=0
            numero_2=0
            operador=''

            numero_1= input("Digite um número: ").strip()
            limpar()
            
            if numero_1.isnumeric():
                operador= input("Digite um operador: ").strip().lower()
                limpar()

                #Operações que dependem de apenas um número.
                if operador in OPERADORES_1NUM:
                    operacao_1num(numero_1)

                #Operações que dependem de dois números.
                elif operador in OPERADORES_2NUM:
                    limpar()
                    operacao_2num(numero_1)

            #Tratando possível erro na entrada da variável "numero_1".
            else:
                print("Tente novamente, o número foi considerado invalido.")
                
            #Decisão do usuário alterando a variável "conversor" para: False caso queira parar de usar a calculadora, ou True caso queira continuar utilizando-a.
            continuar = input("Deseja continuar utilizando a Calculadora? \n[s]im [n]ao: ").lower().strip().startswith("s")
            if continuar == False:
                calculadora = False
                limpar()
            
    #Conversor:
    else:
        calculadora = False
        
        #Loop para caso o usuário queira continuar utilizando o Conversor.
        while conversor is True:
            #Reiniciando as variáveis:   
            binario = ""; octal = ""; decimal = ""; hexadecimal = ""; gray = ""; complementar_1 =""; complementar_2 =""

            #Recebendo o que usuário deseja fazer:
            acao =input("Qual ferramenta deseja utilizar? \n[A]Conversor de bases [B]Conversor para Gray [C]Conversor para Complementares [D]Conversor para BCD\n").strip().lower()

            #Conversor de bases:
            if acao == "a":
                #Recebendo qual a base do número a ser convertido:
                base = int(input("Insira qual o número da base de entrada.\n[2] [8] [10] [16]: "))

                #Entrada em base Decimal.
                if base == 10:
                    numero_entrada = input("Insira o número na base decimal:\n")

                    decimal = int(numero_entrada)
                    binario = decimal_para_binario(decimal)
                    octal = decimal_para_octal(decimal)
                    hexadecimal = decimal_para_hexadecimal(decimal)

                    limpar()
                    print(f"Em binário: {binario}\nEm octal: {octal}\nEm decimal: {decimal}\nEm hexadecimal: {hexadecimal}")
                    
                #Entrada em base Binária.
                elif base == 2:
                    numero_entrada = input("Insira o número na base binaria:\n")
                    numero_entrada = tira_0_esquerda(numero_entrada)
                    binario = numero_entrada
                    decimal = int(binario_para_decimal(binario))
                    octal = decimal_para_octal(decimal)
                    hexadecimal = decimal_para_hexadecimal(decimal)

                    limpar()
                    print(f"Em binário: {binario}\nEm octal: {octal}\nEm decimal: {decimal}\nEm hexadecimal: {hexadecimal}")

                #Entrada em base Octal.
                elif base == 8:
                    numero_entrada = input("Insira o número na base octal: \n")
                    numero_entrada = tira_0_esquerda(numero_entrada)
                    octal = numero_entrada
                    decimal = int(octal_para_decimal(octal))
                    binario = decimal_para_binario(decimal)
                    hexadecimal=decimal_para_hexadecimal(decimal)

                    limpar()
                    print(f"Em binário: {binario}\nEm octal: {octal}\nEm decimal: {decimal}\nEm hexadecimal: {hexadecimal}")
                
                #Entrada em base Hexadecimal.
                elif base == 16:
                    numero_entrada = input("Insira o número na base hexadecimal: \n")
                    numero_entrada = tira_0_esquerda(numero_entrada)
                    hexadecimal = numero_entrada
                    decimal = int(hexadecimal_para_decimal(hexadecimal))
                    binario = decimal_para_binario(decimal)
                    octal = decimal_para_octal(decimal)

                    limpar()
                    print(f"Em binário: {binario}\nEm octal: {octal}\nEm decimal: {decimal}\nEm hexadecimal: {hexadecimal}")
                
                #Tratando erro na entrada do tipo de base.
                else:
                    print("Ocorreu um erro ao inserir o número da base de início, utilize apenas números, digitando exatamente o que estiver entre os colchetes.")
            
            #Conversor para Gray:
            elif acao == "b":
                numero_entrada = input("Insira o número na base binaria:\n")
                numero_entrada = tira_0_esquerda(numero_entrada)
                binario = numero_entrada
                gray = binario_para_gray(binario)
                limpar()
                print(f"Binário: {binario} \n Seu Gray: {gray}")

            #Conversor para Complementares:
            elif acao == "c":
                numero_entrada = input("Insira o número na base binaria:\n")
                numero_entrada = tira_0_esquerda(numero_entrada)
                binario = numero_entrada
                complementar_1 = binario_para_complementar_1(binario)
                complementar_2 = complementar_1_para_complementar_2(complementar_1)
                limpar()
                print(f"Binário: {binario} \nSeu Complementar 1: {complementar_1} \nSeu Complementar 2: {complementar_2}")

            #Conversor para BCD:
            elif acao == "d":
                base = int(input("Insira qual o número da base de entrada.\n[2] [8] [10] [16]: "))

                #Entrada em base Decimal.
                if base == 10:
                    numero_entrada = input("Insira o número na base decimal:\n")
                    decimal = int(numero_entrada)
                    bcd = decimal_para_bcd(decimal)
                    limpar()
                    print(f"O número de entrada na base [{base}] é {numero_entrada}\nSeu BCD é: {bcd}")
                    
                #Entrada em base Binária.
                elif base == 2:
                    numero_entrada = input("Insira o número na base binaria:\n")
                    numero_entrada = tira_0_esquerda(numero_entrada)
                    binario = numero_entrada
                    decimal = int(binario_para_decimal(binario))
                    bcd = decimal_para_bcd(decimal)

                    limpar()
                    print(f"O número de entrada na base [{base}] é {numero_entrada}\nSeu BCD é: {bcd}")

                #Entrada em base Octal.
                elif base == 8:
                    numero_entrada = input("Insira o número na base octal: \n")
                    numero_entrada = tira_0_esquerda(numero_entrada)
                    octal = numero_entrada
                    decimal = int(octal_para_decimal(octal))
                    bcd = decimal_para_bcd(decimal)
                    
                    limpar()
                    print(f"O número de entrada na base [{base}] é {numero_entrada}\nSeu BCD é: {bcd}")
                
                #Entrada em base Hexadecimal.
                elif base == 16:
                    numero_entrada = input("Insira o número na base hexadecimal: \n")
                    numero_entrada = tira_0_esquerda(numero_entrada)
                    hexadecimal = numero_entrada
                    decimal = int(hexadecimal_para_decimal(hexadecimal))
                    bcd = decimal_para_bcd(decimal)

                    limpar()
                    print(f"O número de entrada na base [{base}] é {numero_entrada}\nSeu BCD é: {bcd}")

                #Tratando erro na entrada do tipo de base.
                else:
                    print("Ocorreu um erro ao inserir o número da base de início, utilize apenas números, digitando exatamente o que estiver entre os colchetes.")

            #Tratando erro de entrada na variável "acao":
            else:
                print("Ocorreu um erro ao inserir qual a ferramenta que deseja utilizar, tente novamente.")
            #Decisão do usuário alterando a variável "conversor" para: False caso queira parar de usar o conversor, ou True caso queira continuar utilizando-o.
            continuar = input("Deseja continuar convertendo? \n[s]im [n]ao: ").lower().strip().startswith("s")
            if continuar == False:
                conversor = False
                limpar()

    #Decisão do usuário alterando a variável "continuar" para: False caso queira parar de usar o algoritmo, ou True caso queira continuar utilizando-o.
    continuar = input("Deseja continuar utlizando o algoritmo?\n [S]im [N]ao: ").strip().lower().startswith("s")
    if continuar == False:
        algoritmo = False
