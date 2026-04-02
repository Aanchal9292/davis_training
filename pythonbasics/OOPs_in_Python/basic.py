class Car:
    def __init__(self,engine,mileage):     #special method
        self.engine = engine
        self.mileage = mileage
    def info(self):        # self is mandatory
        print(f"Engine : {self.engine}")
        print(f"Mileage : {self.mileage}")
car1 = Car("4000cc",14)
car1.info()
car2 = Car("1200cc",23.9)
car2.info()