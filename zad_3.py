class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (f"Adres: {self.address}.\n"
                f"Powierzchnia: {self.area} m2\n"
                f"Pokoje: {self.rooms}\n"
                f"Cena: ${self.price}\n")


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"Adres: {self.address}.\n"
                f"Powierzchnia: {self.area} m2\n"
                f"Rooms: {self.rooms}\n"
                f"Działka: {self.plot} m2\n"
                f"Cena: ${self.price}")


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Adres: {self.address}.\n"
                f"Pow: {self.area} m2\n"
                f"Pokoje: {self.rooms}\n"
                f"Piętro: {self.floor}\n"
                f"Cena: ${self.price}")



house = House(area=120, rooms=4, price=300000, address="ul Agonalna 5", plot=500)
flat = Flat(area=80, rooms=3, price=200000, address="AAAAAAAAAAAAAAAAAAAA", floor=5)

print(house, "\n")
print(flat)
