# CALCULADORA - VERSIÓN 3
# Autor(a): RAYNER CORY
# =============================================

print("CALCULADORA")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\ n1. Sumar")
print(" 2. Restar")
print(" 3. Multiplicar")

opcion = input("\n Seleccione una opción: ")

if opcion == "1":
    print("\n La suma es:", num1 + num2)

elif opcion == "2":
    print("\n La resta es:", num1 - num2)

elif opcion == "3":
    print("\n La multiplicación es:", num1 * num2)

else:
    print("\n Opción no válida.")
