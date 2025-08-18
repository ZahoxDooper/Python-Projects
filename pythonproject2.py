print("Welcome to the Unit Converter!")
print("Options: 1) Celsius to Fahrenheit  2) Meters to Kilometers")
choice = input("Enter your choice (1/2): ")
#Python is a decent langauge الحمدلله 
if choice == "1":
    c = float(input("Celsius: "))
    f = (c * 9/5) + 32
    print(c, "C =", f, "F")
elif choice == "2":
    m = float(input("Meters: "))
    km = m / 1000
    print(m, "meters =", km, "kilometers")
else:
    print("Invalid choice")