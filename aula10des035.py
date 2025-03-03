a = int(input('Valor da reta A: '))
b = int(input('Valor da reta B: '))
c = int(input('Valor da reta C: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Podem formar um triângulo!')
else:
    print('Não podem formar um triângulo!')