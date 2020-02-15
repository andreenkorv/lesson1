price = 100
discount = 5
price_with_discount = price - price * discount / 100
print(price_with_discount)

###
def price_with_discount(price=0, discount=0):
    if discount>0 and price>0:
        if discount > 100:
            return price
        else:
            return price - price * discount / 100
    return [abs(price), abs(discount)]
        
###
def discount_sum(price, discount):
    return price * discount / 100


print(price_with_discount(122))
print(price_with_discount(125, 104))
print(price_with_discount(-125, 99))
print(price_with_discount(-125, -99))
print(price_with_discount(125, -99))