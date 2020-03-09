"""
FelipedelosH

6/20/2019

Se desea hacer un programa que dados 320 numeros aleatoreos de 0 a 400
los organice por medio de burbuja y muestre paso a paso con un slider que retarde


6/25/2019

Acabo de recivir ayuda de abulafia
https://es.stackoverflow.com/questions/273963/como-se-sincronizan-2-hilos-en-python
"""

from tkinter import *
from random import randint
from threading import *
from time import sleep


class GraphiBubbleShort:
    def __init__(self):
        self.pantalla = Tk()
        self.telaControl = Canvas(self.pantalla, width=640, height=80, bg="snow")
        self.telaGraficas = Canvas(self.pantalla, width=640, height=400, bg="white")
        self.btnPlay = Button(self.telaControl, text="PLAY", command=self.play)
        self.btnPausa = Button(self.telaControl, text="PAUSE", command=self.pause)
        self.lblIteracion = Label(self.telaControl, text="Iteracion: 0")

        """Variables"""
        self.vectorNumeros = []  # aqui se guardan los 640 numeros
        self.estoyRondando = False  # controla si el programa esta en ejecucion
        self.intSlider = 0.5

        self.hilo = Thread(target=self.run)
        """Preparativos para lanzar el programa"""
        # Se inicia el hilo
        self.hilo.start()
        # Se rellena el vector
        self.rellemarVectorNum()
        """Se muestra todo"""
        self.visualizarInterfaz()


    def visualizarInterfaz(self):
        self.pantalla.title("Burbuja by loko")
        self.pantalla.geometry("640x480")

        self.telaControl.place(x=0, y=0)
        self.btnPlay.place(x=10, y=20)
        self.btnPausa.place(x=60, y=20)
        self.lblIteracion.place(x=10, y=50)
        self.telaGraficas.place(x=0, y=80)

        """Se procede a graficar el vector"""
        self.graficarVector()

        # Se añade un evento al bucle de eventos para que tan pronto
        # como arranque mainloop() lo procese. Ese evento consiste en 
        # invocar la función self.update_graphic lo antes posible (tras 0ms)
        self.pantalla.after(0, self.update_graphic)
        self.pantalla.mainloop()

    def rellemarVectorNum(self):
        if not self.estoyRondando:
            self.vectorNumeros.clear()
            for i in range(320):
                self.vectorNumeros.append(randint(1, 400))

    def update_graphic(self):
        """Esta función actualiza el estado de la gráfica cada 30ms"""

        # Solo la actualizamos si realmente está cambiando, para ahorrar CPU
        if self.estoyRondando:
            self.graficarVector()
            # Cambiamos también la etiqueta con el número de iteraciones
            self.lblIteracion["text"] = "Iteracion: " + str(self.Iteracion)
        self.pantalla.after(30, self.update_graphic)

    def graficarVector(self):
        # Borramos el canvas y lo repintamos
        self.telaGraficas.delete("vector")
        for i in range(0, len(self.vectorNumeros)):
            x0 = 1 + (2 * i)
            self.telaGraficas.create_rectangle(
                x0, 0, x0 + 1, self.vectorNumeros[i], tags="vector"
            )

    def play(self):
        self.pantalla.title("Burbuja by loko:PLAY")
        self.estoyRondando = True

    def pause(self):
        self.pantalla.title("Burbuja by loko:PAUSE")
        self.estoyRondando = False

    def run(self):
        contadori = 0
        contadorj = 0
        aux = 0
        # La variable Iteracion pasa a ser un atributo del objeto, para poder
        # compartirla con la función que actualiza la interfaz
        self.Iteracion = 0
        while True:
            while self.estoyRondando and contadori < len(self.vectorNumeros):
                # procedo a instaciar j en lo que no esta ordenado
                contadorj = 0
                while self.estoyRondando and contadorj < len(self.vectorNumeros) - (contadori + 1):
                    if (self.vectorNumeros[contadorj] < self.vectorNumeros[contadorj + 1]):
                        aux = self.vectorNumeros[contadorj + 1]
                        self.vectorNumeros[contadorj + 1] = self.vectorNumeros[contadorj]
                        self.vectorNumeros[contadorj] = aux

                    if self.estoyRondando:
                        self.Iteracion += 1
                        contadorj = contadorj + 1

                sleep(0.01)
                """Se incrementa i"""
                if self.estoyRondando:
                    contadori = contadori + 1


sw = GraphiBubbleShort()