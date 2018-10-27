cpf=input('CPF sem os dois últimos dígitos: ')
n1=0
n2=0
for x in range(0,9):
    n1+= int(cpf[x:(x+1)])*(11-(x+1))

n1 = n1%11

if n1 < 2:
    n1 = 0
else:
    n1 = 11-n1

cpf = cpf+str(n1)

for x in range(0,10):
    n2+= int(cpf[x:(x+1)])*(12-(x+1))

n2 = n2%11

if n2 < 2:
    n2 = 0
else:
    n2 = 11-n2

print('Seus dois últimos dígitos são: {}{}'.format(n1,n2))

print('CPF: {}'.format(cpf+str(n2)))
