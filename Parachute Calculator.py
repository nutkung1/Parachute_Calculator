import math
r = 1.229
Cansat_Weight = float(input("Cansat Weight(g) : "))
Kilo = float(Cansat_Weight/1000)
print(f"Cansat weight = {Kilo} Kilogram")
Velocity = float(input("Velocity : "))
Dg = float(input("Drag coefficient : "))
Parachute_Type = input("Choose your parachute type \n 1=basic 2=ring 3=ring diameter equal 10 : ")
Area = (float(2*Kilo*9.834565215))/(float(Dg*r*Velocity**2))
print(f"Parachute Area = {Area:.4f} m^2")
if Parachute_Type == "1":
    range_out = (math.sqrt(Area/math.pi))*100
    print(f"radius = {range_out:.2f} cm")
    sum=range_out*2
    print(f"diameter = {sum:.2f} cm")
    rope=sum*1.5
    print(f"Rope range = {rope:.0f} cm")
elif Parachute_Type == "2":
    range_out = (math.sqrt((Area/math.pi)+0.01))
    sum1=range_out*2*100
    print(f"diameter out = {sum1:.2f} cm")
    range_in = math.sqrt(range_out*range_out-(Area/math.pi))
    sum2 = range_in*2*100
    print(f"diameter in = {sum2:.2f} cm")
    rope = sum1*1.5
    print(f"Rope range = {rope:.0f} cm")
elif Parachute_Type == "3":
    range_in = 0.05
    sum2=range_in*100*2
    print("diameter_in = 10.00 cm")
    range_out=math.sqrt(range_in*range_in+(Area/math.pi))
    sum1=range_out*100*2
    print(f"diamter out = {sum1:.2f} cm")
    rope = sum1*1.5
    print(f"Rope range = {rope:.0f} cm")
else:
    print("Error")
Mass=Area*55+0.8
print(f"Parachute Mass = {Mass:.2f} g")
Rope_Mass = rope*14.4*0.01
print(f"Rope Mass = {Rope_Mass:.2f} g")
Sum_Mass = Mass+Rope_Mass
print(f"Approximately parachute weight = {Sum_Mass:.2f} g")
