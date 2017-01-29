cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Basic instructions from LPtHW
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "Therre will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drill 1! Testing out the == function
#print "Does the number of drivers of equal the number of passengers?"
#print passengers == drivers, "the number of drivers does not equal the number of passengers"

# Study Drill 2! Testing out the "%" function as a way to insert any text
#print "Hey %s there." % "you"
#print "Mother%s!" % "[insert explative here]"