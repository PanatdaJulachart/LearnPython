cost = 0
#size
while True :
    Ship_size = input("Enter spac size S M and L").upper()

    if Ship_size in ["S" ,"M", "L"] :
        print(f"Your spac size {Ship_size}")
        break
    else:
        print("Please enter again.")

#type
while True :
    print("Enter product type : 1 Normal ,2 Dangerous ,3 Contraband")
    Cargo_type = int(input("Please enter 1-3."))

    if Cargo_type in [1, 2, 3]:
        print(f"Your product type is {Cargo_type}")

        break
    else: 
        print("Please enter again.")

while True :
    print("Are you VIP")
    Is_vip = input("Enter Y/N").upper()
    
    if Is_vip in ["Y", "N"] :
        print("Saved.")
        break
    else :
        print("Please enter again.")

if Is_vip == "Y":
    Is_vip = True
if Is_vip == "N":
    Is_vip = False

#zone
if Cargo_type == 3 :
    print("Arrested!")
elif Cargo_type == 2 :
    if Ship_size == "L" :
        print("Access denied : Danger level too high")
    else :
        print("Isolated zone")
else :
    if Is_vip == True:
        print("VIP Lounge")
    else:
        if Ship_size == "S":
            print("Zone A")
        elif Ship_size == "M":
            print("Zone B")
        else:
            print("zone C")

#cost
if cost == 0 :
    if Ship_size == "S" :
        cost = cost + 500
    elif Ship_size == "M" :
        cost = cost + 1500
    else : 
        cost = cost + 5000

if Cargo_type == 2:
    cost = cost * 1.50

Distance_tax = int(input("Enter the speed of light years."))

if Distance_tax >= 1000:
    cost = cost + 1000

if Is_vip == True:
    cost = cost - (cost * 0.20)

print (f"Your parking fee is: {cost}")

    

        

