"reconocimiento de tipos de datos: type() "

"""creacion de variables"""

nombre="luis"
ciudad="lima"
saldo= 5000
empresa=False
correo= "Luish@gmail.com"
empleado=[nombre,saldo,empresa,ciudad]
empleado_d={'nomb':nombre, 'ciud': ciudad, 'sald':saldo, 'empre': empresa, 'corr':correo}

print("tipo de  dato de mi variable 'nombre' es: {}".format(type(nombre)))
print("tipo de  dato de mi variable 'ciudad' es: {}".format(type(ciudad)))
print("tipo de  dato de mi variable 'saldo' es: {}".format(type(saldo)))
print("tipo de  dato de mi variable 'empresa' es: {}".format(type(empresa)))
print("tipo de  dato de mi variable 'correo' es: {}".format(type(correo)))
print("tipo de  dato de mi variable 'empleado' es: {}".format(type(empleado)))
print("tipo de  dato de mi variable 'empleado:d' es: {}".format(type(empleado_d)))