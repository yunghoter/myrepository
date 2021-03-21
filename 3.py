class Ship:
    s_id = 0
    name = 'anyName'
    numberOfCrew = 0
 
class Spacecraft (Ship):
    AngOfrot = 180             #Угол повороту (Angle of rotation)
    TurningTime = 600          #Час повороту (Turning time)

class Starship (Spacecraft):
    RocketThrust = 3000        #Потужність ракетної тяги (Rocket thrust)
    TotСapacity = 2000         #Загальна місткість (Total capacity)

ship = Ship ()
ship.name = 'Naomi'
ship.numberOfCrew = 15
ship.s_id = 0
ship.AngOfrot = 180
ship.TurningTime = 300

spacecraft = Spacecraft ()
spacecraft.name = 'Voyager 1'
spacecraft.numberOfCrew = 0
spacecraft.s_id = 1
spacecraft.AngOfrot = 360
spacecraft.TurningTime = 100
spacecraft.RocketThrust = 250
spacecraft.TotCapacity = 150

starship = Starship ()
starship.name = 'Milano'
starship.numberOfCrew = 6
starship.s_id = 2
starship.AngOfrot = 180
starship.TurningTime = 200
starship.RocketThrust = 3000
starship.TotСapacity = 2000

print('\nНазва: {0}\nКількість екіпажу: {1}\nID: {2}\nУгол повороту: {3}\nЧас повороту: {4}\n'.format(ship.name, ship.numberOfCrew, ship.s_id, ship.AngOfrot, ship.TurningTime))

print('\nНазва: {0}\nКількість екіпажу: {1}\nID: {2}\nУгол повороту: {3}\nЧас повороту: {4}\nПотужність ракетної тяги: {5}\nЗагальна місткість: {6}\n'.format(spacecraft.name, spacecraft.numberOfCrew, spacecraft.s_id, spacecraft.AngOfrot, spacecraft.TurningTime, spacecraft.RocketThrust, spacecraft.TotCapacity))

print('\nНазва: {0}\nКількість екіпажу: {1}\nID: {2}\nУгол повороту: {3}\nЧас повороту: {4}\nПотужність ракетної тяги: {5}\nЗагальна місткість: {6}\n'.format(starship.name, starship.numberOfCrew, starship.s_id, starship.AngOfrot, starship.TurningTime, starship.RocketThrust, starship.TotСapacity))

import datetime
def printTimeStamp(name):
 print('\nЧас компіляції: ' + str(datetime.datetime.now()))
 print('Автор програми: ' + name)
printTimeStamp("Максим Волошко")