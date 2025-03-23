nombre= "Alicia"
edad= 32
profesion= "Bióloga"

nombre1= "Princesa"
edad1= 31
profesion1= "Microbióloga"

lista1 = []
lista2= []

lista1.append(nombre)
lista1.append(edad)
lista1.append(profesion)

lista2.append(nombre1)
lista2.append(edad1)
lista2.append(profesion1)
print("Elementos de lista 1 son:{}".format(lista1))
print("Elementos de lista 2 son:{}".format(lista2))
print("--------------------------------------------------")

suma= lista1[1]+lista2[1]
print("La suma de las listas es :{}".format(suma))
print("--------------------------------------------------")

suma2= lista1+lista2
print("La suma de las listas es :{}".format(suma2))
print("--------------------------------------------------")

lista2.reverse()
lista1.reverse()
suma_inversa= lista2 + lista1
print("La lista 1 al reves es: {}".format(lista1))
print("La lista 2 al reves es: {}".format(lista2))
print("La suma de la lista inversa es :{}".format(suma_inversa))
print("--------------------------------------------------")

suma_inversa.remove(32)
suma_inversa.remove(31)
print("La lista al reves es: {}".format(suma_inversa))
print("--------------------------------------------------")

lista2.clear()
print("lista 2 actualizada:{}".format(lista2))