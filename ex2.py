class FormaBidimensional:
    def area(self):
        pass

    def perimetro(self):
        pass

class Circulo(FormaBidimensional):
    raio = int(input("Informe o raio do Círculo: "))
    def area(self):
        area = 3.14*(self.raio**2)
        print("A área do círculo é: %.2f"%(area))
    def perimetro(self):
        perimetro = 2*3.14*self.raio
        print("O perímetro do círculo é: %.2f"%(perimetro))

class Quadrado(FormaBidimensional):
    lado = int(input("Informe o lado do Quadrado: "))
    def area(self):
        area = self.lado**2
        print("A área do quadrado é: {}".format(area))
    def perimetro(self):
        perimetro = self.lado*4
        print("O perímetro do quadrado é: {}".format(perimetro))


objCirculo = Circulo()
objCirculo.area()
objCirculo.perimetro()

objQuadrado = Quadrado()
objQuadrado.area()
objQuadrado.perimetro()