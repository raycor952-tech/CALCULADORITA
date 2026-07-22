# CALCULADORA - VERSIÓN 2
# Autor(a): RAYNER CORY
# =============================================

print("CALCULADORA")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\n1. Sumar")
print("2. Restar")

opcion = input("\nSeleccione una opción: ")

if opcion == "1":
    print("\n La suma es:", num1 + num2)

elif opcion == "2":
    print("\n La resta es:", num1 - num2)

else:
    print("\n Opción no válida.")
