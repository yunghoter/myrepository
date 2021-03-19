class Person:
    name = 'Maxim'
    surname = 'Voloshko'
    age = 17
    born = 'Zvenyhorodka'
    studyPlace = 'CHSBC'
    
    def __init__(self, name, surname, age, born, studyPlace):
        self.name = name
        self.surname = surname
        self.age = age
        self.born = born
        self.studyPlace = studyPlace

Human = Person (input("Введіть ваше ім'я: "), input('Введіть вашу фамілію: '), input('Введіть ваш вік: '), 
input('Де ви народились?(Місто населеного пункту): '), input('Де ви навчаєтесь?: '))

print('\nВсім привіт, я {0} {1}. Мені {2} років, я з міста {3}, навчаюсь в {4}.' 
.format(Human.name, Human.surname, Human.age, Human.born, Human.studyPlace))

import datetime
def printTimeStamp(name):
 print('\nЧас компіляції: ' + str(datetime.datetime.now()))
 print('Автор програми: ' + name)
printTimeStamp("Максим Волошко")






