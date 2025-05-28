# cashier at a supermarket

def enter_products():  # function-1
# here we got the cashier to input all the products bought one by one
# we stored all that info in a dictionary called "buying_data" and returned it back
    buying_data = {}
    enter_details = True
    while enter_details:
        details = input("press A to add product and Q to quit :")
        if details == "A":
          product = input("enter product :")
          quantity = int(input("enter quantity :"))
          buying_data.update({product : quantity})
        elif details =="Q":
           enter_details = False
        else :
           print("please select a correct option")
    return buying_data

def get_price(product,quantity):   # function-2
# the job of this function is to give the subtotal of a single product as per its price and quantity mentioned
   price_data = {
      "biscuit": 3,
      "chicken":5,
      "egg":1,
      "fish":3,
      "coke":2,
      "bread":2,
      "apple":3,
      "onion":3,
   }
   subtotal = price_data[product]*quantity
   print(product+"$"+str(price_data[product])+"x"+str(quantity)+"="+str(subtotal))
   return subtotal

def get_discount(billamount,membership): # function-3
# here,as per the total bill amount we decide the discount is applicable or not 
   discount = 0
   if billamount >= 25:
      if membership == "gold":
         billamount = billamount*0.80
         discount = 20
      elif membership == "silver":
         billamount = billamount*0.90
         discount = 10
      elif membership == "bronze":
         billamount = billamount*0.95
         discount = 5
      print(str(discount)+"% off for "+membership+""+" membership on total amount :$"+str(billamount))
   else:
      print("no discount on amount less than 25$")
   return billamount

def make_bill(buying_data,membership):   # function-4
# loop starts : call function-2 until subtotal is added for all products within buying data
# loop ends
# call function-3 to calculate discounted amount
# this is the main part of the program which is not inside of any function
# the first line of execution of code will start from here....
   billamount = 0
   for key,value in buying_data.items():
      billamount += get_price(key,value)
   billamount = get_discount(billamount,membership)
   print("the discounted amount is $",str(billamount)) 

buying_data =   enter_products()   # makes call to the function-1
membership = input("enter customer membership :")
make_bill(buying_data,membership)   # makes a call to function-4
