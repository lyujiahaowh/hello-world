# Write a program which prompts the user for a Celsius temperature
# convert the temperature to Fahrenheit
# and print out the converted temperature.

cTemp = input("Enter Celsius:")
fTemp = float(cTemp) * 9/5 + 32
print("Fahrenheit:", fTemp, type(fTemp))