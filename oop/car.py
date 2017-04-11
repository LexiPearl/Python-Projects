class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price>10000:
            tax=.15
            return tax
        else:
            tax=.12
            return tax
        self.display_all()
    def display_all(self):
        print "Price =", self.price
        print "Speed =", self.speed
        print "Fuel =", self.fuel
        print "Mileage =", self.mileage
        print "Tax=", self.tax()


car1 = Car(2000, "35mph", "full", "15mpg")
car2 = Car(17000, "87mph", "half empty", "22mpg")
car3 = Car(8900, "100mph", "empty", "40mpg")
car4 = Car(20000, "79mph", "full", "28mpg")
car5 = Car(750, "10mph", "almost full", "19mpg")
car6 = Car(1000, "130mph", "full", "31mpg")

# car1.display_all()
# car2.display_all()
# car3.display_all()
# car4.display_all()
# car5.display_all()
# car6.display_all()
#
#
# class Car(object):
#     def __init__(self, price, speed, fuel, mileage):
#         self.speed = speed
#         self.fuel = fuel
#         self.mileage = mileage
#         self.price = price
#         if price > 10000:
#            self.tax = .15
#         else:
#             self.tax = .12
#         self.display_all()
#
#     def display_all(self):
#         print 'Price: ' + str(self.price)
#         print 'Speed: ' + str(self.speed) + 'mph'
#         print 'Fuel: ' + self.fuel
#         print 'Mileage: ' + str(self.mileage) + 'mpg'
#         print 'Tax: ' + str(self.tax)
#
# car1 = Car(2000, 35, 'Full', 15)
# car2 = Car(2000, 5, 'Not Full', 105)
# car3 = Car(2000, 15, 'Kind of Full', 95)
# car4 = Car(2000, 25, 'Full', 25)
# car5 = Car(2000, 45, 'Empty', 25)
# car6 = Car(20000000, 35, 'Empty', 15)
