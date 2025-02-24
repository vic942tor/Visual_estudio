# Se quiere implementar una clase que permita utilizar números fraccionarios
# num/den
# La clase debe llamarse Fracción y recibirá dos parámetros de tipo entero num y
# den.
# La idea es que se va a trabajar la fracción de forma algebraica y no con números
# decimales.
# La clase debe implementar los siguientes métodos
# __str__ que genera el string “num / den” de los componentes de la fracción.
# simplica( fracc ) que recibe una fracción y la simplica.
# suma( a, b ) que recibe dos fracciones y realiza la operación de la suma de las
# fracciones, el resultado se debe simplicar.
# resta( a, b ) que recibe dos fracciones y realiza la operación de la resta de las
# fracciones, el resultado se debe simplicar.
# multiplicacion( a, b ) que recibe dos fracciones y realiza la operación de la
# multiplicación de las fracciones, el resultado se debe simplicar.
# division( a, b ) que recibe dos fracciones y realiza la operación de la división de las
# fracciones, el resultado se debe simplicar.
# multpornumero(frac, num) que recibe una fracción y un número entero y realiza la
# operación de multiplicar la fracción por el número.
# cambiarsigno( fracc ) recibe una fracción y le cambia el signo
# potencia( fracc, número ) que recibe una fracción y un número entero y realiza la
# operación de la potencia de la fracción elevada al número.
# Tener en cuenta que para la simplicación se debe utilizar la función del mcm() que
# la pueden encontrar en la librería math.
# Se debe tener un programa principal que permita probar todos los métodos que
# se han pedido

import math

class Fraccion:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("El denominador no puede ser cero")
        self.num = num
        self.den = den
        self.simplifica()
    def __str__(self):
        return f"{self.num} / {self.den}"
    def simplifica(self):
        mcd = math.gcd(self.num, self.den)
        self.num //= mcd
        self.den //= mcd
    @staticmethod
    def suma(a, b):
        num = a.num * b.den + b.num * a.den
        den = a.den * b.den
        return Fraccion(num, den)
    @staticmethod
    def resta(a, b):
        num = a.num * b.den - b.num * a.den
        den = a.den * b.den
        return Fraccion(num, den)
    @staticmethod
    def multiplicacion(a, b):
        return Fraccion(a.num * b.num, a.den * b.den)
    @staticmethod
    def division(a, b):
        if b.num == 0:
            raise ValueError("No se puede dividir por una fracción con numerador 0")
        return Fraccion(a.num * b.den, a.den * b.num)
    @staticmethod
    def multpornumero(frac, num):
        return Fraccion(frac.num * num, frac.den)
    @staticmethod
    def cambiarsigno(frac):
        return Fraccion(-frac.num, frac.den)
    @staticmethod
    def potencia(frac, exponente):
        if exponente < 0:
            return Fraccion(frac.den ** abs(exponente), frac.num ** abs(exponente))
        return Fraccion(frac.num ** exponente, frac.den ** exponente)
    
if __name__ == "__main__":
    f1 = Fraccion(3, 4)
    f2 = Fraccion(2, 5)
    print("Fracción 1:", f1)
    print("Fracción 2:", f2)
    print("Suma:", Fraccion.suma(f1, f2))
    print("Resta:", Fraccion.resta(f1, f2))
    print("Multiplicación:", Fraccion.multiplicacion(f1, f2))
    print("División:", Fraccion.division(f1, f2))
    print("Multiplicar por número (2):", Fraccion.multpornumero(f1, 2))
    print("Cambio de signo:", Fraccion.cambiarsigno(f1))
    print("Potencia al cuadrado:", Fraccion.potencia(f1, 2))
    print("Potencia negativa (-1):", Fraccion.potencia(f1, -1))