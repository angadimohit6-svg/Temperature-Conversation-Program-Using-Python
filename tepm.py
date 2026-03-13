unit = input("Is this temperature in Celsius or in Farenheit (C/F): ")
temp = float(input("What is the Temperature:"))

if unit == "C":
    temp = round((temp* 9/5) + 32, 3)
    print(f"The temperature in Farenheit is: {temp} °F")
    
elif unit == "F":
    temp = round((temp - 32) * 5/9, 3)
    print(f"The temperature in Celcius is: {temp} °C")
    
else:
    print(f"{unit} is not a valid unit of temperature.Please enter valid unit of temperature (C/F). ")