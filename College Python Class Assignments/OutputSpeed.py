"""
Using variables write a script that defines a distance of 60 miles and a completion time of 3 hours.
The output should show a completion speed in miles per hour, knots, and feet per second.
"""
distance_in_miles = 60
time_in_hours = 3

distance_in_knots = distance_in_miles / 1.15078
distance_in_feet = distance_in_miles * 5280

time_in_seconds = time_in_hours * 3600

#dis / time = speed 


print(f"The speed in knots is: {distance_in_knots / time_in_hours}")
print(f"The speed in miles per hour is: {distance_in_miles / time_in_hours} ")
print(f"The speed in feet per second is: {distance_in_feet / time_in_seconds} ")
