class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponibilidad = True
    
    def prestar(self):
        self.disponibilidad = False
        print("Libro prestado")

    def devolver(self):
        self.disponibilidad = True
        print("Libro devuelto")

    def datos(self):
        print(f"Libro: {self.titulo}, disponibilidad: {self.disponibilidad}")

    def getAutor(self):
        return self.autor
    
    def getTitulo(self):
        return self.titulo
    
    def getDisponibilidad(self):
        return self.disponibilidad

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agragar_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregado")
    
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.datos())
    
    def buscar(self, autor):
        for libro in self.libros:
            if(libro.getAutor() == autor):
                return libro

        print("Libro no encontrado")
        return None

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if(libro.getTitulo() == titulo):
                if(libro.getDisponibilidad() == True):
                    libro.prestar()
                    print("Se presto correctamente")
                else:
                    print("Libro ocupado")
                
class Digital(Libro):
    def __init__(self, titulo, autor, año, tipo, tamaño):
        super().__init__(titulo, autor, año)
        self.tipo = tipo
        self.tamaño = tamaño
    
    def prestar(self):
        self.disponibilidad = True

libro01 = Libro("Libro 01", "Autor 01", 2025)
libro02 = Libro("Libro 02", "Autor 02", 2025)
libro03 = Libro("Libro 03", "Autor 03", 2025)
digital01 = Digital("Libro 04", "Autor 04", 2025, "PDF", "5mb")
digital02 = Digital("Libro 05", "Autor 05", 2025, "PDF", "3mb")

biblioteca = Biblioteca()
biblioteca.agragar_libro(libro01)
biblioteca.agragar_libro(libro02)
biblioteca.agragar_libro(libro03)
biblioteca.agragar_libro(digital01)
biblioteca.agragar_libro(digital02)
# Presta el libro
biblioteca.prestar_libro("Libro 01")
# Presta 5 veces un libro digital
biblioteca.prestar_libro("Libro 04")
biblioteca.prestar_libro("Libro 04")
biblioteca.prestar_libro("Libro 04")
biblioteca.prestar_libro("Libro 04")
biblioteca.prestar_libro("Libro 04")
# Presta un libro ya prestado
biblioteca.prestar_libro("LIbro 01")
# Busca un libro por autor
print(biblioteca.buscar("Autor 01").getTitulo())