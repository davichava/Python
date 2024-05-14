class Restaurant():

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.__price = price  # Con 2 __se vuelve privada y no se puede modificar la informacion ## Con 1 _ se vuelve protected

    def mostrar_informacion(self):
        print(f'Nombre: {self.name}, Category: {self.category}, Price: {self.__price}')

    def get__price(self):
        return self.__price
    
    def set__price(self, price):
        self.__price = price

restaurant = Restaurant('Pizza', 'Americana', 25)
restaurant.mostrar_informacion()
restaurant.set__price(80)
price = restaurant.get__price()
print(price)
# print(restaurant.__price)
# restaurant.__price = 80 ## NOSE PUEDE MODIFICAR CON __PRIVATE

restaurant2 = Restaurant('Hamburgers', 'Callejera', 100)
# print(restaurant2.__price)
# restaurant2.__price = 40## NOSE PUEDE MODIFICAR CON __PRIVATE
restaurant2.mostrar_informacion()