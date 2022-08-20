#DATO DE ENTRADA PARA ALAMACENAR EL VALOR DEL NIVEL DE AGUA
print(f'ESTACIONES DEL AÑO')
monthName=input("Digita el mes actual para conocer la estacion del año: ")

#CONDICIONES MULTIPLES CON PY
if monthName=='Enero' or monthName=='Febrero' or monthName=='Marzo':
    print(f'Se encuentra en INVIERNO')
elif monthName=='Abril' or monthName=='Mayo' or monthName=='Junio':
    print(f'Se encuentra en PRIMAVERA')
elif monthName=='Julio' or monthName=='Agosto' or monthName=='Septiembre':
    print(f'Se encuentra en VERANO')
elif monthName=='Octubre' or monthName=='Noviembre' or monthName=='Diciembre':
    print(f'Se encuentra en OTOÑO')
else:
    print(f'Escribe un mes entre Enero y Diciembre')