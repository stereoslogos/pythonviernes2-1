#DATO DE ENTRADA PARA ALAMACENAR EL VALOR DEL NIVEL DE AGUA
nivelAgua=int(input("Digita el nivel de agua: "))

#CONDICIONES MULTIPLES CON PY
if nivelAgua>=0 and nivelAgua<20:
    print(f'Peligro el nivel de agua es de {nivelAgua} metros y es muy bajo')
elif nivelAgua>=20 and nivelAgua<400:
    print(f'El nivel de agua {nivelAgua} es optimo')
elif nivelAgua>=400:
    print(f'Peligro el nivel de agua es de {nivelAgua} metros y es demasiado alto')
else:
    print(f'Digita un numero de 0 en adelante')