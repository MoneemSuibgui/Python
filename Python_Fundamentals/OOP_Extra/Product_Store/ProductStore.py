class store:
    def __init__(self,name) :
        self.name=name
        self.prod_list=[]
# add product method 
    def add_product(self, new_product):
        self.prod_list.append(new_product)
        return self
# sell product method
    def sell_product(self,id):
        for index,product in enumerate(self.prod_list):
            if product.id==id:
                print('*'*20)
                print('this product is sell...')
                product.print_info()
                print('*'*20)
                self.prod_list.pop(index)
        return self 
#inflation method
    def inflation(self,percent_increase):
        for prod in  self.prod_list:
            prod.update_price(percent_increase,True)
        return self
# set_clearance method 
    def set_clearance(self,category,percent_discount):
        for product in self.prod_list:
            if product.category==category:
                product.update_price(percent_discount,False)
        return self
#display info method
    def display_info(self):
        for product in self.prod_list:
            product.print_info()
        return self

class Product:
    i=0
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
        self.id=Product.i
        Product.i+=1
# update price  
    def update_price(self,percent_change,is_increased):
        if  is_increased== True:
            self.price+=self.price*percent_change
        else:
            self.price-=self.price*percent_change
        return self
# print info method
    def print_info(self):
        print(f'the name of the product : {self.name}, the id of product is: {self.id} , its category : {self.category}, and its price : {self.price}.')


store1=store('fruits')
product1=Product('apple',3,'small_fruit')
product2=Product('strawberry',5,'small_fruit')
product3=Product('Ananas',10,'big_fruit')

store1.add_product(product1).add_product(product2).add_product(product3).sell_product(0).sell_product(1).sell_product(2).display_info()


