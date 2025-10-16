class Cart:
    def __init__(self,products):
        self.products = []
        
    def add_product(self, product):
        price = product.get("price")
        if "name" not in product or not product["name"]:
            raise ValueError("Brak pola name")
        if "price" not in product or not isinstance(price,(int, float)):
            raise ValueError("niepoprawny format, lub brak ceny")
        self.products.append(product) 
    
    def remove_product(self, product_name):
        for product in self.products:
            if product["name"] == product_name:
                self.products.remove(product)
                break