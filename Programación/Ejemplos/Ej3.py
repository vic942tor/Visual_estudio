#Establecer los 20 primeros números de fibonacci
print("0")
Fib_1 = 0
Fib_2 = 1
cont = 2
while cont <= 20:
    Fib = Fib_1 + Fib_2
    print(Fib)
    Fib_2 = Fib_1
    Fib_1 = Fib
    cont += 1
