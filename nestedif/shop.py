print("⚆_⚆ 🍦Welcome to Classic Delights🍨 ^_^")
print("Here's are some of our signature dishes!")
print("IceCreams🍨")
print("1) Nutty Delight")
print("2) Lotus Bicoff")
print("3) French Twist")
print("4) Tiramisu")
order=int(input("Please select your order🍽️❤️  "))
if order==1:
    print("Nutty Delight😎")
    cost=169
    cc=int(input("do you want 1) cup or 2)cone: "))
    if cc==1:
            #print("cost for cone is Rs.199 ")
        cost+=10
        scoop=int(input("do you want double scoop if yes press 1 else 0: "))
        if scoop==1:
        #print("total cost: Rs. ",cost)
           print("total cost: Rs. ",cost)
           print("Addons:")
           print("1) Gems Rs.10")
           print("2) Nuts Rs.50")
           print("3) Waffle Rs.20")
            #addons=input("do you need any add ons y/n:")
           toppings=int(input("Enter your addon: "))
           if toppings==1:
              cost+=10
              print("total cost: Rs. ",cost)
           elif toppings==2:
              cost+=50
              print("total cost: Rs. ",cost)
           else:
              cost+=20
              print("total cost: Rs. ",cost)
        else:
            print("total cost: Rs. ",cost)
    elif cc==2:
        cost+=20
        scoop=int(input("do you want double scoop if yes press 1 else 0: "))
        if scoop==1:
            print("total cost: Rs. ",cost)
            print("Addons:")
            print("1) Gems Rs.10")
            print("2) Nuts Rs.50")
            print("3) Waffle Rs.20")
            toppings=int(input("Enter your addon: "))
            if toppings==1:
                cost+=10
                print("total cost: Rs. ",cost)
            elif toppings==2:
                cost+=50
                print("total cost: Rs. ",cost)
            else:
                cost+=20
                print("total cost: Rs. ",cost)
        else:
            print("total cost: Rs. ",cost)
    else:
            print("invalid options")
if order==2:
    print("Lotus Biscoff😁")
    cost=199
    cc=int(input("do you want 1) cup or 2)cone: "))
    if cc==1:
            #print("cost for cone is Rs.199 ")
        cost+=10
        scoop=int(input("do you want double scoop if yes press 1 else 0: "))
        if scoop==1:
        #print("total cost: Rs. ",cost)
           print("total cost: Rs. ",cost)
           print("Addons:")
           print("1) Gems Rs.10")
           print("2) Nuts Rs.50")
           print("3) Waffle Rs.20")
            #addons=input("do you need any add ons y/n:")
           toppings=int(input("Enter your addon: "))
           if toppings==1:
              cost+=10
              print("total cost: Rs. ",cost)
           elif toppings==2:
              cost+=50
              print("total cost: Rs. ",cost)
           else:
              cost+=20
              print("total cost: Rs. ",cost)
        else:
            print("total cost: Rs. ",cost)
    elif cc==2:
        cost+=20
        print("total cost: Rs. ",cost)
        print("Addons:")
        print("1) Gems Rs.10")
        print("2) Nuts Rs.50")
        print("3) Waffle Rs.20")
        toppings=int(input("Enter your addon: "))
        if toppings==1:
            cost+=10
            print("total cost: Rs. ",cost)
        elif toppings==2:
            cost+=50
            print("total cost: Rs. ",cost)
        else:
            cost+=20
            print("total cost: Rs. ",cost)
    else:
            print("invalid options")
if order==3:
    print("French Twist😉")
    cost=179
    cc=int(input("do you want 1) cup or 2)cone: "))
    if cc==1:
            #print("cost for cone is Rs.199 ")
        cost+=10
        scoop=int(input("do you want double scoop if yes press 1 else 0: "))
        if scoop==1:
        #print("total cost: Rs. ",cost)
           print("total cost: Rs. ",cost)
           print("Addons:")
           print("1) Gems Rs.10")
           print("2) Nuts Rs.50")
           print("3) Waffle Rs.20")
            #addons=input("do you need any add ons y/n:")
           toppings=int(input("Enter your addon: "))
           if toppings==1:
              cost+=10
              print("total cost: Rs. ",cost)
           elif toppings==2:
              cost+=50
              print("total cost: Rs. ",cost)
           else:
              cost+=20
              print("total cost: Rs. ",cost)
        else:
            print("total cost: Rs. ",cost)
    elif cc==2:
        cost+=20
        print("total cost: Rs. ",cost)
        print("Addons:")
        print("1) Gems Rs.10")
        print("2) Nuts Rs.50")
        print("3) Waffle Rs.20")
        toppings=int(input("Enter your addon: "))
        if toppings==1:
            cost+=10
            print("total cost: Rs. ",cost)
        elif toppings==2:
            cost+=50
            print("total cost: Rs. ",cost)
        else:
            cost+=20
            print("total cost: Rs. ",cost)
    else:
            print("invalid options")
if order==4:
    print("Tiramisu😋")
    cost=183
    cc=int(input("do you want 1) cup or 2)cone: "))
    if cc==1:
            #print("cost for cone is Rs.199 ")
        cost+=10
        scoop=int(input("do you want double scoop if yes press 1 else 0: "))
        if scoop==1:
        #print("total cost: Rs. ",cost)
           print("total cost: Rs. ",cost)
           print("Addons:")
           print("1) Gems Rs.10")
           print("2) Nuts Rs.50")
           print("3) Waffle Rs.20")
            #addons=input("do you need any add ons y/n:")
           toppings=int(input("Enter your addon: "))
           if toppings==1:
              cost+=10
              print("total cost: Rs. ",cost)
           elif toppings==2:
              cost+=50
              print("total cost: Rs. ",cost)
           else:
              cost+=20
              print("total cost: Rs. ",cost)
        else:
            print("total cost: Rs. ",cost)
    elif cc==2:
        cost+=20
        print("total cost: Rs. ",cost)
        print("Addons:")
        print("1) Gems Rs.10")
        print("2) Nuts Rs.50")
        print("3) Waffle Rs.20")
        toppings=int(input("Enter your addon: "))
        if toppings==1:
            cost+=10
            print("total cost: Rs. ",cost)
        elif toppings==2:
            cost+=50
            print("total cost: Rs. ",cost)
        else:
            cost+=20
            print("total cost: Rs. ",cost)
    else:
            print("invalid options")
print("Thank you for coming...Visit us again❤️")