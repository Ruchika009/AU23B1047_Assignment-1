
from ice_cream import *

toppings=add_topping("Small","springles","hot fudge","whipped cream")
print("Toppings on icecream are: ")
print(*toppings, sep='\n')

shake=make_shake("nuts")
print("Shake flavour choosen is ",shake)