class cajero:
    monto = 0
    print("Bienvenido al cajero automatico")
    def operaciones(self):
        self.opcion = int(input('''
        por favor seleccione que opcion elegira:
        1. consultar saldo.
        2. deposito a cuenta
        3. retirar dinero
        4. salir
        : '''))
        self.control = 0
        while self.control == 0:
            if self.opcion ==1:
                self.consultasaldo()
            elif self.opcion == 2:
                self.depositar()
            elif self.opcion == 3:
                self.retirar()
            elif self.opcion == 4:
                self.control = 1
                self.salir()
            else:
                print("opcion invalida, por favor seleccione una de las alternativas mostradas ")
                self.operaciones()


    def consultasaldo(self):
        print("su saldo disponible es: ",self.monto)
        print("¿desea realizar otra operacion?")
        self.operaciones()

    def depositar(self):
        self.deposito = int(input("ingrese el monto que desea depositar: "))
        self.monto = self.monto + self.deposito
        self.consultasaldo()

    def retirar(self):
        self.retiro = int(input("indique la cantidad de dinero que desea rerirar: "))
        self.control = 0
        while self.control == 0:
            if self.retiro > self.monto:
                print("""usted no cuenta con saldo disponible en este momento
                intente de nuevo mas tarde""")
                self.retiro = int(input("indique la cantidad de dinero que desea retirar: "))
            elif self.retiro <= self.monto:
                self.monto = self.monto - self.retiro
                self.control = 1
                print("cantidad retirada: ",self.retiro)
                self.consultasaldo()

    def salir(self):
        print("gracias por usar el cajero, vuelva pronto!")

ejecucion = cajero()
ejecucion.operaciones()
