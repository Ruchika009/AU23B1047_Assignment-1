#adding size parameter
def get_tshirt(brand_name,size=None):
    #get.name()
    intialize='"Hii '
    sen=', the brand you are looking for is available in store."'
    sen1=', Unfortunately the brand you are looking for is not available in store."'
    n=get_name()
    available_brand=["Peter England", "Raymond","Arrow","Allen Solly","Gucci","H&M","Zara","Calvin Klein"]
    S=["Allen Solly","Gucci","H&M","Zara","Calvin Klein"]
    M=["Peter England", "Raymond","Arrow","Allen Solly","Gucci"]
    L=["Raymond","Arrow","Allen Solly","Gucci","H&M","Zara"]


    find=[]
    
    if size=='S':
        find+=S
        print("Available brand :",find)
    elif size=='M':
        find+=M
        print("Available brand :",find)
    elif size=='L':
        find+=L
        print("Available brand :",find)
    elif size==None:
        find+=available_brand
        print("Available brand :",find)
    else:
        print("Size is unavailable")
        
    for ele in find:
        
        if ele==brand_name:
            
            greeting=intialize+n+sen
            
            return greeting
            
    else:
        greeting=intialize+n+sen1
        return greeting
        

def get_name():
    name=input("Enter name:")
    return name
n=input("Enter brand name:")
optional=input("Do you want to search according to size-Yes/No:")
if optional=="Yes":
    size=input("Enter size:")
    print(get_tshirt(n,size))

else:
    print(get_tshirt(n))