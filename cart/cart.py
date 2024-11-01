from Product.models import Product
from decimal import Decimal
CART_SESSION_ID='cart'
class Cart:
    def __init__(self, request):
        self.session=request.session
        cart=self.session.get(CART_SESSION_ID)
        if not cart:
            cart =self.session[CART_SESSION_ID]={}
        self.cart=cart
    def __iter__(self):
        product_ids =self.cart.keys()
        products=Product.objects.published().filter(id__in=product_ids)
        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product
        for item in cart.values():

            item['total_price']=Decimal(item['price'])*item['quntity']
            yield item
    def add(self,product,quantity=1):
        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0,'price':product.price}
        self.cart[product_id]['quantity']+=quantity
        self.save()
    def save(self):
        self.session.modified=True
