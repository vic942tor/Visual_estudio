class CuentaBancaria:
    def __init__(self, titular, nif, saldo, limite_retiro):
        self.titular = titular
        self.nif = nif
        self.saldo = saldo
        self.limite_retiro = limite_retiro
    @property
    def titular(self):
        return self._titular
    @titular.setter
    def titular(self, value):
        if not value.strip():
            raise ValueError("El titular no puede estar vacío.")
        self._titular = value
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, value):
        try:
            value = float(value)
            if value < 0:
                raise ValueError("El saldo no puede ser negativo.")
            self._saldo = value
        except ValueError:
            raise ValueError("El saldo debe ser un número válido.")
    @property
    def limite_retiro(self):
        return self._limite_retiro
    @limite_retiro.setter
    def limite_retiro(self, value):
        try:
            value = float(value)
            if value <= 0:
                raise ValueError("El límite de retiro debe ser un número positivo.")
            self._limite_retiro = value
        except ValueError:
            raise ValueError("El límite de retiro debe ser un número válido.")
    def depositar(self, monto):
        try:
            monto = float(monto)
            if monto <= 0:
                raise ValueError("El monto a depositar debe ser positivo.")
            self._saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self._saldo:.2f}")
        except ValueError:
            print("Error: Ingrese un monto válido.")
    def retirar(self, monto):
        try:
            monto = float(monto)
            if monto <= 0:
                raise ValueError("El monto a retirar debe ser positivo.")
            if monto > self._saldo:
                print("Fondos insuficientes.")
            elif monto > self._limite_retiro:
                print(f"No puedes retirar más de {self._limite_retiro:.2f} por transacción.")
            else:
                self._saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: {self._saldo:.2f}")
        except ValueError:
            print("Error: Ingrese un monto válido.")
    def mostrar_saldo(self):
        print(f"Saldo actual: {self._saldo:.2f}")
    def mostrar_info(self):
        print(f"Titular: {self.titular}")
        print(f"NIF: {self.nif[:3]}******")
        print(f"Saldo actual: {self._saldo:.2f}")
        print(f"Límite de retiro: {self._limite_retiro:.2f}")
while True:
    try:
        titular = input("Introduce el nombre del titular: ")
        nif = input("Introduce el NIF: ")
        saldo = input("Introduce el saldo de la cuenta: ")
        limite_retiro = input("Introduce el límite de retiro: ")
        cuenta = CuentaBancaria(titular, nif, saldo, limite_retiro)
        break
    except ValueError as e:
        print(f"Error: {e}. Inténtalo de nuevo.")
print("\nInformación de la cuenta:")
cuenta.mostrar_info()
while True:
    print("\nOpciones:")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar saldo")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        monto = input("Introduce el monto a depositar: ")
        cuenta.depositar(monto)
    elif opcion == "2":
        monto = input("Introduce el monto a retirar: ")
        cuenta.retirar(monto)
    elif opcion == "3":
        cuenta.mostrar_saldo()
    elif opcion == "4":
        print("Gracias por usar el sistema bancario.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")