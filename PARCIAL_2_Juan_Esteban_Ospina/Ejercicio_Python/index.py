from tkinter import Tk, Label, Entry, Button, messagebox


def verificar_division(num2):
    if num2 == 0:
        return True 
    return False  


def realizar_operacion(operacion):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = ""

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            if verificar_division(num2): 
                raise ZeroDivisionError("División por cero no permitida.")
            resultado = num1 / num2
        elif operacion == "potencia":
            if verificar_division(num2):  
                raise ZeroDivisionError("Potenciar un numero por cero es permitido.")
            resultado = num1 ** num2  

        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))


# Configuración de la interfaz gráfica
root = Tk()
root.title("Calculadora")
label_num1 = Label(root, text="Número 1:")
label_num1.pack()
entry_num1 = Entry(root)
entry_num1.pack()

label_num2 = Label(root, text="Número 2:")
label_num2.pack()
entry_num2 = Entry(root)
entry_num2.pack()

label_resultado = Label(root, text="Resultado:")
label_resultado.pack()

boton_suma = Button(root, text="Sumar", command=lambda: realizar_operacion("suma"))
boton_suma.pack()

boton_resta = Button(root, text="Restar", command=lambda: realizar_operacion("resta"))
boton_resta.pack()

boton_multiplicacion = Button(root, text="Multiplicar", command=lambda: realizar_operacion("multiplicacion"))
boton_multiplicacion.pack()

boton_division = Button(root, text="Dividir", command=lambda: realizar_operacion("division"))
boton_division.pack()

boton_potencia = Button(root, text="Potencia", command=lambda: realizar_operacion("potencia"))
boton_potencia.pack()

root.mainloop()
