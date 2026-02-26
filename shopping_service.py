import random

class ShoppingService:
    def __init__(self):
        self.vendors = ["Amazon", "Zappos", "Road Runner Sports", "Dick's Sporting Goods"]

    def search_product(self, product_details: dict):
        """
        Simulates searching for products across different vendors.
        """
        if not product_details:
            return []

        results = []
        base_price = random.uniform(120, 160)
        
        for vendor in self.vendors:
            price = round(base_price + random.uniform(-10, 10), 2)
            discount = 0
            if random.random() > 0.7:
                discount = round(price * random.uniform(0.05, 0.15), 2)
            
            results.append({
                "vendor": vendor,
                "product_name": product_details.get("product_name"),
                "size": product_details.get("size"),
                "width": product_details.get("width"),
                "price": price,
                "discount": discount,
                "final_price": round(price - discount, 2),
                "in_stock": True,
                "image_url": "/static/brooks_glycerin.png" if product_details.get("product_name") and ("glycerin" in product_details.get("product_name").lower() or "brooks" in product_details.get("product_name").lower()) else None
            })
        
        return results

    def get_best_offer(self, results: list):
        if not results:
            return None
        return min(results, key=lambda x: x["final_price"])

shopping_service = ShoppingService()
