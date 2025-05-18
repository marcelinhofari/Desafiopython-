def salariomes():
    try:
        a=int(input('Quanto voce ganha por hora:'))
        b=int(input('Quando horas você trabalha por mês:'))
        s=a*b
        print('Você recebe por mês',s)
    except ValueError:
        print('Erro. Valor inválido.')
salariomes()
#thanks
