"""
Crear 3 variables: nombre, edad y distrito

Requisitos:
- Nombre: string, edad: int, distrito: string
- Concatenar estos 2 datos e indicar una oración como la siguiente:
José tiene x años y es de "Distrito"
- Obtener el módulo de su edad al usarlo con el número 5
"""

var_1 = "Jorge"
var_2 = 19
var_3 = "Ate"
modulo = var_2 % 5

print("Mi nombre es {} tengo {} años y vivo en {}".format(var_1, var_2, var_3))
print("El módulo es: {}".format(modulo))