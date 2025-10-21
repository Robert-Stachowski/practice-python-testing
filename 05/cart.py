import copy

class Cart:
    def __init__(self):
        self.products = []
        
    def add(self, product):
        if "name" not in product:
            raise ValueError("Brak pola name")
        name = product["name"] # bez .get - bo juz sprawdziliśmy czy klucz istnieje
        if name is None or not isinstance(name, str):
            raise ValueError("Niepoprawny format")        
        if "price" not in product:  
            raise ValueError("brak pola cena")
        price = product["price"]
        if price is None or not isinstance(price,(int, float)) or isinstance(price, bool):
            raise ValueError("niepoprawny format")
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