#DATO DE ENTRADA PARA ALAMACENAR EL VALOR DEL NIVEL DE AGUA
print(f'LAS ETAPAS DE LA VIDA')
age=int(input("Digite su edad: "))

#CONDICIONES MULTIPLES CON PY
if age>=0 and age<=14:
    print(f'Niño')
if age>=15 and age<=28:
    print(f'Joven')
if age>=29 and age<=60:
    print(f'Adulto')
if age>=61:
    print(f'Anciano')
else:
    print(f'Digita un numero de 0 en adelante')