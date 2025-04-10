import math
n2 = float(input('Digite um número:  '))
print('O número {} tem a parte inteira {}'.format(n2, int(n2)))

# outra forma
num = float(input('Digite um número:  '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))