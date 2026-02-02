#BAG CHECKING & BOARDING PASS GENERATOR AT THE AIRPORT
import sys
import random
from datetime import datetime, timedelta     

banned_stuff = ['weapon', 'gun', 'bomb', 'explosive', 'knife', 'blade',
                'drugs', 'acid', 'lighter fluid', 'grenade', 'sword', 'firearm']

risky_stuff = ['scissors', 'hammer', 'screwdriver', 'lighter', 'power bank',
               'drill', 'wrench', 'pliers']
 
countries = {
    'USA': 'US',
    'UK': 'UK',
    'INDIA': 'IN',
    'CANADA': 'CA',
    'AUSTRALIA': 'AU',
    'FRANCE': 'FR',
    'GERMANY': 'DE',
    'JAPAN': 'JP',
    'CHINA': 'CN',
    'DUBAI': 'AE',
    'SINGAPORE': 'SG'
}

airlines = ['Emirates', 'Delta', 'Air India', 'British Airways', 'Lufthansa',
            'Singapore Airlines', 'Qantas']

print("=======================================================")
print("         WELCOME TO INTERNATIONAL AIRPORT")
print("              Baggage Security Check")
print("=======================================================")

print("\nHello! Let's start with some basic information.")
name = input("enter your name to proceed: ")
if not name:
    print("Come on, I need your name to proceed!")
    sys.exit()

print(f"\nNice to meet you, {name}!")

print("\n-------------------------------------------------------")
print("Do you have any baggage with you?")

try:
    has_bag = input("Do you have bag (yes/no): ").lower()

    if has_bag not in ["yes", "no"]:
        raise ValueError("wrong input, Please type yes or no.")

    if has_bag == "yes":
        print("great, proceed ahead")
    else:
        print("you can move ahead")

except ValueError as e:
    print("Error:", e)
    sys.exit()

print("\n-------------------------------------------------------")
print("Where are you flying to today?")
print("We fly to these countries:")
for country in countries.keys():
    print(f"  • {country}")

destination = input("\nType your destination: ").upper().strip()

if destination not in countries:
    print(f"\nOops! We don't have flights to {destination} right now.")
    print("Please choose from the list above.")
    sys.exit()

code = countries[destination]
print(f"\nGreat choice! {destination} it is.")

# Initialize items_list early
items_list = []

# Only ask about bag type if they have baggage
if has_bag == "yes":
    bag_type = input("Is it just a small handbag/purse? (yes/no): ").lower().strip()

    if bag_type not in ["yes", "no"]:
        print("Error: Wrong input. Please type yes or no.")
        print("Please try again.\n")
        bag_type = input("Is it just a small handbag/purse? (yes/no): ").lower().strip()

    if bag_type == 'yes' or bag_type == 'y':
        print("\n✓ Small handbag noted!")
        print("Please place it in the scanner and collect it after.")
        print("You're good to go!")
        items_list = ['handbag']
    else:
        print("\n-------------------------------------------------------")
        print("Now, what do you have in your baggage?")
        print("-------------------------------------------------------")
        print("Just list everything separated by commas.")
        print("For example: clothes, laptop, phone, charger, books, shoes")

        bag_items = input("\nWhat's in your bag: ").strip()
        if not bag_items:
            print("\nYou need to declare what's in your bag!")
            print("Security rules, you know.")
            sys.exit()

        items_list = [item.strip().lower() for item in bag_items.split(',')]

        print(f"\nOkay, let me check these {len(items_list)} items...")

        found_banned = []
        found_risky = []

        for item in items_list:
            for ban in banned_stuff:
                if ban in item:
                    found_banned.append(item)
                    break

            for risk in risky_stuff:
                if risk in item:
                    found_risky.append(item)
                    break

        if found_banned:
            print("\n=======================================================")
            print("           SECURITY ALERT!")
            print("=======================================================")
            print(f"\nWait, you have: {', '.join(found_banned)}")
            print("\nI'm sorry, but these items are strictly prohibited!")
            print("You cannot bring them on the flight.")
            print("Security will need to confiscate them.")
            sys.exit()

        if found_risky:
            print(f"\nHold on! You have: {', '.join(found_risky)}")
            print("These can't go in your carry-on bag.")
            answer = input("Can you put them in checked baggage instead? (yes/no): ").lower()

            if answer != 'yes' and answer != 'y':
                print("\nThen I'm afraid you'll have to leave them behind.")
                print("Can't let you through security with those.")
                sys.exit()
            else:
                print("Perfect! We'll move those to checked baggage.")

        print("\n-------------------------------------------------------")
        print("Let's check your baggage weight.")
        print("-------------------------------------------------------")

        try:
            weight = float(input("How heavy is your bag? (in kg): "))

            if destination == 'INDIA':
                weight_limit = 15.0
            else:
                weight_limit = 20.0

            if weight > weight_limit:
                extra = weight - weight_limit

                if destination == 'INDIA':
                    fee_per_kg = 550
                    fee = extra * fee_per_kg
                    print(f"\nUh oh! Your bag is {extra:.1f} kg over the limit.")
                    print(f"Domestic excess baggage: ₹{fee_per_kg}/kg")
                    print(f"Total extra charge: ₹{fee:.2f}")
                    pay = input("Do you want to pay the fee? (yes/no): ").lower()

                    if pay != 'yes' and pay != 'y':
                        print("\nYou'll need to remove some items then.")
                        sys.exit()
                    else:
                        print(f"Alright, ₹{fee:.2f} added to your bill.")
                else:
                    fee_per_kg = 100
                    fee = extra * fee_per_kg
                    print(f"\nUh oh! Your bag is {extra:.1f} kg over the limit.")
                    print(f"International excess baggage: ${fee_per_kg}/kg")
                    print(f"Total extra charge: ${fee:.2f}")
                    pay = input("Do you want to pay the fee? (yes/no): ").lower()

                    if pay != 'yes' and pay != 'y':
                        print("\nYou'll need to remove some items then.")
                        sys.exit()
                    else:
                        print(f"Alright, ${fee:.2f} added to your bill.")
            else:
                print(f"Perfect! {weight} kg is within the limit.")

        except ValueError:
            print("\nThat doesn't look like a valid weight!")
            print("Let's just say it's fine for now.")
else:
    print("\n=======================================================")
    print("           NO BAGGAGE - QUICK PASS!")
    print("=======================================================")
    print("\nLucky you! No baggage to check.")

# Liquids check
print("\n-------------------------------------------------------")
print("Quick question about liquids...")
print("-------------------------------------------------------")

try:
    has_liquids = input("Do you have any liquids? (yes/no): ").lower()

    if has_liquids not in ["yes", "no"]:
        raise ValueError("wrong input, Please type yes or no.")

    if has_liquids == 'yes' or has_liquids == 'y':
        print("\nRemember: Liquids must be under 100ml each")
        print("And all must fit in one small plastic bag.")
        confirm = input("Is yours compliant? (yes/no): ").lower()

        if confirm != 'yes' and confirm != 'y':
            print("\nPlease remove excess liquids at the security bin.")
            print("You can buy drinks after security!")
            sys.exit()

    if has_liquids == "yes":
        print("great, proceed ahead")
    else:
        print("you can move ahead")

except ValueError as e:
    print("Error:", e)
    sys.exit()

print("\n=======================================================")
print("            ALL CHECKS PASSED!")
print("=======================================================")
print("\nGreat! Everything looks good.")
print("Let me generate your boarding pass...")

aline = random.choice(airlines)
flight = f"{code}{random.randint(100, 999)}"
booking = ''.join(random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ123456789', k=6))

now = datetime.now()
departure = now + timedelta(hours=random.randint(2, 5), minutes=random.randint(0, 59))
trip_time = random.randint(5, 14)
arrival = departure + timedelta(hours=trip_time)

gate = f"{random.choice('ABCDEFG')}{random.randint(1, 25)}"
seat = f"{random.randint(1, 35)}{random.choice('ABCDEF')}"
terminal = random.choice(['1', '2', '3'])

print("\n=======================================================")
print("              YOUR BOARDING PASS")
print("=======================================================")
print(f"""
    Passenger Name       : {name.upper()}
    Booking Reference    : {booking}

    Airline              : {aline}
    Flight Number        : {flight}
    Destination          : {destination}

    Departure Time       : {departure.strftime('%I:%M %p')}
    Departure Date       : {departure.strftime('%d / %m / %Y')}

    Arrival Time         : {arrival.strftime('%I:%M %p')}
    Arrival Date         : {arrival.strftime('%d / %m / %Y')}

    Flight Duration      : {trip_time} hours

    Terminal             : {terminal}
    Boarding Gate        : {gate}
    Seat Number          : {seat}

    Items in Baggage     : {len(items_list) if items_list else 'No baggage'}
""")
print("=======================================================")

print("\nImportant reminders:")
print("  • Be at the gate 30 minutes before departure")
print("  • Keep your ID and boarding pass handy")
print("  • Boarding starts 45 minutes before departure")

print("\n=======================================================")
print("     Have an amazing flight! Safe travels!")
print("=======================================================")
print("\nThank you for flying with us!")
