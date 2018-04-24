# ACPyhton5

'''Esta atividade deve ser realizada até 21/04/2018 às 23hs
1 - Considere o problema de conversão de temperatura. Escreva um programa modularizado que permite ao usuário converter uma faixa de temperatura de Fahrenheit para Celsius (O usuário deve digitar F) e de Celsius para Fahrenheit (O usuário deve digitar C). Para a construção do
programa você deve escrever as seguintes funções:

       (a). exibeMsg() - apenas exibe uma msg para o usuário dizendo o que o programa faz e informando como deve ser a entrada de dados. Não tem parâmetro de entrada e não retorno.

       (b). getConvertTo() - a função não tem parâmetro de entrada e retorna “F” ou “C”

        (c). exibeFahrenheitTOCelsius(start, end) – essa função recebe como entrada o intervalo de temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida para Celsius

         (d). exibeCelsiusTOFahrenheit(start, end) – essa função recebe como entrada o intervalo de temperatura a ser exibido, faz a conversão de temperatura e mostra a temperatura convertida para Fahrenheit
'''

init=1
Msg = 'Este programa converte temperatura de  ºCelsius para Fahrenheit ou vice-e-versa '
def exibeMsg():
    return Msg

def getConvertTO():
    Med = input(' F - Fahrenheit para Celsius \n C - Celsius para Fahrenheit \n>>>>').strip().upper()[0]
    while Med not in 'FfCc':
        Med = input('DADOS INVÁLIDOS!!!  TENTE NOVAMENTE:\n F - Fahrenheit para Celsius \n C - CelsiusTOFahrenheit \n>>>>').strip().upper()[0]
    if Med == 'F':
        return exibeFahrenheitTOCelsius()
    else:
        return exibeCelsiusTOFahrenheit()
        
        

def exibeFahrenheitTOCelsius(start = None, end = None):
    start = float(input('Digite a tempreratura em Fahrenheit:  '))
    end = ((start-32)/1.8)
    print ('a temperatura convertida para Celsius é igual a: ')
    return end

def exibeCelsiusTOFahrenheit(start = None, end = None):
    start = float(input('Digite a tempreratura em Celsius:  '))
    end = start*1.8+32
    print ('a temperatura convertida para Fahrenheit é igual a: ')
    return end

if init > 0:
    print (exibeMsg())
    print (getConvertTO())

#------------------------------------------------------------------------------------------------------------------------------------------------------------

'''2 - Faça um programa modularizado que calcule e apresente o fatorial de um número inteiro e natural fornecido pelo usuário.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1=120.
Por definição 0! = 1.
O seu programa deve contar uma função que lê um número inteiro e positivo, bem como uma função, chamada fatorial, que recebe um inteiro e positivo n e retorna um inteiro e positivo, representando a soma dos dígitos do número dado.'''

def validarPositivo ():
    print ('>>>>FATORIAL<<<<')
    x = int(input('Digite um número inteiro positivo: '))
    while x < 0:
        x = int(input('DADOS INCORRETOS!!! TENTE NOVAMENTE: \nDigite um número inteiro positivo: '))
    return x
    

        
def fatorial(y = validarPositivo (), result =1):
    w = y
    while y >= 1:
        result *= y
        y -= 1
    print('O fatorial de ',w,' é: ',  result)

if init > 0:
    print ( fatorial())

#---------------------------------------------------------------------------
    
    


