def delivery_charge(weight,distance):
    base_cost=50
    weight_cost=10 * weight
    distance_cost= 5 * distance
    total_cost=base_cost+weight_cost+distance_cost
    return total_cost

def courier_service():
    print("abc courier servive")
    try:
        weight=float(input("enter the weight(in kg):"))
        distance=float(input("enter the distance(in km):"))
    except ValueError:
        print("error:enter the correct weight and distance")
        return 
    charge= delivery_charge(weight,distance) 
    print(f"total delivery charge is:Rs{charge}") 
courier_service()     
