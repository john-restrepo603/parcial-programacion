from pelicula import Pelicula

def main():
    pelicula1 = Pelicula(
        codigo=1602,
        titulo="Rambo",
        duracion=169,
        director=" Sylvester Stallone",
        prestada=False
    )

    print(pelicula1)
    
if __name__ == "__main__":
    main()