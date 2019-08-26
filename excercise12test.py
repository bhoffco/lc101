

class Car:

    def __init__(self, level):

        self.level = level

    def add_gas(self, gas_added):
        return gas_added + self.level

    def fill_up(self):

        if self.level >= 13:
            return 0
        else:
            return 13 - self.level


def main():

    example_car1 = Car(5.5)

    print(example_car1.fill_up())
    print(example_car1.level)

    print(example_car1.add_gas(5))

    print(example_car1.fill_up())


if __name__ == "__main__":
    main()
