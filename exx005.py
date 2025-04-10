def Calcular_Metro():
    try:
        print('Olá,Seja bem-vindo!')
        m=float(input('Digite quantos metros:'))
        c=(m*100)
        print(m,'metros em centimetros é:',c,'centimetros!')
    except ValueError:
        print('Erro. não foi possivel te enteder.') 
Calcular_Metro()
