import numpy as np
import matplotlib.pyplot as plt

# Rango de x de 0 a 2*pi con paso 0.01
x = np.arange(0, 2 * np.pi, 0.01)
y = np.sin(x)

# Graficar
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Gráfica de la función seno")
plt.grid(True)
plt.show()

# Pedir texto al usuario
z = input("Ingrese cualquier texto: ")
print("Texto ingresado:", z)

