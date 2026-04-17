class Car:
    def __init__(self,brand,model,color,engine,mileage):     #special method
        self.brand = brand
        self.model = model
        self.color = color
        self.engine = engine
        self.mileage = mileage
    def info(self):        # self is mandatory
        print(f"Model : {self.model}")
        print(f"Engine : {self.engine}")
        print(f"Color : {self.color}")
        print(f"Engine : {self.engine}")
        print(f"Mileage : {self.mileage}")
car1 = Car("Maruti Suzuki","Swift","Red","1197cc",25)
car1.info()
car2 = Car("Hyundai","Creta","Black","2000cc",21)
car2.info()