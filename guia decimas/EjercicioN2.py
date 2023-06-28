class conjunto:
    def final(self):

        self.aleatorios()

        self.numeros()

        self.contar()

    def aleatorios(self):
        nombres = []
    
        self.n1 = input("ingrese el primer nombre: ")
        self.n2 = input("ingrese el segundo nombre: ")
        self.n3 = input("ingrese el tercer nombre: ")
        self.n4 = input("ingrese el cuarto nombre: ")
        self.nombres = self.n1 + self.n2 + self.n3 + self.n4
        return nombres
    
    def numeros(self):

        self.cont1 = len(self.n1)
        self.cont2 = len(self.n2)
        self.cont3 = len(self.n3)
        self.cont4 = len(self.n4)
        self.cont5 = len(self.nombres)

    def contar(self):
        print(f"el primer nombre tiene: {self.cont1} letras")
        print(f"el segundo nombre tiene: {self.cont2} letras")
        print(f"el tercer nombre tiene: {self.cont3} letras")
        print(f"el cuarto nombre tiene: {self.cont4} letras")
        print(f"el numero total de letras es: {self.cont5}")
              
              
              
resultado = conjunto()

resultado.final()

