T = float(input("please enter the temperature of the tea"))
T_a= float(input("please enter the ambient air temperature:"))
k = 0.055
rateofcooling = -k * (T - T_a)
print("The rate of cooling is", rateofcooling, "degrees per minute")
