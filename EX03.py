print('')
print('EXERCICIOS-03')
print('Faça um programa que leia 3 números inteiros e mostre o menor deles')
print('')
a = int(input('[1] PRIMEIRO NÚMERO:   '))
b = int(input('[2] SEGUNDO  NÚMERO:   '))
c = int(input('[3] PRIMEIRO NÚMERO:   '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('')
print('O MENOR NÚMERO É {}'.format(menor))