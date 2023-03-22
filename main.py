(0C*9/5)+32=32F

while true:
	menu = int(input("1) farenheit to celcius  2) celcius to farenheit  3) exit : "))

	if menu == "1":
		farenheit = float(input('Enter temperature on Farenheit : '))
		celsius = (farenheit -32.0) * (5.0/9.0)
		print(f"{farenheit:.2f} degrees Farenheit is {celsius:.2f} degrees Cesius.")
	elif menu == "2":
		celsius = float(input("Enter teperature in Celsius : "))
		farenheit = (celsius * 5.0/9/0) + 32.0
		print(f"{celsius:.2f} degrees Celsius is {farenheit:.2f} degrees Farenheit.")
	elif menu == "3":
		break # exit(1)
	else:
		print("Please choose from the given menu.")

print("Program finished!")