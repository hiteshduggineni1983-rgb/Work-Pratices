# This function will be tested automatically. 
# Do not change the function name or parameter type.
def calculate_delivery_charge(distance: float) -> str:
    # Write your code below this line
    
 distance = float(input("enter  the user for delivery distance in Kilometers"))

 if distance <= 2:
    return "Delivery charge: 0"
 elif ditance <= 5:
     return "Delivery charge: 30"
 elif diatance <= 10:
     return "Delivery charge: 50"
 else:
      return "Delivery not available for your location."
      
      
      pass