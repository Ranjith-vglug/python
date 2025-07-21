class bike:
    company="honda"
    address="chennai main road"

    def details(self):
        print("WWW.HONDA.com")
class bike1(bike):
    def __init__ (self):
        self.name="bike"
        self.year=2025
    
    def products_detials(self):
        print(self.name)
        print(self.year)
        print(self.company)
        print(self.address)

bike=bike1()
bike.products_detials()
bike.details()
