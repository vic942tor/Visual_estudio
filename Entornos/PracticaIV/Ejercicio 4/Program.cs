/*
	 *  Programa que llama a la funcion sumarDigitos(int num), la cual devuelve la suma
	 *  de cada uno de los digitos del valor que se le pasa por parametro
	 *  sumarDigitos(1223) devuelve 1 + 2 + 2 + 3 = 8
*/
int res;
res = sumarDigitos(1223);
Console.WriteLine("La suma de los dígitos es: " + res);
static int sumarDigitos(int num)
{
    int suma = 0; // Inicializamos la suma en 0
    int aux;      // Variable auxiliar para almacenar el dígito actual

    // Bucle que extrae los dígitos y los suma
    while (num > 0)
    {
        aux = num % 10; // Obtenemos el último dígito
        suma += aux;    // Lo sumamos a la variable 'suma'
        num /= 10;      // Eliminamos el último dígito dividiendo entre 10
    }

    return suma; // Retornamos la suma total
}

