class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("guau, guau")
            
    def __str__(self):
        return "Soy el perro {}".format(self.nombre)
    
class Perroasistencia():
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
    
    def __str__(self):
        print("perro de asistencia de {}".format(self.amo))
        
    def pasear(self):
            print("ayudo ami dueño {}" .format(self.amo))
    
    def ladrar(self):
        if self.trabajando:
            print("No puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor

salchicho = Perro("salchicho", 3, 15)
lola = Perro("lola", 5, 3.5)
salchicho.ladrar()
lola.ladrar()
daga = Perroasistencia("daga", 3, 12, "pedro")
daga.__str__()




