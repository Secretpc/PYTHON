class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_de_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_de_cuenta = numero_de_cuenta
        self.balance = balance
    def __str__(self):
        return f"{self.nombre} {self.apellido} - Cuenta: {self.numero_de_cuenta} - Balance: {self.balance}"
    def depositar(self, valor):
        if valor > 0:
            self.balance += valor
        else:
            print("El valor debe ser positivo")
    def retirar(self, valor):
        if valor <= self.balance:
            self.balance -= valor
        else:
            print("Fondos insuficientes")

print("Hola, bienvenido al banco JCC")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
numero_de_cuenta = input("Ingresa tu numero de cuenta: ")
balance = float(input("Ingresa tu balance: "))
Cliente1 = Cliente(nombre, apellido, numero_de_cuenta, balance)


while True:
    print("Menu principal")
    print("1. Ver datos")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Ingresa su opcion: ")
    if opcion == "1":
        print(Cliente1)
    elif opcion == "2":
        valor = float(input("Ingresa tu valor: "))
        Cliente1.depositar(valor)
        print("El deposito ha sido realizado")
        print(Cliente1)
    elif opcion == "3":
        valor = float(input("Ingresa tu valor: "))
        Cliente1.retirar(valor)
        print(Cliente1)
    elif opcion == "4":
        break

input("Presiona Enter para continuar...")


