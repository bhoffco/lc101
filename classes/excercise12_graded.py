

class Car:

<<<<<<< HEAD
  def __init__(self, level):
    
    self.level = level

example_car1 = Car(10)

print(example_car1.level)

=======
    def __init__(self, level):

        self.level = level

    def add_gas(self, gas_added):
        self.level = self.level + gas_added

    def fill_up(self):

        if self.level >= 13:
            return 0
        else:
            gas_needed = 13 - self.level
            self.add_gas(gas_needed)
            return gas_needed


example_car1 = Car(5.5)
example_car2 = Car(8)


print(example_car1.level)


print(example_car1.fill_up())
>>>>>>> d34158ca6b2de6b282992671c7772fc1107be0c4
