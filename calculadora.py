#Importando bilbliotecas:
from os import name, system
import math

#Declarando Variáveis:
algoritmo = True
conversor = False
calculadora = False
operadores_1num= ['!','sen', 'cos', 'tg', 'cossec', 'sec', 'cotg']
operadores_2num = ['+', '-','/','*','%','^','raiz', 'hiper']
tipos_de_base = [2,8,10,16]
binario = ""
octal = ""
hexadecimal = ""
decimal = 0
numero_1=0
numero_2=0
operador=''

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
        num_2= math.radians(num_1)

        if operador =='sen':#Operação Seno.
            print(f'sen({num_1}) = {math.sen(num_2)}')
            
        elif operador =='cos':#Operação Cosseno.
            print(f'cos({num_1}) = {math.cos(num_2)}')
            
        elif operador =='tg':#Operação Tangente.
            print(f'tg({num_1}) = {math.tg(num_2)}')
            
        elif operador =='sec':#Operação Secante.
            print(f'sec({num_1}) = {1/math.cos(num_2)}')
                
        elif operador =='cossec':#Operação Cossecante.
            print(f'cossec({num_1}) = {1/math.sen(num_2)}')
            
        elif operador =='cotg':#Operação Cotangente.
            print(f'cotg({num_1}) = {1/math.tg(num_2)}')
        

def operacao_2num(numero_1):#Responsável por realizar as operações com 2 números.
    numero_2= input("Digite outro número: ").strip()
    
    if numero_2.isnumeric():
        num_1=float(numero_1)
        num_2=float(numero_2)

        if operador == '+':#Operação Soma.
            print(f'{num_1} + {num_2} = {num_1+num_2}')

        elif operador == '-':#Operação Subtração.
            print(f'{num_1} - {num_2} = {num_1-num_2}')

        elif operador == '*':#Operação Multiplicação.
            print(f'{num_1} * {num_2} = {num_1*num_2}')

        elif operador == '/':#Operação Divisão.
            print(f'{num_1} / {num_2} = {num_1/num_2}')

        elif operador == '^':#Operação Potênciação.
            print(f'{num_1} ^ {num_2} = {num_1**num_2}')

        elif operador == '%':#Operação Modular.
            print(f'{num_1} % {num_2} = {num_1%num_2}')

        elif operador == 'raiz':#Operação Radiciação.
            print(f'A {num_2}ª raiz de {num_1} = {num_1**(1/num_2)}')
        
        elif operador == 'hiper':#Operação Tetração.
            num_2= int(num_2)
            indice = num_1
            for i in range(0,num_2):
                num_1= num_1**indice
                print(f'{numero_1} hiper {num_2} = {num_1}')
        
        else:#Tratando possível erro no operador.
            print("Tente novamente, o operador foi considerado invalido.")
    else:#Tratando possível erro na entrada da variável "numero_2"
        print("Tente novamente, o número foi considerado invalido.")
    

            
def decimal_para_binario(decimal):#Responsável por converter Decimal -> Binário.
    binario = ""

    while decimal > 0:
        if decimal % 2 == 1:
            binario = "1" + binario
            
        else:
            binario = "0" + binario
            
        decimal //= 2
        
    return binario


def decimal_para_octal(decimal):#Responsável por converter Decimal -> Octal.
    octal = ""

    while decimal > 0:
        if decimal % 8 != 0:
            octal = str(decimal % 8) + octal
        else:
            octal = "0" + octal
        decimal //= 8
    return octal


def decimal_para_hexadecimal(decimal):#Responsável por converter Decimal -> Hexadecimal.
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


def binario_para_decimal(binario):#Responsável por converter Binário -> Decimal.
    decimal = 0
    binario = binario[::-1]

    for i in range(len(binario)):
        decimal += int(binario[i]) *  (2** i)

    return decimal


def octal_para_decimal(octal):#Responsável por converter Octal -> Decimal.
    decimal = 0
    octal = octal[::-1]

    for i in range(len(octal)):
        decimal += int(octal[i])* (8 ** i)

    return decimal


def hexadecimal_para_decimal(hexadecimal):#Responsável por converter Hexadecimal -> Decimal.
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


#Tutorial:
tutorial = True
texto_tutorial ='\
Esse algoritmo foi desenvolvida utilizando a linguagem de programação Python3, portanto, para usufruir da melhor maneira possível, deve-se seguir algumas regras.\
        \nNos locais em que existem decisões de sim ou nao, caso coloque algo invalido, adotaremos como um "NÃO". \
        \n0:Como escolher o que utilizar:\
        \n0.1:Para escolher utilizar a Calculadora, quando pedido, digite "A". \
        \n0.2:Para escolher utilizar a Conversor, quando pedido, digite "B". \
        \n\n1: Como utilizar a Calculadora: \
        \n1.1: Serão pedidos números para a realização das operações. Nesses espaços digite APENAS números, salvo 2 exceções:\
        \n Angulos: adote sempre os angulos em graus.\
        \n Negativos: use o " - " antes de digitar os números (exemplo: -14);\
        \n Decimais: utilize o " . " para separar a parte inteira de um número de sua parte racional(exemplo: 3.14)  \
        \n1.2: Será pedido o operador matemático de interesse, para usar de maneira devida digite APENAS UM operador por vez, utilizando operadores entre: [!,sen, cos, tg, cossec, sec, cotg] e [+, -, /, *, %, ^, raiz, hiper]. \
        \n1.3: Após a operação, será apresentado o resultado e a pergunta se quer sair ou não da calculadora. Para continuar digite "s", caso contrário digite "n".\
        \n1.5: Ocorra algum erro, será perguntado se deseja sair da calculadora e caso permaneça, recomeça tudo novamente.\
        \n\n2: Como utilizar o Conversor: \
        \n2.1: Quando pedido, digite, utilizando APENAS números, qual o tipo de base estará o número a ser convertido. \
        \n2.2: Quando pedido, digite, utilizando APENAS os bits que a base aceita (exemplo: Binario - utilize apenas 0s e 1s),  o número que será convertido para as outras bases.\
        \n2.3. Serão exibidos os números pós-conversão.\
        \n2.4. Quando pedido, digite, utilizando apenas UMA letra ("n" ou "s"), se deseja continuar convertendo ou não, se quiser continuar digite "s", caso contrário digite "n".\n' 

tutorial= input("Deseja ver o tutorial de como utilizar o algoritmo?\n [S]im [N]ao: ").strip().lower().startswith('s')

if tutorial is True:
    print(texto_tutorial)

#Algortimo:
while algoritmo is True:
    conversor = input("O que deseja utilizar? \n [A]Calculadora [B]Conversor de bases\n").strip().lower().startswith('b')

    if conversor is False: #Calculadora:
        calculadora = True
        
        while calculadora is True:
            #Reiniciando as variavéis:
            numero_1=0
            numero_2=0
            operador=''

            numero_1= input("Digite um numero: ").strip()

            if numero_1.isnumeric():
                operador= input("Digite um operador: ").strip().lower()
                limpar()

                if operador in operadores_1num:#Operaçoes que dependem APENAS de um numero.
                    operacao_1num(numero_1)

                elif operador in operadores_2num:#Operaçoes que dependem de 2 numeros.
                    limpar()
                    operacao_2num(numero_1)

            else:#Tratando possível erro na entrada da variável "numero_1".
                print("Tente novamente, o numero foi considerado invalido.")
                
            #Decisão ao usuário alterando o conversor para: False caso queira parar de usar a calculadora, ou True caso queira continuar utilizando-a.
            calculadora = input("Deseja continuar utilizando a Calculadora? \n[s]im [n]ao: ").lower().strip().startswith("s")
            limpar()
    
    else:#Conversor de bases:
        calculadora = False

        while conversor is True:
            #Reiniciando as variáveis:   
            binario = ""
            octal = ""
            decimal = ""
            hexadecimal = ""
            
            #Recebendo qual a base do número a ser convertido:
            base = int(input("Insira qual o número da base [2] [8] [10] [16]:\n "))

            if base == 10:#Entrada em base Decimal.
                numero_entrada = input("Insira o número na base decimal: \n")

                decimal = int(numero_entrada)
                binario = decimal_para_binario(decimal)
                octal = decimal_para_octal(decimal)
                hexadecimal = decimal_para_hexadecimal(decimal)

                limpar()
                print(f" Em binario: {binario}\n Em octal: {octal}\n Em decimal: {decimal}\n Em hexadecimal: {hexadecimal} ")

            elif base == 2:#Entrada em base Binária.
                numero_entrada = input("Insira o número na base binaria: \n")

                binario = numero_entrada
                decimal = int(binario_para_decimal(binario))
                octal = decimal_para_octal(decimal)
                hexadecimal = decimal_para_hexadecimal(decimal)

                limpar()
                print(f" Em binario: {binario}\n Em octal: {octal}\n Em decimal: {decimal}\n Em hexadecimal: {hexadecimal} ")

            elif base == 8:#Entrada em base Octal.
                numero_entrada = input("Insira o número na base octal: \n")

                octal = numero_entrada
                decimal = int(octal_para_decimal(octal))
                binario = decimal_para_binario(decimal)
                hexadecimal=decimal_para_hexadecimal(decimal)

                limpar()
                print(f" Em binario: {binario}\n Em octal: {octal}\n Em decimal: {decimal}\n Em hexadecimal: {hexadecimal} ")

            elif base == 16:#Entrada em base Hexadecimal.
                numero_entrada = input("Insira o número na base hexadecimal: \n")

                hexadecimal = numero_entrada
                decimal = int(hexadecimal_para_decimal(hexadecimal))
                binario = decimal_para_binario(decimal)
                octal = decimal_para_octal(decimal)

                limpar()
                print(f" Em binario: {binario}\n Em octal: {octal}\n Em decimal: {decimal}\n Em hexadecimal: {hexadecimal} ")

            else:#Tratando erro na entrada do tipo de base.
                print("Ocorreu um erro ao inserir o número da base de inicio, utilize apenas números, digitando exatamente o que estiver entre os colchetes.")

        #Decisão ao usuário alterando o conversor para: False caso queira parar de usar o conversor, ou True caso queira continuar utilizando-o.
        conversor = input("Deseja continuar convertendo? \n[s]im [n]ao: ").lower().strip().startswith("s")
        limpar()

    #Decisão ao usuário alterando o algoritmo para: False caso queira parar de usar o algoritmo, ou True caso queira continuar utilizando-o.
    sair = input("Deseja sair?\n [S]im [N]ao: ").strip().lower().startswith('s')
    
    if sair is True:
        algoritmo = False
