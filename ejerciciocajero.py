#Crear un programa que simule un cajero con un saldo inicial de $2500, con el siguiente menú
#1. Ingreso de dinero
#2. Retirar dinero
#3. Mostrar saldo
#4. Salir
saldo= 2500
print('1. Ingreso de dinero')
print('2. Retirar dinero')
print('3. Mostrar saldo')
print('4. Salir')

seleccion = int(input('Ingrese una opción '))
if seleccion == 1:
    ing = float(input('Ingrese la cantidad '))
    saldo += ing
    print(f'\nUsted ingresó: {ing} \nSu nuevo saldo es {saldo}')
    #seleccion = int(input('¿Qué desea hacer?\n 1. Regresar al menú \n 2. Salir \n'))
elif seleccion == 2:
    ret = float(input('Ingrese la cantidad '))
    if ret > saldo: 
        print('!Error¡ Fondos insuficientes')
    else:
        saldo -= ret
        print(f'\n Usted retiró: {ret} \nSu nuevo saldo es {saldo}')
elif seleccion == 3:
    print(f'Su saldo disponible es: {saldo}')
elif seleccion == 4:
    print('Sesión terminada')
else: 
    print('Error de ingreso de datos')