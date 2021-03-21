class Ship:
    height = 0    #Ширина
    width = 0     #Довжина
    crew = 0      #Екіпаж
    speed = 0     #Швидкість
    tonnage = 0       #Тоннаж
    runwaySize = 0    #Розмір взлітної полоси
    cruisingRange = 0     #Дальність плавання
    destructiveAbility = 0      #Винищувальна здатність
    locatorPower = 0         #Потужність локаторів
    sizeOfdecks = 0    #Розмір палуб

    def __init__(self, height, width, crew, speed, tonnage, runwaySize, cruisingRange, destructiveAbility, locatorPower, sizeOfdecks):
        self.height = height
        self.width = width
        self.crew = crew
        self.speed = speed
        self.tonnage = tonnage
        self.runwaySize = runwaySize
        self.cruisingRange = cruisingRange
        self.destructiveAbility = destructiveAbility
        self.locatorPower = locatorPower
        self.sizeOfdecks = sizeOfdecks

class military_ship (Ship):
    height = 0    #Ширина
    width = 0     #Довжина
    crew = 0      #Екіпаж
    speed = 0     #Швидкість
    tonnage = 0       #Тоннаж
    runwaySize = 0    #Розмір взлітної полоси
    cruisingRange = 0     #Дальність плавання
    destructiveAbility = 0      #Винищувальна здатність
    locatorPower = 0         #Потужність локаторів
    sizeOfdecks = 0    #Розмір палуб

class civil_ship (Ship):
    height = 0    #Ширина
    width = 0     #Довжина
    crew = 0      #Екіпаж
    speed = 0     #Швидкість
    tonnage = 0       #Тоннаж
    runwaySize = 0    #Розмір взлітної полоси
    cruisingRange = 0     #Дальність плавання
    destructiveAbility = 0      #Винищувальна здатність
    locatorPower = 0         #Потужність локаторів
    sizeOfdecks = 0    #Розмір палуб

air_carrier = military_ship (100, 600, 700, 100, 2000, 2000, 350, 5000, 130, 1000)
landing_ship = military_ship (10, 30, 12, 180, 1, 0, 200, 40, 0, 20)
destroyer = military_ship (8, 20, 8, 180, 0.5, 0, 300, 300, 0, 15)
boat = military_ship (3, 7, 4, 190, 0.3, 0, 200, 250, 0, 10)
corvette = military_ship (10, 20, 18, 180, 1, 0, 300, 500, 0, 30)

container_ship = civil_ship (200, 1000, 500, 200, 10000, 0, 7000, 0, 0, 400)
tanker = civil_ship (100, 700, 300, 160, 7000, 0, 8000, 0, 0, 100)
fishing_ship = civil_ship (10, 20, 6, 100, 2, 0, 150, 0, 0, 10)
research_ship = civil_ship (5, 15, 10, 170, 0.3, 0, 500, 0, 1000, 15)
yacht = civil_ship (10, 50, 5, 200, 0.3, 0, 400, 0, 0, 30)











