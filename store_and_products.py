class store:
    def __init__(self, name , list_of_products):
        self.name = name
        self.list = list_of_products
        self.product
class product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        return self
    def update_price(self, percent_change, is_increased):
        if self.is_increased > self.price:
            self.price += self.percent_change 
        else: self.price -= self.percent_change
        return self
    def print_info(self,):
        print("Product: " + self.name + "Catergory: " + self.catergory + "Price: " self.price)
        return self

