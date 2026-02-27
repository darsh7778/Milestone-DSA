def trafficlight(color):
   value = color
                            
   if value.lower() == "red":
       print("stop...")
   elif value.lower() == "green":
       print("Go...")
   elif value.lower() == "yellow":
       print("Wait..")
   else:
       print("invalid input")
    
trafficlight("Red")