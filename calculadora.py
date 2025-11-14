print("bienvenido a la calculadora")
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def menu():
    print("=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "5":
        print("Saliendo...")
        break
def pedir_numero(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Error: por favor ingresa un número válido.")

a = pedir_numero("Ingrese el primer número: ")
b = pedir_numero("Ingrese el segundo número: ")


    if opcion == "1":
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        print("Resultado:", dividir(a, b))
    else:
        print("Opción inválida")
