cars = 100 # define cars number
space_in_a_car = 4.0 #defne _ car number = 4.0 and 4 is ok too.
drivers = 30 #define drivers number
passengers = 90 #define passengers number
cars_not_drivers = cars - drivers # define cars not drivers
cars_driven = drivers  #define cars_driven
carpool_capacity = cars_driven * space_in_a_car  #define carpool_capacity
average_passengers_per_car = passengers / cars_driven #define average_passengers_per_car


print "there are" , cars, "cars available."
print "there are only", drivers,"drivers available."
print "there will be" , cars_not_drivers,"empty cars today."
print "we can transport",carpool_capacity,"people today."
print "we have", passengers,"to carpool today."
print "we need to put about" ,average_passengers_per_car,"in each car."
