from django.contrib.sessions.backends.base import SessionBase
from officeshop.models.products import Product

class CartSession(SessionBase):
    CART_SESSION_ID='cart'
    
    def __init__(self,session:dict) -> None:
        self.session:dict=session
        self.cart=self.session.get(self.CART_SESSION_ID)
        
        if not self.cart:
            self.cart=self.session[self.CART_SESSION_ID]={}
    def __iter__(self):
        product_ids = self.cart.keys()
        
        products=Product.objects.filter(id__in=product_ids)
        cart=self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product']=product
            
        for item in cart.values():
            item['price']=int(item['price'])
            item['total_price']=item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        return sum(item['quantity']for item in self.cart.values())
    
    def save(self):
        self.session.modified=True