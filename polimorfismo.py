class Restaurant():

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def mostrar_informacion(self):
        print(f'Name: {self.name}, Category: {self.category}, Price: {self.price}')

    def get_price(self):
        return self.get_price
    
    def set_price(self, price):
        self.get_price = price

class Hotel(Restaurant):
    def __init__(self, name, category, price, alberca):
        super().__init__(name, category, price)
        self.alberca = alberca

## Reescribir un metodo
    def mostrar_informacion(self):
        print(f'Name: {self.name}, Category: {self.category}, Price: {self.price}, Alberca: {self.alberca}')

## Metodo que solo se encuentra en la clase Hotel
    def get_alberca(self):
        return self.alberca
    
hotel = Hotel('Suite', '5 Estrellas', 500, 'SI')
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)
