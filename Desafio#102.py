fat = True
def fatorial(num, show=False):
    """
      fatoria(num, show)
    calcula o fatorial do nume desejado
    para num: o numero a ser fatorada
    para show: se deve ou nao mostrar a conta 
    """

    list = []
    d = 1
    for c in range(1, num):
        d = c * d 
        list.append(c)
    d = d * num
    if show == False:
        print(d)
    else:
        for i in list:
            print(f'{i} x ', end='')
        print(f'{num} = {d}')

while fat != 'S':

    nume = int(input('escolha um numero para ser fatorado'))
    fat = input('gostaria de mostrar a conta? Y ou N ou S para sair')
    fat = fat.upper()
    if fat == 'Y':
        fat = True
        fatorial(nume, fat)
    elif fat == 'N':
        fat = False
        fatorial(nume, fat)
    elif fat == 'S':
        print('obrigado, tchau')
    else: 
        print('digite comando valido')

        
#Feito




