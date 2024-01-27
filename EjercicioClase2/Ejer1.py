
lista_1 = []
lista_2 = []

lista_1.append("Jorge")
lista_1.append(19)
lista_1.append("Ingeniero")

lista_2.append("Luis")
lista_2.append(22)
lista_2.append("Médico")

suma_listas = lista_1 + lista_2

print("La lista es: {}".format(suma_listas))

suma_listas.reverse()

print("La lista actualizada es: {}".format(suma_listas))

suma_listas.remove(19)
suma_listas.remove(22)

print("La lista actualizada es: {}".format(suma_listas))