numvar = int()
def menu(numvar): #Menu inicial do programa de Karnaugh.
    from os import system, name
    caracteres_especiais = ['.', ' ', '-', '+']
    system('cls' if name == 'nt' else 'clear') #Função que limpa a tela.
    while numvar > 3 or numvar < 2:
        numvar = int(input('Digite o número de variáveis para o seu mapa. 2 ou 3: ')) #Define o número de variáveis
        if numvar > 3 or numvar < 2: #Verifica se o número de variáveis não passou do limite
            print('Digite novamente.')
        if numvar == 2:
            system('cls' if name == 'nt' else 'clear')
            A = True #define duas variáveis a e b como true para posterior avaliação
            B = True
            print('Agora você irá digitar a expressão lógica.\nPara isso, utilize:\n. = and\n( = Abre Parêntese\n) = Fecha Parêntese\n+ = or\n- (Antes do Valor) = not\nAlém disso, utilize A e B para as variáveis.')
            expr = str(input('Digite a expressão lógica: ')).strip() #Recebe a expressão logica em uma string e a coloca em uma lista.
            expr_final = transformar_booleana(expr, caracteres_especiais)
            print(expr_final)
            resultado = tabela_verdade2(expr_final)
        elif numvar == 3:
            system('cls' if name == 'nt' else 'clear')
            A = True
            B = True
            C = True
            print('Agora você irá digitar a expressão lógica.\nPara isso, utilize:\n. = and\n( = Abre Parêntese\n) = Fecha Parêntese\n+ = or\n´ (Antes do Valor) = not\nAlém disso, utilize A e B para as variáveis.')
            expr = str(input('Digite a expressão lógica: ')).strip()
            expr_final = transformar_booleana(expr,caracteres_especiais)
            print(expr_final)
            resultado = tabela_verdade3(expr, expr_final, caracteres_especiais)

def transformar_booleana(expr, caracteres_especiais): #Função que transforma a versão da expressão digitada pelo usuário em uma melhor formatada.
    exprL = list()
    for i in range(len(expr)):
        if expr[i] not in caracteres_especiais:
            exprL.append(expr[i].upper())
        if expr[i] == '.':
            exprL.append(' and ')
        if expr[i] == '-':
            exprL.append(' not ')
        if expr[i] == '+':
            exprL.append(' or ')
        expr_final = ''.join(exprL)
    return(expr_final)

def transformar_booleana3var(expr, caracteres_especiais): #Função que transforma a versão da expressão digitada pelo usuário em uma melhor formatada.
    exprL = list()
    for i in range(len(expr)):
        if expr[i] not in caracteres_especiais and expr[i-1] != '-':
            exprL.append(expr[i].upper())
        if expr[i] == '.':
            exprL.append(' & ')
        if expr[i] == '-':
            exprL.append(' Not(')
            exprL.append(f"{expr[i+1].upper()})")
        if expr[i] == '+':
            exprL.append(' | ')
        expr_final = ''.join(exprL)
    return(expr_final)

def tabela_verdade2(expr):
    from os import system, name
    system('cls' if name == 'nt' else 'clear')
    A = True  #Altera os valores de A e B para todas as possibilidades, e checa o valor da expressão em cada caso.
    B = True
    s1 = eval(expr) 
    A = False
    s2 = eval(expr)
    A = True
    B = False
    s3 = eval(expr)
    A = False
    s4 = eval(expr)
    print('TABELA VERDADE: ')
    print('--------------')
    print('A | B   |  S')
    print(f'1 | 1   |  {s1}')
    print(f'0 | 1   |  {s2}')
    print(f'1 | 0   |  {s3}')
    print(f'0 | 0   |  {s4}')
    karnaugh2(s1, s2, s3, s4)

def karnaugh2(s1, s2, s3, s4): #Karnaugh para duas variáveis
    print('MAPA DE KARNAUGH')  #Imprime o mapa de karnaugh formatado e simplifica a expressão por meio das posições dos valores no mapa, de acordo com o padrão
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
    #Código que simplifica a expressão por karnaugh.
    if s1 == s3 and s1 != False:
        simplified.append(' A')  
        simplified.append(' or ')
    if s1 == s2 and s1 != False:
        simplified.append(' B')
        simplified.append(' or ')
    if s4 == s2 and s2 != False:
        simplified.append(' not A ')
        simplified.append(' or ')
    if s3 == s4 and s3 != False:
        simplified.append(' not B ')
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
    simplifiedx = ''.join(simplified) #Transforma em string a lista simplificada
    print('')
    print('A expressão mais simplificada é: ', simplifiedx)

def tabela_verdade3(betaexpr, expr, caracteres_especiais):
    from sympy.logic.boolalg import simplify_logic
    from sympy.abc import A, B, C
    from os import system, name
    system('cls' if name == 'nt' else 'clear')   
    A = True                            #Avalia todas as possibilidades para a tabela verdade em 3 variáveis.
    B = True
    C = True 
    s1 = eval(expr)
    C = False
    s2 = eval(expr)
    B = False
    C = True
    s3 = eval(expr)
    C = False
    s4 = eval(expr)
    A = False
    B = True
    C = True
    s5 = eval(expr)
    C = False
    s6 = eval(expr)
    B = False
    C = True
    s7 = eval(expr)
    C = False
    s8 = eval(expr)
    print('TABELA VERDADE: ')
    print('--------------')
    print('A  |  B  | C  |  S')
    print(f'1 |  1  |  1  | {s1}')    #Imprime a tabela formatada
    print(f'1 |  1  |  0  | {s2}')
    print(f'1 |  0  |  1  | {s3}')
    print(f'1 |  0  |  0  | {s4}')
    print(f'0 |  1  |  1  | {s5}')
    print(f'0 |  1  |  0  | {s6}')
    print(f'0 |  0  |  1  | {s7}')
    print(f'0 |  0  |  0  | {s8}')
    final = transformar_booleana3var(betaexpr, caracteres_especiais)
    karnaugh3(s1, s2, s3, s4, s5, s6, s7, s8, final)

def karnaugh3(s1, s2, s3, s4, s5, s6, s7, s8, expr):
    print('MAPA DE KARNAUGH')
    print('A/B.C  |  00    |     01    |  11    |     10')
    print('-----------------------------------------------')
    for i in range(7):                                                      #Avalia a expressão e á reduz baseada em seu mapa de karnaugh
        if i != 2 and i != 4: 
            print('  |')
        if i == 2:
            print(f' 0|     {s8}      {s7}      {s5}        {s6}')
        if i == 4:
            print(f' 1|     {s4}      {s3}      {s1}        {s2}')
    from sympy.logic.boolalg import simplify_logic
    from sympy.abc import A, B, C
    simplified_expression = simplify_logic(expr)
    print('A expressão mais simplificada é: ', end='')
    print(simplified_expression)
    print("| = Or\n& = And")
menu(numvar)