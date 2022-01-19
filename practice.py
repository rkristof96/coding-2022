def convert_feet_to_meters(distance_feet):
    # print(distance)
    return 0.3048*distance_feet
    
def convert_inches_to_feet(distance_inches):
    return distance_inches /12.0


def convert_inches_to_meters(distance_inches):
    # distance_feet=convert_inches_to_feet(distance_inches)
    # distance_meter = convert_feet_to_meters(distance_feet)
    distance_meter= convert_feet_to_meters(convert_inches_to_feet(distance_inches))
    return distance_meter


print('I am here.')
distance_meter=10.0
print(distance_meter)
distance=convert_feet_to_meters(200.0)
print('Distance is', distance, 'meters')
print('Now I am done.')    


print('1000 inches in meters are', convert_feet_to_meters(convert_inches_to_feet(1000.0)))
print('1000 inches in meters are', convert_inches_to_meters(1000.0))
