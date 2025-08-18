print("Welcome to the Ohm's law calculator! ")
print("What do you want to calculate?")
print("V = Voltage" , "I = Current" , "R = Resistance")
choice = input("Enter your choice (V/I/R) :")
if choice == "V":
    I = float(input("Current(I) : "))
    R = float(input("Resistance(R) : "))
    print("V =" , I * R , "Volts")
elif choice == "I":
    V = float(input("Voltage(V) : "))
    R = float(input("Resistance(R) : "))
    print("I =" , V / R , "Amps")
elif choice == "R":
    V = float(input("Voltage(V) : "))
    I = float(input("Current(I) : "))
    print("R =" , V / R , "Ohms")
    
    
    
              
    
    


    

    
    
    

            




                      

           
           





