class OperadorInvalido(Exception):
    pass

entrada = input("Operación: ")  # Ej: "10 / 2"

try:
    partes = entrada.split()
    num1 = float(partes[0])
    num2 = float(partes[2])
    operador = partes[1]

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = num1 / num2
    else:
        raise OperadorInvalido
    
    print(f"Resultado: {resultado}")

except ValueError:
    print("Error: Los números no son válidos")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
except OperadorInvalido:
    print("Error: Operador inválido")