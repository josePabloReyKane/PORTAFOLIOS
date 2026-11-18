import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("500x550")
ventana.configure(bg='#2b2b2b')  # Fondo oscuro

# 1. Abrir la imagen con Image (no con ImageTk)
ima = Image.open("D:\\PORTAFOLIOS\\PRACTICA_S_I\\asset SI\\Imagenes\\extra.png")
print(ima.size)

# 2. (Opcional) cambiar el tamaño
ima = ima.resize((200, 200))


ima_tk = ImageTk.PhotoImage(ima)

# 4. Mostrarla en un Label
etiqueta = tk.Label(ventana, image=ima_tk, bg='#2b2b2b')
etiqueta.image = ima_tk   # evita que Python borre la imagen de memoria
etiqueta.pack(pady=20)

ventana.mainloop()
