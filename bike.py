# sets up the class of wheels
class Wheel(object):
    """docstring for Wheel"""
    def __init__(self, weight, price, name):
        self.weight = weight
        self.price = price
        self.name = name

#sets up the class of frames
class Frame(object):
    """docstring for Frame"""
    def __init__(self, weight, price, material, name):
        self.weight = weight
        self.price = price
        self.material = material
        self.name = name
    def __repr__(self):
        return "Type: {}".format(self.name)


# sets the class of bikes (wheels plus frame), plus calculates the cost and weight of the bikes
class Bike(object):
    """bike made up of frame and wheels"""
    def __init__(self, wheel, frame, name, manufacturer):
        self.name = name
        self.frame = frame
        self.wheel = wheel
        self.manufacturer = manufacturer
    def __repr__(self):
        return "Bike Name: {}; {}; Frame weight: {}kg; Cost: ${}".format(self.name, self.frame, self.wgt(), self.cost())
    def wgt(self):
        return (2 * self.wheel.weight + self.frame.weight)
    def cost(self):
        return (2 * self.wheel.price + self.frame.price)

#creates the customer class
class Customer(object):
    """he who buys the bikes"""
    Purchased_bike_count = 0
    def __init__(self, name, money):
        self.name = name
        self.money = money


# sets up the class of bike shops
class BikeShop(object):
    """where Customer buy the bikes, gets bikes from manufacturer"""
    def __init__(self, name, profit_margin, inventory):
        self.name = name
        self.profit_margin = profit_margin
        self.inventory = inventory 
    def total_wholesale_cost(self):
        total_cost = 0
        for bike in self.inventory:
            total_cost += bike.cost()
        print "Total Cost of Bikes in {}:${}".format(self.name, total_cost)
    def print_weights(self):
        for bike in self.inventory:
            print bike.wgt()
    def print_costs(self):
        for bike in self.inventory:
            print "Retail Price {}:${}".format(bike.name,(bike.cost() * self.profit_margin))
    def print_affoardable_bikes(self, customer):
        affoardable_bikes = []
        for bike in self.inventory:
            if (bike.cost() * self.profit_margin) <= customer.money:
                affoardable_bikes.append(bike.name)
        print "{}, You can buy:{}".format(customer.name, affoardable_bikes)
    def print_inventory(self):
        print "{} Inventory: {}".format(self.name, self.inventory)
    def buy_a_bike(self, customer, bike_name):
        bike = None
        for b in self.inventory:
            if bike_name == b.name:
                bike = b
        if bike == None:
            print "sorry we don't have that bike"
        else:
            money_remaining = customer.money - (bike.cost() * self.profit_margin)
            print "{}, you purchased {}: you have ${} left".format(customer.name, bike.name, money_remaining)
            print "{} made ${} profit".format(self.name, ((bike.cost() * self.profit_margin)-bike.cost()))
            sold_bike = bike.name
            remaining_bikes = [] 
            for bike in self.inventory:
                if sold_bike != bike.name:
                    remaining_bikes.append(bike)
            self.inventory = remaining_bikes
            print "{} still has these bikes in stock:{}".format(self.name, remaining_bikes)
            #customer.money = money_remaining
            customer.money -= bike.cost() * self.profit_margin
