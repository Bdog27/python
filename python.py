"""def square(x):
    return x**2"""
"""def five(x) :
    return x + 5
def three(y):
    return five(y) - 3"""

"""def cube(x):
    return x**3
def three(x):
    if x%3 == 0:
        return cube(x)
    else:
        return False"""
"""maximum = max(3,43,54,7,9)
print (maximum)
    
minimum = min(17,43,55,56)
print (minimum)
absolute = abs(-554)
print (absolute)
print (type("alex"))"""


def hotel_cost(days):
    return days*150

def plane_cost(city):
    if city == "Chicago":
        return 183
    elif city == "London":
        return 222
    elif city == "Toronto":
        return 220
    elif city == "Tokyo":
        return 475

def car_cost(days):
    price=150*days
    if days >= 7:
        return price - 50 
    elif days >= 3:
        return price - 20
    else:
        return price

def total_cost():
    askcity = input("what city would you like to stay in")
    askdays = int(input("How many days would you like to stay?"))
    hotelcost = hotel_cost(askdays)
    planecost = plane_cost(askcity)
    carcost = car_cost(askdays)
    total = hotelcost + planecost + carcost
    return(total)
