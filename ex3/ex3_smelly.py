class Product:
    """Base class for all product types."""
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_discount_rate(self):
        """Return the discount rate for this product type. Override in subclasses."""
        raise NotImplementedError("Subclasses must implement get_discount_rate()")
    
    def get_tax_rate(self):
        """Return the tax rate for this product type. Override in subclasses."""
        raise NotImplementedError("Subclasses must implement get_tax_rate()")
    
    def get_category_name(self):
        """Return the category name for this product type. Override in subclasses."""
        raise NotImplementedError("Subclasses must implement get_category_name()")
    
    def apply_discount(self):
        """Apply discount to the product price."""
        discount = self.get_discount_rate()
        discounted_price = self.price - (self.price * discount)
        print(f"Discounted price for {self.name} ({self.get_category_name()}): {discounted_price}")
        return discounted_price
    
    def calculate_tax(self):
        """Calculate tax for the product."""
        tax_rate = self.get_tax_rate()
        tax = self.price * tax_rate
        print(f"Tax for {self.name} ({self.get_category_name()}): {tax}")
        return tax


class Electronics(Product):
    """Electronics product with 10% discount and 15% tax."""
    def get_discount_rate(self):
        return 0.10
    
    def get_tax_rate(self):
        return 0.15
    
    def get_category_name(self):
        return "Electronics"


class Clothing(Product):
    """Clothing product with 20% discount and 8% tax."""
    def get_discount_rate(self):
        return 0.20
    
    def get_tax_rate(self):
        return 0.08
    
    def get_category_name(self):
        return "Clothing"


class Grocery(Product):
    """Grocery product with 5% discount and 2% tax."""
    def get_discount_rate(self):
        return 0.05
    
    def get_tax_rate(self):
        return 0.02
    
    def get_category_name(self):
        return "Grocery"