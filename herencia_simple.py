class Animal:
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
    
class Terrestre(Animal):
    def set_num_patas(self, num_patas):
        self.__num_patas = num_patas
        
    def get_num_patas(self):
        return self.__num_patas
    
    def imprime_nombre(self):
        print(self.__nombre)
    
class Acuatico(Animal):
    def set_num_aletas(self, num_aletas):
        self.__num_aletas = num_aletas
        
    def get_num_aletas(self):
        return self.__num_aletas

class Gato(Terrestre):
    def maullar(self):
        print("¡Miauuuuu!")

isidoro = Gato()
isidoro.set_num_patas(4)
isidoro.set_nombre('Isidoro')
isidoro.imprime_nombre()
print(f'Tengo un gato que se llama {isidoro.get_nombre()}.')
print(f'Ese gato tiene {isidoro.get_num_patas()} patas.')
print('Y ahora va a maullar:')
isidoro.maullar()

