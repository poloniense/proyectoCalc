import tkinter
import tkinter.font as tkfont
import math
from math import sqrt

ventana = tkinter.Tk()
ventana.title("Calculadora")
ventana.config(bg="black")

fuente = tkfont.Font(family="ubuntu",size=17)
fresultado = tkfont.Font(family="ubuntu",size=16)
fsig = tkfont.Font(family="ubuntu", size=16)

nro1 = tkinter.Label(ventana,width=10, height=5)
nro1.config(font = fuente,bg="black",fg="#ADD8E6")
nro1.grid()

sig = tkinter.Label(ventana,width=8, height=5)
sig.config(font = fsig,bg="black",fg="green")
sig.grid(row=0,column=1) 

nro2 = tkinter.Label(ventana,width=10, height=5)
nro2.config(font = fuente,bg="black",fg="#ADD8E6")
nro2.grid(row=0,column=2)

resultado = tkinter.Label(ventana,width=22, height=6)
resultado.config(font=fresultado, bg="#0f1513", fg="#ADD8E6", highlightthickness=1, highlightbackground="white")
resultado.grid(row=0,column=3, columnspan=2)

def salir () :
    ventana.quit()

def mostrar_numero(numero):
    if sig["text"] == "":
        nro1["text"] += str(numero)
    else:
        nro2["text"] += str(numero)

def mostrar_signo(signo):
    sig["text"] = signo

def borrar():
    nro1["text"] = ""
    sig["text"] = ""
    nro2["text"] = ""
    resultado["text"] = ""

def cambiar_signo():
    if sig["text"] == "":
        nro1["text"] = str(-int(nro1["text"]))
    else:
        nro2["text"] = str(-int(nro2["text"]))

def calcular():
    if sig["text"] == "+":
        resultado["text"] = int(nro1["text"]) + int(nro2["text"])
    elif sig["text"] == "-":
        resultado["text"] = int(nro1["text"]) - int(nro2["text"])
    elif sig["text"] == "x":
        resultado["text"] = int(nro1["text"]) * int(nro2["text"])
    elif sig["text"] == "÷":
        resultado["text"] = int(nro1["text"]) / int(nro2["text"])
    elif sig["text"] == "°":
        resultado["text"] = int(nro1["text"]) ** int(nro2["text"])
    elif sig["text"] == "√":
        resultado["text"] = round(math.sqrt(int(nro2["text"])))
    else:
        resultado["text"] = "Error"

img0 = tkinter.PhotoImage(file='imagenes/0.png')
cero = tkinter.Button(ventana,image=img0,width=128, height=120,command=lambda:mostrar_numero(0),bg="black",fg="#ADD8E6")
cero.grid(row=4,column=0)

img1 = tkinter.PhotoImage(file='imagenes/1.png')
uno = tkinter.Button(ventana,image=img1,width=128, height=120,command=lambda:mostrar_numero(1),bg="black",fg="#ADD8E6")
uno.grid(row=3,column=0)

img2 = tkinter.PhotoImage(file='imagenes/2.png')
dos = tkinter.Button(ventana,image=img2,width=128, height=120,command=lambda:mostrar_numero(2),bg="black",fg="#ADD8E6")
dos.grid(row=3,column=1)

img3 = tkinter.PhotoImage(file='imagenes/3.png')
tres = tkinter.Button(ventana,image=img3,width=128, height=120,command=lambda:mostrar_numero(3),bg="black",fg="#ADD8E6")
tres.grid(row=3,column=2)

img4 = tkinter.PhotoImage(file='imagenes/4.png')
cuatro = tkinter.Button(ventana,image=img4,width=128, height=120,command=lambda:mostrar_numero(4),bg="black",fg="#ADD8E6")
cuatro.grid(row=2,column=0)

img5 = tkinter.PhotoImage(file='imagenes/5.png')
cinco = tkinter.Button(ventana,image=img5,width=128, height=120,command=lambda:mostrar_numero(5),bg="black",fg="#ADD8E6")
cinco.grid(row=2,column=1)

img6 = tkinter.PhotoImage(file='imagenes/6.png')
seis = tkinter.Button(ventana,image=img6,width=128, height=120,command=lambda:mostrar_numero(6),bg="black",fg="#ADD8E6")
seis.grid(row=2,column=2)

img7 = tkinter.PhotoImage(file='imagenes/7.png')
siete = tkinter.Button(ventana,image=img7,width=128, height=120,command=lambda:mostrar_numero(7),bg="black",fg="#ADD8E6")
siete.grid(row=1,column=0)

img8 = tkinter.PhotoImage(file='imagenes/8.png')
ocho = tkinter.Button(ventana,image=img8,width=128, height=120,command=lambda:mostrar_numero(8),bg="black",fg="#ADD8E6")
ocho.grid(row=1,column=1)

img9 = tkinter.PhotoImage(file='imagenes/9.png')
nueve = tkinter.Button(ventana,image=img9,width=128, height=120,command=lambda:mostrar_numero(9),bg="black",fg="#ADD8E6")
nueve.grid(row=1,column=2)

imgsum = tkinter.PhotoImage(file="imagenes/suma.png")
sumar = tkinter.Button(ventana,image=imgsum,width=128,height=120,command=lambda:mostrar_signo("+"),bg="black",fg="green")
sumar.grid(row=4,column=3)

imgres = tkinter.PhotoImage(file="imagenes/resta.png")
restar = tkinter.Button(ventana,image=imgres,width=128,height=120,command=lambda:mostrar_signo("-"),bg="black",fg="green")
restar.grid(row=3,column=3)

imgpor = tkinter.PhotoImage(file= "imagenes/por.png")
por = tkinter.Button(ventana,image=imgpor,width=128,height=120,command=lambda:mostrar_signo("x"),bg="black",fg="green")
por.grid(row=2,column=3)

imgdiv = tkinter.PhotoImage(file="imagenes/division.png")
dividir = tkinter.Button(ventana,image=imgdiv,width=128,height=120,command=lambda:mostrar_signo("÷"),bg="black",fg="green")
dividir.grid(row=1,column=3)

imgpon = tkinter.PhotoImage(file="imagenes/potencia.png")
potencia = tkinter.Button(ventana,image=imgpon,width=128,height=120,command=lambda:mostrar_signo("°"),bg="black",fg="green")
potencia.grid(row=1,column=4)

imgraiz = tkinter.PhotoImage(file="imagenes/raiz.png")
raiz = tkinter.Button(ventana,image=imgraiz,width=128,height=120,command=lambda:mostrar_signo("√"),bg="black",fg="green")
raiz.grid(row=2,column=4)

imgcambio = tkinter.PhotoImage(file="imagenes/cambio.png")
cambio_signo = tkinter.Button(ventana,image=imgcambio,width=128,height=120,command=cambiar_signo,bg="black",fg="green")
cambio_signo.grid(row=3,column=4)

imgigual = tkinter.PhotoImage(file="imagenes/igual.png")
igual = tkinter.Button(ventana,image=imgigual,width=128,height=120,command=calcular,bg="black",fg="green")
igual.grid(row=4,column=2)

borrars = tkinter.PhotoImage(file='imagenes/borrar.png')
borra = tkinter.Button(ventana,image=borrars,width=128,height=120,command=borrar,bg="black")
borra.grid(row=4,column=1)

imgsal = tkinter.PhotoImage(file= "imagenes/salir.png")
salida = tkinter.Button(ventana,image=imgsal,width=128,height=120,command=salir,bg="black",fg="red")
salida.grid(row=4,column=4)

ventana.mainloop()