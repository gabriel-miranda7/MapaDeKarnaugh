numvar = int()
def menu(numvar):
    from os import system, name
    system('cls' if name == 'nt' else 'clear')
    while numvar > 4 or numvar < 2:
        numvar = int(input('Digite o número de variáveis para o seu mapa. 2, 3 ou 4: ')) #Define o número de variáveis
        if numvar > 4 or numvar < 2: #Verifica se o número de variáveis não passou do limite
            print('Digite novamente.')
        if numvar == 2:
            choice = int(input('Você quer digitar a TABELA-VERDADE[1] ou a EXPRESSÃO BOOLEANA[2] ?: '))
            system('cls' if name == 'nt' else 'clear')
            if choice == 2: #Recebe que o usuário quer digitar a expressão
                A = True
                B = True
                print('Agora você irá digitar a expressão lógica.\nPara isso, utilize:\n. = and\n+ = or\n´ (Antes do Valor) = not\nAlém disso, utilize A e B para as variáveis.')
                expr = str(input('Digite a expressão lógica: ')).strip()
                exprL = list()
                for i in range(len(expr)):
                    if expr[i] != ' ' and expr[i] != '.' and expr[i] != '´' and expr[i] != '+':
                        exprL.append(expr[i].upper())
                    if expr[i] == '.':
                        exprL.append(' and ')
                    if expr[i] == '´':
                        exprL.append(' not ')
                    if expr[i] == '+':
                        exprL.append(' or ')
                expr_final = ''.join(exprL)
                print(expr_final)
                resultado = tabela_verdade(expr_final)

def tabela_verdade(expr):
    from os import system, name
    system('cls' if name == 'nt' else 'clear')
    A = True
    B = True
    s1 = eval(expr)
    A = False
    s2 = eval(expr)
    A = True
    B = False
    s3 = eval(expr)
    A = False
    s4 = eval(expr)
    print('--------------')
    print('A | B   |  S')
    print(f'1 | 1   |  {s1}')
    print(f'0 | 1   |  {s2}')
    print(f'1 | 0   |  {s3}')
    print(f'0 | 0   |  {s4}')
    karnaugh2(s1, s2, s3, s4)
def karnaugh2(s1, s2, s3, s4):
    print('MAPA DE KARNAUGH')
    print('A/B  |  0    |     1')
    print('------------------------')
    for i in range(7):
        if i != 2 and i != 4:
            print('  |')
        if i == 2:
            print(f' 0|   {s4}     {s2}')
        if i == 4:
            print(f' 1|   {s3}     {s1}')
    simplified = list()
    if s1 == s2 and s1 != False:
        simplified.append(' B')
        simplified.append(' or ')
    if s1 == s3 and s1 != False:
        simplified.append(' A') 
        simplified.append(' or ')
    if s3 == s4 and s3 != False:
        simplified.append(' not B ')
        simplified.append(' or ')
    if s4 == s2 and s2 != False:
        simplified.append(' not A ')
        simplified.append(' or ')
    if s1 == True and s2 == False and s3 == False and s4 == False:
        simplified.append('A and B')
    if s2 == True and s1 == False and s3 == False and s4 == False:
        simplified.append('not A and B')
    if s3 == True and s1 == False and s2 == False and s4 == False:
        simplified.append('A and not B')
    if s4 == True and s2 == False and s3 == False and s1 == False:
        simplified.append('not A and not B')
    if simplified[len(simplified)-1] == ' or ':
        simplified.pop()
    simplifiedx = ''.join(simplified)
    print('')
    print('A expressão mais simplificada é: ', simplifiedx)
menu(numvar)
