#5)	Escreva uma função que:
#a)	Receba uma frase como parâmetro.
#b)	Retorne uma nova frase com cada palavra com as letras invertidas.

def palavra_str(s):
    if s == '':
        return s
    return s[-1] + palavra_str(s[:-1])

print(palavra_str('A B C D E F G'))