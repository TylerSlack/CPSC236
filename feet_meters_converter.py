import math
def feet_to_meters():
    feet = float(input("Enter feet:"))
    meters = feet * 0.3048
    print(round(meters, 2), "Meters")
def meters_to_feet():
    meters = float(input("Enter meters:"))
    feet = meters / 0.3048
    print(round(feet, 2), "Feet")