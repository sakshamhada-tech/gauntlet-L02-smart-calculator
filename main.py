def bill_split(no_of_ppl, amt):
    tip_percent = 5
    tip_amt = amt * tip_percent/100
    total_amt = amt + tip_amt
    share_per_head = total_amt/no_of_ppl
    print(f"\nThe share of each person is ${share_per_head:.2f} including the tip. The tip ammount is ${tip_amt:.2f}.")

def km_to_miles(no_of_km):
    no_of_miles = no_of_km * 0.6213712
    print(f"\n{no_of_km}km is equal to {no_of_miles:.2f}mi.")

def c_to_f(c):
    f = c * (9/5) + 32
    print(f"\n{c} degree celcius is equal to {f} farenheit.")

def calc_bmi(height, weight):
    bmi = weight/(height**2)
    if bmi < 18.5:
        print(f"Your BMI is {bmi:.2f}, you are underweight. You should gain some weight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi:.2f}, you are normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {bmi:.2f}, you are overweight. You should lose some weight.")
    else:
        print(f"Your BMI is {bmi:.2f}, you are obese. You need to lose weight asap.")

while True:
    print("----------------------------------------------")
    print("1. Split Bill among your friends")
    print("2. Convert units (km to miles, celcius to farenheit)")
    print("3. Calculate your BMI")
    print("4. Exit")
    print("-----------------------------------------------")
    option = int(input("Please choose what do you want to do: "))

    if option == 1:
        print("\nCalculating the split of each person...\n")
        no_of_ppl = int(input("Enter the number of people: "))
        amt = float(input("Enter the bill ammount: "))
        bill_split(no_of_ppl, amt)
    elif option == 2:
        print("\nConverting units...\n")
        print("----------------------------------------------")
        print("1. Convert km to mi")
        print("2. Convert celcius to farenheit")
        print("3. Back")
        print("----------------------------------------------")
        unit_option = int(input("Choose what do you want to do: "))

        if unit_option == 1:
            no_of_km = float(input("\nEnter the no. of km: "))
            km_to_miles(no_of_km)
        elif unit_option == 2:
            c = float(input("\nEnter the temp in celcius: "))
            c_to_f(c)
        else:
            continue

    elif option == 3:
        print("\nConverting your BMI...\n")
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kg: "))

        calc_bmi(height, weight)
    elif option == 4:
        print("\nExiting the program...\n")
        break
    else:
        print("Please enter a number between 1 to 4!")
        continue



