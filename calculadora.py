#Importando bilbliotecas:
from math import tan, sin, cos, radians ; from os import name, system

#DECLARANDO VARIÁVEIS:
#Booleanos usados nos loops.
algoritmo = True ; conversor = False ; calculadora = False ; complementando = False
#Variável usada para selecionar a ferramenta.
ferramenta = ""

#Calculadora:
#Lista com operadores que necessitam apenas de 1 número.
OPERADORES_1NUM = '!','sen', 'cos', 'tg', 'cossec', 'sec', 'cotg'
#Lista com operadores que necessitam de 2 números.
OPERADORES_2NUM = '+', '-','/','*','%','^','raiz', 'hiper'
#Inicializando números e operador.
numero_1 = 0 ; numero_2 = 0 ; operador = '' 

#Conversor:
#Lista com bases que são aceitas.
TIPOS_DE_BASE = 2,8,10,16
#Inicializando bases
binario = "" ; octal = "" ; decimal = "" ; hexadecimal = "" ; gray = "" ; complementar_1 = "" ; complementar_2 = "" ; bcd = ""


#DECLARANDO FUNÇÕES:
#Responsável por limpar o terminal.
def limpar():
    #Conferindo qual o tipo de sistema operacional:
    if name == "nt":#Windows
        system('cls')
        
    else:#Linux
        system('clear')

#Responsável por mostrar créditos do autor.
def creditos():
    limpar()
    
    #Antes de escolher qual ferramenta utilizar.
    if algoritmo == False:
        print("\n------------------- MUITO OBRIGADO -------------------")
        print("    Algoritmo por Arthur Vinicius Carneiro Nunes")
        print( "------------------------ FIM -------------------------\n")
    
    #Utilizando o Conversor.
    elif conversor == True:
        print("\n-------------- CONVERSOR DE BASES -----------------")
        print("    Algoritmo por Arthur Vinicius Carneiro Nunes")
        print( "---------------------------------------------------\n")
    
    #Utilizando a Calculadora.
    elif calculadora == True:
        print("\n------------------- CALCULADORA -------------------")
        print("    Algoritmo por Arthur Vinicius Carneiro Nunes")
        print( "---------------------------------------------------\n")
        
    else:
        print("\n-------------- BEM VINDO AO PROGRAMA --------------")
        print("    Algoritmo por Arthur Vinicius Carneiro Nunes")
        print( "---------------------------------------------------\n")

#Calculadora:
#Responsável por realizar as operações com 1 número.
def operacao_1num(numero_1):
    if operador == '!':#Operação Fatorial.
        num_1=int(numero_1)
        resultado = 1
        
        for i in range(num_1):
            resultado *= (i+1)
            
        print(f'{num_1}! = {resultado}')

    else:#Operações trigométricas:
        num_1 = float(numero_1)
        num_2= radians(num_1)

        #Operação Seno.
        if operador =='sen':
            print(f'sen({num_1}) = {sin(num_2)}')
        
        #Operação Cosseno.
        elif operador =='cos':
            print(f'cos({num_1}) = {cos(num_2)}')
        
        #Operação Tangente.
        elif operador =='tg':
            print(f'tg({num_1}) = {tan(num_2)}')

        #Operação Secante.    
        elif operador =='sec':
            print(f'sec({num_1}) = {1/cos(num_2)}')
                
        #Operação Cossecante.
        elif operador =='cossec':
            print(f'cossec({num_1}) = {1/sin(num_2)}')
            
        #Operação Cotangente.
        elif operador =='cotg':
            print(f'cotg({num_1}) = {1/tan(num_2)}')

#Responsável por realizar as operações com 2 números.       
def operacao_2num(numero_1):
    numero_2= input("Digite outro número: ").strip()

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

#Conversor de bases:
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

#Responsável por tirar os zeros à esquerda.
def tira_0_esquerda(numero):
    numero_tratado = numero
    for i in range(0,len(numero)):
        if numero_tratado[0] == "0":
            numero_tratado = ""
            for u in range(i,len(numero)):
                numero_tratado += numero[u]

        else:
            return numero_tratado


#Tutorial:
tutorial = False 
texto_tutorial = f'-------------- POSSÍVEIS OPERAÇÕES ----------------- \
                \n1.Calculadora:\
                \n1.1.Operações de 1 número:\
                \n{OPERADORES_1NUM} \
                \n1.2.Operações de 2 números:\
                \n{OPERADORES_2NUM} \n\
                \n2.Conversor:\
                \n2.1.Converter para bases 2,8,10 e 16.\
                \n2.2.Converter para Complementares, Gray e BCD.\n\
                \n-------------- ENTRADAS DE DECISÃO -----------------\
                \n1.Digite APENAS o que está entre colchetes.\
                \n2.Não importa se utilizar letra maiúscula ou minúscula.\n\
                \n-------------- ENTRADAS DE NÚMERO ----------------- \
                \n1.Na calculadora:\
                \n1.1.Digite APENAS números reais na base decimal.\
                \n1.2.Utilize o "." para definir parte racional\n\
                \n2.No conversor:\
                \n2.1.Digite apenas números na base selecionada.\
                \n---------------------------------------------------\n'
creditos()
tutorial= input("Deseja ver o tutorial de como utilizar o algoritmo?\n\t         [S]im [N]ao: ").strip().lower().startswith('s')
if tutorial is True:
    creditos()
    print(texto_tutorial)

else:
    creditos()


#Algoritmo:
while algoritmo is True:
    ferramenta = input("\tQual programa deseja utilizar?\
                    \n---------------------------------------------------\
                    \n      [A]Calculadora [B]Conversor de bases: ").strip().lower()
    
    #Calculadora:
    if ferramenta.startswith("a"): 
        calculadora = True
        conversor = False
        
        #Loop para caso o usuário queira continuar utilizando a Calculadora.
        while calculadora is True:
            #Reiniciando as variavéis:
            numero_1 = 0
            numero_2 = 0
            operador = ''

            creditos()
            numero_1 = input("Digite um número: ").strip()
            
            try:
                creditos()
                operador = input("Digite um operador: ").strip().lower()

                #Operações que dependem de apenas um número.
                if operador in OPERADORES_1NUM:
                    creditos()
                    operacao_1num(numero_1)

                #Operações que dependem de dois números.
                elif operador in OPERADORES_2NUM:
                    creditos()
                    operacao_2num(numero_1)
                
                #Operador considerado inválido.
                else:
                    creditos()
                    print("\n-------------------  ERROR ----------------------")
                    print("    Por favor, siga de acordo com o tutorial")
                    print( "---------------------------------------------------\n")

            #Tratando possível erro na entrada da variável "numero_1".
            except ValueError:
                creditos()
                print("\n-------------------  ERROR ----------------------")
                print("    Por favor, siga de acordo com o tutorial")
                print( "---------------------------------------------------\n")
                
            #Decisão do usuário alterando a variável "conversor" para: False caso queira parar de usar a calculadora, ou True caso queira continuar utilizando-a.
            continuar =  input("\n---------------------------------------------------\
                    \n    Deseja continuar utilizando a Calculadora?\
                    \n\t         [S]im [N]ao: ").lower().strip().startswith("s")
            
            if continuar == False:
                calculadora = False
                creditos()
            
    #Conversor de Bases:
    elif ferramenta.startswith("b"):
        conversor = True
        calculadora = False
        
        #Loop para caso o usuário queira continuar utilizando o Conversor.
        while conversor is True:
            #Reiniciando as variáveis:   
            binario = "" ; octal = "" ; decimal = "" ; hexadecimal = "" ; gray = "" ; complementar_1 ="" ; complementar_2 =""
            creditos()

            #Recebendo o que usuário deseja fazer:
            acao = input("\tQual ferramenta deseja utilizar?\
                    \n---------------------------------------------------\
                    \n[A]Conversor de bases [B]Complementares, Gray e BCD\n").strip().lower()

            #Conversor de bases:
            if acao == "a":
                try:
                    creditos()

                    #Recebendo qual a base do número a ser convertido:
                    base = int(input("Insira qual o número da base de entrada.\
                    \n---------------------------------------------------\
                    \n[2] [8] [10] [16]: "))

                    #Entrada em base Decimal.
                    if base == 10:
                        creditos()
                        numero_entrada = input("Insira o número na base decimal:\n")

                        decimal = int(numero_entrada)
                        binario = decimal_para_binario(decimal)
                        octal = decimal_para_octal(decimal)
                        hexadecimal = decimal_para_hexadecimal(decimal)

                        creditos()
                        print(f"Em binário: {binario}\nEm octal: {octal}\nEm decimal: {decimal}\nEm hexadecimal: {hexadecimal}")
                        
                    #Entrada em base Binária.
                    elif base == 2:
                        creditos()
                        numero_entrada = input("Insira o número na base binaria:\n")

                        numero_entrada = tira_0_esquerda(numero_entrada)
                        binario = numero_entrada
                        decimal = int(binario_para_decimal(binario))
                        octal = decimal_para_octal(decimal)
                        hexadecimal = decimal_para_hexadecimal(decimal)

                        creditos()
                        print(f"Em binário: {binario}\nEm octal: {octal}\nEm decimal: {decimal}\nEm hexadecimal: {hexadecimal}")

                    #Entrada em base Octal.
                    elif base == 8:
                        creditos()
                        numero_entrada = input("Insira o número na base octal: \n")

                        numero_entrada = tira_0_esquerda(numero_entrada)
                        octal = numero_entrada
                        decimal = int(octal_para_decimal(octal))
                        binario = decimal_para_binario(decimal)
                        hexadecimal=decimal_para_hexadecimal(decimal)

                        creditos()
                        print(f"Em binário: {binario}\nEm octal: {octal}\nEm decimal: {decimal}\nEm hexadecimal: {hexadecimal}")
                    
                    #Entrada em base Hexadecimal.
                    elif base == 16:
                        creditos()
                        numero_entrada = input("Insira o número na base hexadecimal: \n").title()

                        numero_entrada = tira_0_esquerda(numero_entrada)
                        hexadecimal = numero_entrada
                        decimal = int(hexadecimal_para_decimal(hexadecimal))
                        binario = decimal_para_binario(decimal)
                        octal = decimal_para_octal(decimal)

                        creditos()
                        print(f"Em binário: {binario}\nEm octal: {octal}\nEm decimal: {decimal}\nEm hexadecimal: {hexadecimal}")
                    
                    #Tratando erro na entrada do tipo de base.
                    else:
                        creditos()
                        print("\n-------------------  ERROR ----------------------")
                        print("    Por favor, siga de acordo com o tutorial")
                        print( "---------------------------------------------------\n")

                #Tratando erro na entrada do número de entrada.
                except ValueError:
                    creditos()
                    print("\n-------------------  ERROR ----------------------")
                    print("    Por favor, siga de acordo com o tutorial")
                    print( "---------------------------------------------------\n")

            #Conversor para BCD, C1, C2 e Gray:
            elif acao == "b":
                try:
                    creditos()
                    base = int(input("Insira qual o número da base de entrada.\
                    \n---------------------------------------------------\
                    \n[2] [8] [10] [16]: "))

                    #Entrada em base Decimal.
                    if base == 10:
                        creditos()
                        numero_entrada = input("Insira o número na base decimal:\n")

                        decimal = int(numero_entrada)
                        binario = decimal_para_binario(decimal)
                        bcd = decimal_para_bcd(decimal)
                        gray = binario_para_gray(binario)
                        complementar_1 = binario_para_complementar_1(binario)
                        complementar_2 = complementar_1_para_complementar_2(complementar_1)

                        creditos()
                        print(f"O número de entrada na base [{base}] é {numero_entrada}.\
                            \n\tSeu BCD é: {bcd}\
                            \n\tSeu C1 é: {complementar_1}\
                            \n\tSeu C2 é: {complementar_2}\
                            \n\tSeu Gray é: {gray}")
                        
                    #Entrada em base Binária.
                    elif base == 2:
                        creditos()
                        numero_entrada = input("Insira o número na base binaria:\n")

                        numero_entrada = tira_0_esquerda(numero_entrada)
                        binario = numero_entrada
                        decimal = int(binario_para_decimal(binario))
                        bcd = decimal_para_bcd(decimal)
                        gray = binario_para_gray(binario)
                        complementar_1 = binario_para_complementar_1(binario)
                        complementar_2 = complementar_1_para_complementar_2(complementar_1)

                        creditos()
                        print(f"O número de entrada na base [{base}] é {numero_entrada}.\
                            \n\tSeu BCD é: {bcd}\
                            \n\tSeu C1 é: {complementar_1}\
                            \n\tSeu C2 é: {complementar_2}\
                            \n\tSeu Gray é: {gray}")

                    #Entrada em base Octal.
                    elif base == 8:
                        creditos()
                        numero_entrada = input("Insira o número na base octal: \n")

                        numero_entrada = tira_0_esquerda(numero_entrada)
                        octal = numero_entrada
                        decimal = int(octal_para_decimal(octal))
                        binario = decimal_para_binario(decimal)
                        bcd = decimal_para_bcd(decimal)
                        gray = binario_para_gray(binario)
                        complementar_1 = binario_para_complementar_1(binario)
                        complementar_2 = complementar_1_para_complementar_2(complementar_1)

                        creditos()
                        print(f"O número de entrada na base [{base}] é {numero_entrada}.\
                            \n\tSeu BCD é: {bcd}\
                            \n\tSeu C1 é: {complementar_1}\
                            \n\tSeu C2 é: {complementar_2}\
                            \n\tSeu Gray é: {gray}")
                    
                    #Entrada em base Hexadecimal.
                    elif base == 16:
                        creditos()
                        numero_entrada = input("Insira o número na base hexadecimal: \n").title()

                        numero_entrada = tira_0_esquerda(numero_entrada)
                        hexadecimal = numero_entrada
                        decimal = int(hexadecimal_para_decimal(hexadecimal))
                        binario = decimal_para_binario(decimal)
                        bcd = decimal_para_bcd(decimal)
                        gray = binario_para_gray(binario)
                        complementar_1 = binario_para_complementar_1(binario)
                        complementar_2 = complementar_1_para_complementar_2(complementar_1)

                        creditos()
                        print(f"O número de entrada na base [{base}] é {numero_entrada}.\
                            \n\tSeu BCD é: {bcd}\
                            \n\tSeu C1 é: {complementar_1}\
                            \n\tSeu C2 é: {complementar_2}\
                            \n\tSeu Gray é: {gray}")
                        
                    #Tratando erro na entrada do tipo de base.
                    else:
                        creditos()
                        print("\n-------------------  ERROR ----------------------")
                        print("    Por favor, siga de acordo com o tutorial")
                        print( "---------------------------------------------------\n")

                #Tratando problema no número da entrada.        
                except ValueError:
                    creditos()
                    print("\n-------------------  ERROR ----------------------")
                    print("    Por favor, siga de acordo com o tutorial")
                    print( "---------------------------------------------------\n")
                    
            #Tratando erro de entrada na variável "acao":
            else:
                creditos()
                print("\n-------------------  ERROR ----------------------")
                print("    Por favor, siga de acordo com o tutorial")
                print( "---------------------------------------------------\n")
            #Decisão do usuário alterando a variável "conversor" para: False caso queira parar de usar o conversor, ou True caso queira continuar utilizando-o.
            continuar = input("\n---------------------------------------------------\
                    \n\tDeseja continuar convertendo?\
                    \n\t         [S]im [N]ao: ").lower().strip().startswith("s")
            
            if continuar == False:
                conversor = False
                creditos()

    #Tratando erro de entrada na variável "ferramenta":        
    else:
        creditos()
        print("\n-------------------  ERROR ----------------------")
        print("    Por favor, siga de acordo com o tutorial")
        print( "---------------------------------------------------\n")

    #Decisão do usuário alterando a variável "continuar" para: False caso queira parar de usar o algoritmo, ou True caso queira continuar utilizando-o.
    continuar = input("\n---------------------------------------------------\
                    \n\tDeseja continuar utlizando o algoritmo?\
                    \n\t         [S]im [N]ao: ").lower().strip().startswith("s")
    creditos()
    if continuar == False:
        algoritmo = False
        creditos()
