"""
Ejercicio:

Crear un script de calculadora que:

Pida dos números al usuario.
Permita seleccionar una operación aritmética.
Muestre el resultado usando f-strings.

"""

def leer_numero(mensaje: str) -> float:
    """
    Lee un número desde consola y valida que sea correcto.
    Retorna un float.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: ingrese un número válido.")

def calcular(num1: float, num2: float, op: str) -> float | None:
    """
    Ejecuta una operación aritmética básica.
    Retorna el resultado o None si la operación no es válida.
    """
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/" and num2 != 0:
        return num1 / num2
    elif op == "%":
        return num1 % num2 if num2 != 0 else None
    elif op == "//":
        return num1 // num2 if num2 != 0 else None
    elif op == "^":
        return num1 ** num2
    
    return None

def main() -> None:
    """Función principal de la calculadora."""
    num1 = leer_numero("Ingrese el primer número: ")
    num2 = leer_numero("Ingrese el segundo número: ")

    op = input("Seleccione operación (+, -, *, /): ")
    
    operaciones = ["+", "-", "*", "/", "%", "//", "^"]
    while op not in operaciones:
        print("Operación no válida. Intente nuevamente.")
        op = input("Seleccione operación: ")
    
    resultado = calcular(num1, num2, op)

    if resultado is not None:
        print(f"Resultado: {resultado:.2f}")
    else:
        print("Error: operación inválida o división por cero.")

if __name__ == "__main__":
    main()
