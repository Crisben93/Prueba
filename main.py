from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def main():
    while True:
        num_a = int(input("Ingrese el primer número: "))
        num_b = int(input("Ingrese el segundo número: "))

        print("¿Que operación desea realizar?")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        choice = input("Opción: ")

        if choice == '1':
            print(f"La suma de {num_a} y {num_b} es: {add(num_a, num_b)}")
        elif choice == '2':
            print(f"El resultado de restar {num_b} a {num_a} es: {subtract(num_a, num_b)}")
        elif choice == '3':
            print(f"El resultado de multiplicar {num_a} por {num_b} es: {multiply(num_a, num_b)}")
        elif choice == '4':
            print(f"El resultado de dividir {num_a} entre {num_b} es: {divide(num_a, num_b)}")
        elif choice == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
main()