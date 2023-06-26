#Kurir_Internasional
#Fa'iq Ali Sutiono
#1152100040

def country():
    country = input('Country: ')


    if country ==  "USA":
      USA()
    elif country == "Canada":
      Canada()
    else: 
      print("We don't ship there yet")
      question()

def USA():
    Q = int(input("Quantity: "))
    if Q <= 50:
        cost = 6.25
    elif Q <= 100:
        cost =  9.50
    elif Q <= 150:
        cost = 12.75
    else:
        cost = 15.00
    line()
    print("Cost: ",cost)
    question()

def Canada():
    Q = int(input("Quantity: "))
    if Q <= 50:
        cost = 8.25
    elif Q <= 100:
        cost = 12.50
    elif Q <= 150:
        cost = 18.75
    else: 
        cost = 25.00
    line()
    print("Cost: ",cost)
    question()


def question():
    ask = input("Anything Else? (Y/N) ")
    if ask == "Y":
        line2()
        country()
        
    else:
        print("Thank You")

def line():
    print("=======================")
def line2():
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    
    
country()





    

    