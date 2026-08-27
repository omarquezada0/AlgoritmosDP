import tkinter as tk
import matplotlib.pyplot as plt
root=tk.Tk()
root.title("Saludador")
root.geometry("360x220")

x = [3, 5, 7, 8, 9]
y = [10,11, 3, 4, 7]

plt.plot(x,y)
plt.title("Mi primera gráfica")
plt.xlabel("eje x")
plt.ylabel(" eje y")
plt.scatter(x,y)
plt.show()


def saludar():
    nombre = ent.get().strip()
    if not nombre:
        nombre = "Omar"
    lbl.config(text =f"Que onda, {nombre}")

lbl = tk.Label(root, text="Que pedo, escribe tu nombre y presiona el boton.")
lbl.pack(pady=10)
ent = tk.Entry(root)
ent.pack(pady=10)

btn =tk.Button(root, text="Saludar", command=saludar)
btn.pack(pady=10)

root.mainloop()