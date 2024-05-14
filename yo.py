class Restaurant():

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.__price = price
    
    def mostrar_informacion(self):
        print(f'Name: {self.name}, Category: {self.category}, Price: {self.__price}')

    def get__price(self):
        return self.__price
    
    def set__price(self, price):
        self.__price = price
    

restaurant = Restaurant('Pizza', 'Americana', 50)
restaurant.mostrar_informacion()
restaurant.set__price(10)
price = restaurant.get__price()
print(price)

restaurant2 = Restaurant('Hamburger', 'Callejera', 85)
restaurant2.mostrar_informacion()
restaurant2.set__price(20)
price = restaurant2.get__price()
print(price)