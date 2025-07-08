# main.py

from utils import saludo

def main():
    nombre = input("¿Cómo te llamas? ")
    mensaje = saludo(nombre)
    print(mensaje)

if __name__ == "__main__":
    main()