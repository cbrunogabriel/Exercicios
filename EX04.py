print('')
print('EXERCICIOS-04')

print('Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.\033[m')
print('')

num = int(input('INFORME O NUMERO: '))
cont = 0
for primos in range(1, num + 1):
    if num % primos == 0:
        cont += 1

if cont > 2:
    print('O número é primo \033[1;31mFALSO\033[m')
else:
    print('o número é primo \033[1;32mVERDADEIRO\033[m')