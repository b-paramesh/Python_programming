def applydiscount(price,dis_percent=0):
    return price*dis_percent/100

def add_gst(price,gst_percent=18):
    return price*gst_percent/100

def generate_invoice(cart,discount_percent=0,gst_percent=18):
    print("------Invoice-----")
    print("discount price:",discount_percent)
    print("gst after gst:",gst_percent)
    for i,j in cart.items():
        cart[i]=cart[i]-applydiscount(cart[i],20)+add_gst(cart[i])
    for i,j in cart.items():
        print("name:",i,"price:",j)
    print("Thank you for shoping")