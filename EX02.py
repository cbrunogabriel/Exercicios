print('Exercicios-02')
print('')

def Triangular(i,x):
	if(x > 0):
		while(i <= x):
			i2 = i+1
			i3 = i+2
			valor = i *i2 *i3
			i = i + 1
			if(valor == x):
				return ('Numero '+str(x)+' é triangular. Resultado de: '+ str(i-1)+'*'+str(i2)+'*'+str(i3))
			if(resultado > x):
				break
		return 'Numero '+str(x)+' não é triangular'
	else:
		return 'Numero Negativo Invalido'

print(Triangular(1,8))
print(Triangular(1, 25))
print(Triangular(1, 58))
print(Triangular(1, 120))
print(Triangular(1, 334))
print(Triangular(1, 122))
print(Triangular(1, -11))