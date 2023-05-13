from ObjectDB import ObjectDB

# A sample User class which inherits from `ObjectDB` class
class Car(ObjectDB):

    def __init__(self, make, model, year, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage


# Let's first build a few class objects
cars = [
    Car('Toyota', 'Corolla', 2018, 'Blue', 25000),
    Car('Honda', 'Civic', 2020, 'Red', 15000),
    Car('Ford', 'Mustang', 2015, 'Yellow', 40000)
]

# With this simple line of code 
cars_df = Car.df(cars)

print(cars_df)

# To do the reverse
cars_objs = Car.init_pandas_list(cars_df)

print(type(cars_objs[0]))

