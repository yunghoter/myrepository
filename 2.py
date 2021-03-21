class Ship:
    s_id = 0
    name = 'anyName'
    numberOfCrew = 0
    y = 0
     
    def __init__(self, name, numberOfCrew, y, s_id): 
        self.name = name
        self.numberOfCrew = numberOfCrew
        self.y = y
        self.s_id = s_id
    
    def plus(Ship):
        return Ship.y ++ 1
    
ship1 = Ship ('Veronica', 23, 1, 1)
ship2 = Ship ('Fortuna', 31, 3, 2)
ship3 = Ship ('Hendalf', 15, 8, 3)
ship4 = Ship ('Omega', 9, 3, 4)
ship5 = Ship ('Naomi', 2, 12, 5)
ship6 = Ship ('Maria', 24, 6, 6)

print('Назва корабля: {0}. Кількість екіпажу: {1}. Y координата: {2}'.format(ship1.name, ship1.numberOfCrew, ship1.y))

ch = (input('Хочете пересунути корабель вгору? Y - так. N - ні.   '))
if ch == 'Y':
    ship1.y = ship1.plus()
    print('Тепер корабель {0} має Y координату: {1}'.format(ship1.name, ship1.y))
else:
    print('Ну ок')

z = 1
while z != 0:
    ch1 = (int(input('Введіть номер корабля про який хочете подивитися інформацію (ввід закінчується нулем): \n1)Veronica \n2)Fortuna \n3)Hendalf \n4)Omega \n5)Naomi \n6)Maria\n')))
    z = ch1
    if(ch1 == 1):
        print('Назва: {0}\nКількість екіпажу: {1}\nY координата: {2}\nID корабля: {3}' .format(ship1.name, ship1.numberOfCrew, ship1.y, ship1.s_id))
    elif(ch1 == 2):
        print('Назва: {0}\nКількість екіпажу: {1}\nY координата: {2}\nID корабля: {3}' .format(ship2.name, ship2.numberOfCrew, ship2.y, ship2.s_id))
    elif(ch1 == 3):
        print('Назва: {0}\nКількість екіпажу: {1}\nY координата: {2}\nID корабля: {3}' .format(ship3.name, ship3.numberOfCrew, ship3.y, ship3.s_id))
    elif(ch1 == 4):
        print('Назва: {0}\nКількість екіпажу: {1}\nY координата: {2}\nID корабля: {3}' .format(ship4.name, ship4.numberOfCrew, ship4.y, ship4.s_id))
    elif(ch1 == 5):
        print('Назва: {0}\nКількість екіпажу: {1}\nY координата: {2}\nID корабля: {3}' .format(ship5.name, ship5.numberOfCrew, ship5.y, ship5.s_id))
    elif(ch1 == 6):
        print('Назва: {0}\nКількість екіпажу: {1}\nY координата: {2}\nID корабля: {3}' .format(ship6.name, ship6.numberOfCrew, ship6.y, ship6.s_id))
    elif(ch1 > 6):
        print('Неправильне число')
        continue
    else:
        print('Введено неправильне число!')

x = 1
while x != 0:
    ch2 = (int(input('Введіть номер корабля про який хочете передвинути вверх (ввід закінчується нулем): \n1)Veronica \n2)Fortuna \n3)Hendalf \n4)Omega \n5)Naomi \n6)Maria\n')))
    x = ch2
    if(ch2 == 1):
        ship1.y = ship1.plus()
        print('Тепер корабель {0} має Y координату: {1}'.format(ship1.name, ship1.y))
    elif(ch2 == 2):
        ship2.y = ship2.plus()
        print('Тепер корабель {0} має Y координату: {1}'.format(ship2.name, ship2.y))
    elif(ch2 == 3):
        ship3.y = ship3.plus()
        print('Тепер корабель {0} має Y координату: {1}'.format(ship3.name, ship3.y))
    elif(ch2 == 4):
        ship4.y = ship4.plus()
        print('Тепер корабель {0} має Y координату: {1}'.format(ship4.name, ship4.y))
    elif(ch2 == 5):
        ship5.y = ship5.plus()
        print('Тепер корабель {0} має Y координату: {1}'.format(ship5.name, ship5.y))
    elif(ch2 == 6):
        ship6.y = ship6.plus()
        print('Тепер корабель {0} має Y координату: {1}'.format(ship6.name, ship6.y))
    elif(ch2 > 6):
        print('Неправильне число')
        continue
    else:
        print('Завершення роботи...')

import datetime
def printTimeStamp(name):
 print('\nЧас компіляції: ' + str(datetime.datetime.now()))
 print('Автор програми: ' + name)
printTimeStamp("Максим Волошко")

    




















    







