def multi_table(multiplicando):
    tabla_de_multiplicar = ""
    for multiplicador in range(1, 11):
        tabla_de_multiplicar += str(multiplicador) + " * " +  str(multiplicando) + " = " + str(multiplicador * multiplicando)  
        if multiplicador < 10:
            tabla_de_multiplicar += "\n"                   
    return tabla_de_multiplicar

1 hour agoRefactorDiscuss
