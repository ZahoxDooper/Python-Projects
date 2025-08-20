def c_to_f(celsius):
  return celsius * 9/5 + 32

def calculate_stats(temperatures):
  maximum = max(temperatures)
  minimum = min(temperatures)
  average = sum(temperatures) / len(temperatures)
  return maximum, minimum, average

# Get user input
input_str = input("Enter temperatures in Celsius (comma separated): ")
celsius_list = [float(temp.strip()) for temp in input_str.split(",")]
fahrenheit_list = [c_to_f(temp) for temp in celsius_list]

# This is taking for ever
print("\nTemperature Summary:")
print("Celsius   Fahrenheit")
for c, f in zip(celsius_list, fahrenheit_list):
  print(f"{c:<10} {f:.2f}")

# I am hungry
max_c, min_c, avg_c = calculate_stats(celsius_list)
max_f, min_f, avg_f = calculate_stats(fahrenheit_list)

print(f"\nMax: {max_c}°C / {max_f:.2f}°F")
print(f"Min: {min_c}°C / {min_f:.2f}°F")
print(f"Average: {avg_c:.2f}°C / {avg_f:.2f}°F")


  

  
