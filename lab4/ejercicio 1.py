class enunciado:
    def final(ejercicio):
        ejercicio.minimo()
        ejercicio.insertar()
        ejercicio.encontrar()

    def minimo(ejercicio):
        estatura=[]
        ejercicio.mini = min(pacientes)
        print(round(ejercicio.mini,1))
        return estatura
    
    def insertar(ejercicio):
        pacientes.append(["ricardo",[1,71]])

    def encontrar(ejercicio):
        ejercicio.buscar = pacientes.index("dario")

        if pacientes and ejercicio.buscar:
            print("se encontro el elemnto",ejercicio.buscar)
        else:
            print("no se ha encontrado ele elemnto")

        for n in ejercicio.buscar:
            print(n)

pacientes = ["pedro", 1,78], ["constanza",1,56], ["amanda", 1,62], ["dario", 1,89], ["fernanda", 1,67]
resultado = enunciado()
resultado.final()


