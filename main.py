"""
Wea vista en internet
... Probar que siempre hay un numero repetido y decir cual es el repetido.
Se desea crear un metodo que me diga si en un arreglo hay numeros duplicados.

el arreglo costa de 1 hasta n+1 posiciones. con numeros comprendidos entre 1 y n 

No se puede organizar el vector
No se puede crear una estructura






1 -> tkinter va a generar la interfaz grafica
2 -> se implemento la interfaz y metodos para ver el vector


03/09/2020:

Se crea el slider que controla la velocidad con que
se ejecuta el programa.

# Nota para el futuro... funciona y no se como... y no refrescar... >> Para generaciones futuras.

"""

# Se importan los graficos
from tkinter import *
# Se importa el random
import random
# El programa debe de parar en algun momento por ello
import time


class Software:
    def __init__(self):
        self.pantalla = Tk()
        self.tela = Canvas(self.pantalla, height=480, width=900, bg="snow") 
        self.lblTamanoVector = Label(self.tela, text="Ingrese tamano del vector: ")
        self.txtTamanoVector = Entry(self.tela, width=6)
        self.btnStart = Button(self.tela, text="START", command=self.rellenarVector)
        self.btnSig = Button(self.tela, text=">>", bg="green", command=lambda : self.actualizarListaNumeros(12))
        self.btnAnt = Button(self.tela, text="<<", bg="green", command=lambda : self.actualizarListaNumeros(-12))
        self.lblPivoteA = Label(self.tela, text="Pivote A: ")
        self.lblPivoteB = Label(self.tela, text="Pivote B: ")
        self.lblVelocidad = Label(self.tela, text="Velocidad de Ejecucion: ")
        self.slederVelocidad = Scale(self.tela, from_=0, to=100, orient=HORIZONTAL)

        """Variables"""
        self.tamano = 0
        self.vector = []
        self.pivoteA = 0
        self.pivoteB = 0

        # Estas son las variables para hacer scroll en el vector
        self.listoParaPintar = False
        self.posPintar = 0
        self.posNumerosCinta = [] 


        # Se lanza la pantalla
        self.visualizarPantalla()


    def visualizarPantalla(self):
        self.pantalla.title("Encontrar Numeros duplicados")
        self.pantalla.geometry("900x480")

        self.tela.place(x=0, y=0)
        self.lblTamanoVector.place(x=20, y=10)
        self.txtTamanoVector.place(x=180, y=12)

        self.lblPivoteA.place(x=400, y=10)
        self.lblPivoteB.place(x=600, y=10)
        self.lblVelocidad.place(x=400, y=50)
        self.slederVelocidad.place(x=600, y=50)

        self.btnStart.place(x=260, y=10)
        # Refrecamos la pantalla
        self.update_graphic
        self.pantalla.mainloop()

    """
    Este metodo refresca la pantalla cada 30 milisegundos
    """
    def update_graphic(self):
        # Solo la actualizamos si realmente está cambiando, para ahorrar CPU
        self.pantalla.after(30, self.update_graphic)

    """Los botones anterior y siguiente solo se muestran si hay scroll"""
    def pintarBtnNext(self):
        self.btnSig.place(x=740, y=220)

    def pintarBtnPrevius(self):
        self.btnAnt.place(x=10, y=220)


    """Los botones anterior y siguiente se borran dependiendo si no hay que mostrar"""
    def borrarBTNNext(self):
        self.btnSig.place_forget()

    def borrarBTNPrevius(self):
         self.btnAnt.place_forget()

    """
    Primero se valida que sea un numero insertado
    Luego se rellena el vector
    Luego se muestra el vector en pantalla
    """
    def rellenarVector(self):
        if self.validarTamano():
            # Se rellena el vector

            # Si el vector es muy grande se pintan >> y <<
            if self.tamano+1 > 12:
                self.pintarBtnNext()
            else:
                self.borrarBTNNext()
                self.borrarBTNPrevius()

            for i in range(0, self.tamano+1):
                k = random.randint(1, self.tamano)
                self.vector.append(k)

            # Se pinta el vector
            self.pintarCinta()

            # Se busca la solucion
            self.solve()


    def validarTamano(self):
        try:
            self.tamano = int(self.txtTamanoVector.get())
            return True
        except:
            return False 


    """
    Se pinta una cinta en la pantalla 
    """
    def pintarCinta(self):
        # Se pinta la cinta con cuadritos
        for i in range(0, 12):
            self.tela.create_rectangle((60*(i+1)), 150, (60*(i+2)), 180, width=5, fill='red')
            # Se guardan x0 y y0 de la cinta:
            self.posNumerosCinta.append((60*(i+1)))

        # Se proceden a pintar los numeritos que existan

        if len(self.vector) < 12:
            # Se pinta solo lo que quepa
            aux = 0
            for i in range(len(self.vector)):
                self.tela.create_text(self.posNumerosCinta[aux]+20,
                 165,
                  text=str(self.vector[aux]), tag="numeritos")
                aux = aux + 1
        else:
            # Se pintan los primeros 12
            aux = 0
            for i in range(12):
                self.tela.create_text(self.posNumerosCinta[aux]+20,
                 165,
                  text=str(self.vector[aux]), tag="numeritos")
                 
                aux = aux + 1

        # Se procede a pintar una leyenda
        aux = 0
        for i in range(1, 13):
            self.tela.create_text(self.posNumerosCinta[aux]+20,
                 200,
                  text=str(i), tag="leyenda")
            aux = aux + 1


    """Este metodo actualiza la lista de primos que se muestran
    spc puede ser: +12 o -12 para moverse a la der o izq
    """
    def actualizarListaNumeros(self, spc):
        # Si esta entre 0 y el tamano del vector
        if len(self.vector)>self.posPintar+spc>=0:
            # se actualiza el puntero
            # Esta sera la nueva posA a pintar
            self.posPintar = self.posPintar + spc
            # Se captura el siguiente paquete de numeros
            paquete = []
            if self.posPintar+12<len(self.vector):
                # Esto Siginifica que se pueden pintar 12 posiciones
                for i in range(self.posPintar, self.posPintar+12):
                    paquete.append(self.vector[i])
                
               
            else:
                # Esto significa que quedan menos de 12 numeros para pintar
                for i in range(self.posPintar, len(self.vector)):
                    paquete.append(self.vector[i])    


            # Ya se capturo el vector de los sig primos a mostar procedo actualizar
            aux = 0
            for i in self.tela.find_withtag("numeritos"):
                if aux < len(paquete):
                    self.tela.itemconfigure(i, text=str(paquete[aux]))
                    aux = aux + 1
                else:
                    self.tela.itemconfigure(i, text="X")

            # Se procede a actualizar la leyenda
            for i in self.tela.find_withtag("leyenda"):
                # Capturo el elemento actual
                nro = int(self.tela.itemcget(i, 'text'))
                # lo actulizo sumandole spc
                nro = nro + spc
                self.tela.itemconfigure(i, text=str(nro))

        # Ojo: si no hay nada mas atras se borra el btn
        # Si hay algo adelante se pinta el btn
        if self.posPintar<12:
            self.borrarBTNPrevius()
        else:
            self.pintarBtnPrevius()

        # Ojo si no hay nada mas adelante se borra el btn
        # Si hay cosas por ver adelante se pinta
        if self.posPintar+12>=len(self.vector):
            self.borrarBTNNext()
        else:
            self.pintarBtnNext()


    # Este metodo es el que busca las coincidencias
    def solve(self):
        self.pivoteA = self.vector[0]
        self.pivoteB = self.vector[0]
        for i in self.vector:
            # Se actualizan los pivotes en el entorno grafico
            self.lblPivoteA['text'] = "Pivote A: " + str(self.pivoteA)
            self.lblPivoteB['text'] = "Pivote B: " + str(self.pivoteB)
            # Si pivoteA == pivoteB es xq estamos parados en el repetido
            if self.pivoteA == self.pivoteB:
                # Se actualiza el valor de los pivotes
                self.pivoteA = self.vector[self.pivoteA]
                self.pivoteB = self.vector[self.vector[self.pivoteB]]
                break


            # Se para lo que diga el scale
            k = (int(self.slederVelocidad.get()) / 100)+0.4
            time.sleep(k)

s = Software()