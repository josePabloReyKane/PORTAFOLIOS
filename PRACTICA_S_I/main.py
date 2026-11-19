import tkinter as tk
from PIL import Image, ImageTk
import random



ANCHO_PANTALLA = 600
ALTO_PANTALLA = 600
TAMANO_ESPACIO = 30
VELOCIDAD = 150 # tiempo en milisegundos entre cada movimiento
COLOR_FONDO = "#032143"

ventana = tk.Tk()
ventana.title("Space inveder")
ventana.geometry("500x550")
ventana.resizable(width=False, height=False)
ventana.configure(bg='#2b2b2b')  # Fondo oscuro


ima = Image.open("D:\\PORTAFOLIOS\\PRACTICA_S_I\\asset SI\\Imagenes\\green.png")
player = Image.open("D:\\PORTAFOLIOS\\PRACTICA_S_I\\asset SI\\Imagenes\\player.png")


ima = ima.resize((35, 35))


canvas = tk.Canvas(ventana, bg=COLOR_FONDO, height=ALTO_PANTALLA, width=ANCHO_PANTALLA)

cordenadas_enemigos = [
    [30,30],[30,60],[30,90],[30,120],[30,150],[30,180],
    [60,30],[60,60],[60,90],[60,120],[60,150],[60,180],
    [90,30],[90,60],[90,90],[90,120],[90,150],[90,180],
]

cordenadas_player=[ANCHO_PANTALLA/2,ALTO_PANTALLA]


def crea_enemigos():
    for i in range(0,4):
        for j in range(0,10):
            ima_tk = ImageTk.PhotoImage(ima)
            etiqueta = tk.Label(ventana, image=ima_tk, bg='#2b2b2b')
            
            etiqueta.image = ima_tk   # evita que Python borre la imagen de memoria
            etiqueta.grid(row=i, column=j, padx=5, pady=5)


def cambiar_direccion(nueva_direccion):
    global direccion 
    if nueva_direccion == "izquierda":
        direccion = nueva_direccion
    elif nueva_direccion == "derecha":
        direccion = nueva_direccion
    elif nueva_direccion == "abajo":
        direccion = nueva_direccion
    elif nueva_direccion == "arriba":
        direccion = nueva_direccion
     
ventana.bind('<a>', lambda event: cambiar_direccion("izquierda"))
ventana.bind('<d>', lambda event: cambiar_direccion("derecha"))
ventana.bind('<w>', lambda event: cambiar_direccion("arriba"))
ventana.bind('<s>', lambda event: cambiar_direccion("abajo"))



def comprobar_colisiones():
    x, y = player[0]

    # Choque con bordes de pantalla 
    if x < 0 or x >= ANCHO_PANTALLA or y < 0 or y >= ALTO_PANTALLA:
        return True 

    # Choques con su propio cuerpo
    for segmento in player[1:]:
        if x == segmento[0] and y == segmento[1]:
            return True 

    return False


def mover_paso():
    global cuerpo_serpiente, puntuacion, posicion_comida 
    x, y = cuerpo_serpiente[0]

    """
    ANTES
    cuerpo_serpiente = [
            [0, 60],
            [0, 30],
            [0, 0]
        ]
    """
    if direccion == "arriba":
        y -= TAMANO_ESPACIO
    elif direccion == "abajo":
        y += TAMANO_ESPACIO
    elif direccion == "izquierda":
        x -= TAMANO_ESPACIO
    elif direccion == "derecha":
        x += TAMANO_ESPACIO

    player.grid(row=50, column=50, padx=5, pady=5)
   

    if x == posicion_comida[0] and y == posicion_comida[1]:
        puntuacion += 1
        
        canvas.delete("comida")
        
    else:
        player.pop()


    canvas.delete("player.png")
    for coordenada in player:
        x = coordenada[0]
        y = coordenada[1]

        # x0, y0, x1, y1 

        x1 = x + TAMANO_ESPACIO
        y1 = y + TAMANO_ESPACIO
        


    
    ventana.after(VELOCIDAD, mover_paso)


crea_enemigos()
ventana.mainloop()
