#get_tshirt function
def get_tshirt(brand_name):
    #get.name()
    intialize='"Hii '
    sen=', the brand you are looking for is available in store."'
    sen1=', Unfortunately the brand you are looking for is not available in store."'
    n=get_name()
    available_brand=["Peter England", "Raymond","Arrow","Allen Solly","Gucci"]
    for i in available_brand:
        if brand_name==i:
            greeting=intialize+n+sen
            return greeting
    else:
        greeting=intialize+n+sen1
        return greeting
        

def get_name():
    name=input("Enter name:")
    return name
n=input("Enter brand name:")
print(get_tshirt(n))