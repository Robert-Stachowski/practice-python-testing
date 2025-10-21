import copy

class Cart:
    def __init__(self):
        self.products = []
        
    def add(self, product):
        if "name" not in product or not product["name"]:
            raise ValueError("Brak pola name")
        price = product.get("price")
        if "price" not in product or not isinstance(price,(int, float)):
            raise ValueError("niepoprawny format, lub brak ceny")
        self.products.append(product) 
    
    def remove(self, product_name):
        for product in self.products:
            if product["name"] == product_name:
                self.products.remove(product)
                break

    def total(self):
        total_sum = sum(p["price"] for p in self.products)
        return float(total_sum)
    
    def items(self):
        return copy.deepcopy(self.products)