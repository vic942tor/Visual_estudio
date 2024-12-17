
/*
 *  Programa que pide por teclado una cadena y una letra, de manera que
 *  elimina las 3 primeras ocurrencias de la letra que encuentre en la cadena y lo muestre
    por pantalla.
 *  Por ejemplo, alejandra y a debería devolver lejndr
 */

using System;
class Program
{
    static void Main(string[] args)
    {
        String cadena, letra, nuevaCadena = "";
        int i, cont = 0;

        Console.WriteLine("Introduzca una cadena: ");
        cadena = Console.ReadLine();

        Console.WriteLine("Introduzca una letra: ");
        letra = Console.ReadLine();
        if (letra.Length != 1)
        {
            Console.WriteLine("Debe introducir una sola letra.");
            return;
        }
        for (i = 0; i < cadena.Length; i++)
        {
            if (cadena[i] == letra[0] && cont < 3)
            {
                cont++; 
            }
            else
            {
                nuevaCadena += cadena[i]; 
            }
        }
        Console.WriteLine("Resultado: " + nuevaCadena);
    }
}
