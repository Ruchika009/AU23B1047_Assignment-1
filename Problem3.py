#fooditems problem
def get_order(order):
    
    for i in order:
        print("Preparing your order-",i)
    
    print()
    print("The following order has been dispatched.")
    for k in order:
        print("order-",k)
    for j in order:
        order.remove(order[0])  

    return " "
M=int(input("No. of orders:"))
order=[]
for ele in range(M):
    food_items=input()
    order.append(food_items)
#print(order)
print(get_order(order))