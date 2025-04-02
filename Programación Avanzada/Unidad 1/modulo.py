import time
import matplotlib.pyplot as plt
import math

class Punto2D:
    def __init__(self, x, y):
        """Se inicializa la clase"""
        self.x = x
        self.y = y

    def __repr__(self):
        """Se imprime el punto"""
        return f"({self.x},{self.y})"

    def __call__(self, escalar):
        """Multiplica por un escalar usando la sintaxis "A(escalar)" como una función."""
        return Punto2D(self.x * escalar, self.y * escalar)

    def __add__(self, otro):
        """Suma de dos puntos."""
        return Punto2D(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        """Resta de dos puntos."""
        return Punto2D(self.x - otro.x, self.y - otro.y)

    def __mul__(self, escalar):
        """Multiplica por un escalar usando "escalar * A"."""
        return Punto2D(self.x * escalar, self.y * escalar)

    def __rmul__(self, escalar):
        """Permite multiplicar por un escalar por la derecha usando "A * escalar", y devuelve el valor self.__mul__(escalar)."""
        return self.__mul__(escalar)

    def __abs__(self):
        """Devuelve la distancia del punto al origen."""
        return math.sqrt(self.x**2 + self.y**2)

    
    def grafica(self):
        """Se imprime el punto en un gráfico con etiquetas y título."""
        plt.figure(figsize=(5, 5))
        plt.scatter(self.x, self.y, color='red', label=f'Punto ({self.x},{self.y})')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.xlim(self.x - 2, self.x + 2)
        plt.ylim(self.y - 2, self.y + 2)
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.title("Gráfica del Punto2D")
        plt.legend()
        plt.grid()
        plt.show()

    @staticmethod
    def tiempo_ejecucion(func):
        """Decorador para medir el tiempo de ejecución de una función."""
        def wrapper(*args, **kwargs):
            inicio = time.time()
            resultado = func(*args, **kwargs)
            fin = time.time()
            print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
            return resultado
        return wrapper

    @tiempo_ejecucion
    def distancia(self, otro):
        """Calcula la distancia entre dos puntos."""
        return math.sqrt((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2)

