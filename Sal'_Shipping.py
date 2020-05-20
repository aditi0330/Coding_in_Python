def ground_shipping(weight):
  if weight <= 2:
    return 20+1.50*weight
  elif 2<weight<=6:
    return 20+3.0*weight
  elif 6<weight<=10:
    return 20+4*weight
  else:
    return 20+4.75*weight

print(ground_shipping(8.4))
premium_ground_shipping = 125.0
def drone_shipping(weight):
  if weight<2:
    return weight*4.50
  elif 2<weight<=6:
    return weight*9.00
  elif 6<weight<=10:
    return weight*12.00
  else:
    return weight*14.25

print(drone_shipping(1.5))

def cheapest_method(weight):
  one = ground_shipping(weight)
  two = drone_shipping(weight)
  print(min(one,min(two, 125.0)))

print(cheapest_method(17))
