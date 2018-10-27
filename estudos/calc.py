import sys
import re

def soma(n1, n2):
    return print(n1+n2)

def sub(n1, n2):
    return print(n1-n2)

def mul(n1, n2):
    return print(n1*n2)

def div(n1, n2):
    return print(n1/n2)

def checkOp():
    if p[0][1] == '+':
        soma(n1, n2)
    elif p[0][1] == '-':
        sub(n1, n2)
    elif p[0][1] == 'x':
        mul(n1, n2)
    elif p[0][1] == '/':
        div(n1, n2)

regex = r'(-?\d+)([-+x*/])(-?\d+)'
operadores = '+','-','x','*','/'
p = (''.join(sys.argv[1:]))

if __name__ == '__main__':
    try:
        p = re.findall(regex, p)
        n1 = int(p[0][0])
        n2 = int(p[0][2])
        checkOp()
    except:
        print('Possui algum caracter inválido')