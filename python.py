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

#hotel ,plane and car costs
"""def hotel_cost(days):
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
    if askcity == "Chicago" or askcity == "London" or askcity == "Tokyo" or askcity == "Toronto":
        askdays = int(input("How many days would you like to stay?"))
        hotelcost = hotel_cost(askdays)
        planecost = plane_cost(askcity)
        carcost = car_cost(askdays)
        total = hotelcost + planecost + carcost
        return(total)
    else:
        print ("please enter a valid city")
        total_cost()
total_cost()"""


"""numbers = [1,2,3,4,5,6,7,8,9,10]

numbers[8] = 21

numbers.append(123456789)"""

"""letters = [ "a","b","c","d","e","f"]

sliced_list = letters[2:5]
print (sliced_list)
print (letters)"""

"""aminals = ["ant","bat","cat","dog"]
print (aminals.index("cat"))


aminals.insert(1,"snake")
print (aminals)

aminals.pop(2)# gets rid of item using inedx number
print (aminals)

aminals.remove("dog")
print (aminals)

aminals.sort()
print (aminals)"""


numbers = [1,2,3,4,5,6,7,8,9]
def print_first(lists):
    return(lists[0])









