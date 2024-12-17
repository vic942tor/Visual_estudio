/* Programa que pide un numero hasta que introduce 0.
 * El programa pasará de kilogramos a gramos
 * 
 */
double kg = 0; 
string entrada; 
Console.WriteLine("Introduce los kg (escribe 0 para salir):");
while (true)
{
    entrada = Console.ReadLine();

    if (Double.TryParse(entrada, out kg))
    {
        if (kg == 0)
        {
            Console.WriteLine("Programa finalizado.");
            break; 
        }
        double gramos = kg * 1000;
        Console.WriteLine(gramos + " gramos");
        Console.WriteLine("Introduce los kg (escribe 0 para salir):");
    }
    else
    {
        Console.WriteLine("Entrada inválida. Por favor, introduce un número válido.");
    }
}
