def calcular_media(n1,n2,n3,n4):
    m=n1+n2+n3+n4/4
    if m >= 7.0:
        resultado = (f"Parabéns!!!!!, você foi APROVADO com media {m: .2f}")
    else:
        resultado = (f"Que pena, você foi reprovado com media {m: .2f}")
    return resultado

try:
    
    n1=float(input('Digite a primeria nota:'))
    n2=float(input('Digite a segunda nota:'))
    n3=float(input('Digite a terceira nota:'))
    n4=float(input('Digite a quarta nota:'))
    
    resultado_final = calcular_media(n1,n2,n3,n4)
    print(resultado_final)

except ValueError:
    print('ERRO, Digite numero validos.')
