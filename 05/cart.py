class Cart:
    def __init__(self,products):
        self.products = []
        
    def add_product(self, product):
        name = product.get("name") or ""
        price = product.get("price")
        if name not in product:
            raise ValueError("Brak pola name")
        if isinstance(price,int) or not name in product:
            raise ValueError("niepoprawny format, lub brak ceny")
    
