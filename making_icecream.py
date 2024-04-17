from ice_cream import *
s=input("Enter Size:")
num=int(input("Enter number of toppings:"))
toppings=[]
for i in range(num):
    p=input("Enter toppings:")
    toppings.append(p)
#print(toppings)
result=add_topping(s,toppings)

print("Toppings on icecream are: ")
for i in toppings:
    print(i)


n=input("Enter shake flavour: ")
shake=make_shake(n)
print("Shake flavour choosen is ",shake)