#  pizza - program
print("🍕 Welcome to Python Pizza Deliveries!")

# Get inputs and make them lowercase for easier checking
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0

# Validate pizza size
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("⚠️ Invalid pizza size. Please choose S, M, or L.")
    exit() 

# Add pepperoni price
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
elif pepperoni != "N":  
    print("⚠️ Invalid input for pepperoni. Please type Y or N.")
    exit()

# Add cheese price
if extra_cheese == "Y":
    bill += 1
elif extra_cheese != "N": 
    print("⚠️ Invalid input for cheese. Please type Y or N.")
    exit()

# Final result
print(f"✅ Your final bill is ${bill}")

