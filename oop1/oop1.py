# class Human:
#     height=None
#     age=None
    
# human_one=Human()
# human_two=Human()

# print(human_one.age)
# print(human_two.age)

# human_one.age=22
# human_two.age=27

# delattr(human_one, 'height')
# delattr(human_two, 'height')

# print(hasattr(human_one, 'height'))
# print(hasattr(human_two, 'height'))

# human_one.name="Илья"
# print(human_one.name)

class Goods:
    title = 'Мороженое'
    weight=151
    tp='"Еда"'
    price=12321

Goods.price=125
Goods.weight=100
print(Goods.weight)

class Car:
    ...
    
Car.model="Тойота"
Car.color="черный"
Car.number="П34А123"
print(Car.model)
