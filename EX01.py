print('EXERCICIOS-01')
print('')
print('Informações de iniciais')
data = int(input("Dia do nascimento: "))
mes = int(input("Mês do nascimento: "))
ano = int(input("Ano do nascimento: "))

print('')
print('Informações atuais')

data2 = int(input("o dia atual: "))
mes2 = int(input("O mês atual: "))
ano2 = int(input("O ano atual: "))

idade_anos = ano2 - ano

if mes >= mes2:
    if mes == mes2:
        if data > data2:
            idade_anos - 1
    else:
        idade_anos - 1

dias_passados =  (30 - data) + ((12 - mes)*30) + ((mes2 - 1)*30) + data2 + (idade_anos)*365

print('')
print('Dias de vidas é', dias_passados, "dias.")