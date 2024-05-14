class Restaurant():
    def __init__(self, name, category, price):
        self.__name = name
        self.__category = category
        self.__price = price

    def mostrar_informacion(self):
        print(f'Name: {self.__name}, Category: {self.__category}, Price: {self.__price}')
    
    def get__price(self):
        return self.__price
    
    def set__price(self, price):
        self.__price = price

## Crear una clase hijo de restaurante
        
class Hotel(Restaurant):
    def __init__(self, name, category, price):
        super().__init__(name, category, price)

hotel = Hotel('Hotel', '5 Estrellas', 500)
hotel.mostrar_informacion()
