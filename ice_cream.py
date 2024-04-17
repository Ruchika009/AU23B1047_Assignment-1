def add_topping(Scoop_size,*toppings):
    #Scoop_size=["small","medium","big"]
    #toppings=["springles","hot fudge","whipped cream","crushed nuts"]
    for j in toppings:
        output=j
    return toppings

def make_shake(shake_favour):
    if shake_favour=="nuts":
        return shake_favour
    elif shake_favour=="fruits":
        return shake_favour
    else:
        return "no such shake available"
    

