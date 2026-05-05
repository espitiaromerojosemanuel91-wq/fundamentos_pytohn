<<<<<<< HEAD
=======

>>>>>>> b585fd1c18bc908e51f7036e2ea80527d65775f2
def calculadora():
    print("--- Calculadora Básica ---")
    print("Operaciones: + , - , * , /")
    
    while True:
        num1 = float(input("Primer número: "))
        operacion = input("Operación (+, -, *, /) o 's' para salir: ")
        
        if operacion.lower() == 's':
            break
            
        num2 = float(input("Segundo número: "))

        if operacion == '+':
            print(f"Resultado: {num1 + num2}")
        elif operacion == '-':
            print(f"Resultado: {num1 - num2}")
        elif operacion == '*':
            print(f"Resultado: {num1 * num2}")
        elif operacion == '/':
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Error: No se puede dividir por cero.")
        else:
            print("Operación no válida.")
        
        print("-" * 20)

<<<<<<< HEAD
calculadora()
=======
calculadora()
>>>>>>> b585fd1c18bc908e51f7036e2ea80527d65775f2
