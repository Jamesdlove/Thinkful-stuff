from bike import Wheel, Frame, Bike, BikeShop, Customer

# creates three different wheels
wheel1 = Wheel(10, 75, "amazing wheel") 
wheel2 = Wheel(20, 125, "dexlux wheel") 
wheel3 = Wheel(5, 20, "EL CHEAP-O") 

# creates three frame types
Alu = Frame(10, 50,"aluminum", "Alu Frame")
Carbon = Frame(2, 255, "carbon fiber", "Carbon Frame")
SS = Frame(15, 175,"stainless steel", "stainless Frame")

# creates six bikes that are made of wheels and frames
bike1 = Bike(wheel1, Alu, "bike1", "Triumph Bikes")
bike2 = Bike(wheel2, Carbon, "bike2", "Zelda Bikes")
bike3 = Bike(wheel3, SS, "bike3", "Triumph Bikes")
bike4 = Bike(wheel1, SS, "bike4", "Zelda Bikes")
bike5 = Bike(wheel2, Carbon, "bike5", "Triumph Bikes")
bike6 = Bike(wheel2, Alu, "bike6", "Zelda Bikes")

# a list of the bikes
bikes = [bike1, bike2, bike3, bike4, bike5, bike6]
sam = Customer("Sam", 400)
bill = Customer("Bill", 1000)

# creates a bike shop- with a three bike objects in it.
james_bike_shop = BikeShop("James's bicycle emporium", 1.2, [bike1, bike2, bike3])
james_bike_shop.print_inventory()
james_bike_shop.total_wholesale_cost()
james_bike_shop.print_costs()
james_bike_shop.print_affoardable_bikes(sam)
print "kawasaki"
print "sam money before", sam.money
james_bike_shop.buy_a_bike(sam, "bike1")
print "honda"
james_bike_shop.buy_a_bike(sam, "bike1")
print "sam money after", sam.money



anthonys_bike_shop = BikeShop("Anthony's racing bicyles", 1.25, [bike4, bike5, bike6])
anthonys_bike_shop.print_inventory()
anthonys_bike_shop.total_wholesale_cost()
anthonys_bike_shop.print_costs()
anthonys_bike_shop.print_affoardable_bikes(bill)
anthonys_bike_shop.buy_a_bike(bill,"bike5")


