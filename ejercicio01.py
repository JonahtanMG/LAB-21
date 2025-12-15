class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def nombre_figura(self):
        return f"{self.nombre}"

    def area(self):
        return ""

    def perimetro(self):
        return ""
        

class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
    
    def area(self):
        return f"Area: {self.base*self.altura}"
    
    def perimetro(self):
        return f"Perimetro {(self.base+self.altura)*2}"
    
class Triangulo(Figura):
    def __init__(self, nombre, base, altura, diagonal):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
        self.diagonal = diagonal
    
    def area(self):
        return f"Area: {self.base*self.altura/2}"

    def perimetro(self):
        return f"Perimetro {(self.base+self.altura+self.diagonal)}"
        
class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def area(self):
        return f"Area: {self.radio*3.14}"
    
    def perimetro(self):
        return f"Perimetro {2*self.radio*3.14}"
    
rectangulo = Rectangulo("Rectangulo 01", 10, 20)
triangulo = Triangulo("Triangulo 01", 3, 4, 5)
circulo = Circulo("Cirulo 01", 5)
lista = []
lista.append(rectangulo)
lista.append(triangulo)
lista.append(circulo)

for figura in lista:
    print(figura.nombre_figura())
    print(figura.area())
    print(figura.perimetro())
