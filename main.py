# TREASURE ISLAND

print("""
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|""")

print("Welcome to The Treasure Island.")
print("Your mission is to find the Treasure")
print("You're at a cross road.where do you want to go?")
choice_1 = input('      Type "left" or "right ').lower()
if choice_1 == "right":
    print("Fall into a Hole")
    print("""
      ____                         ___                
     / ___| __ _ _ __ ___   ___    / _ \__   _____ _ __ 
    | |  _ / _` | '_ ` _ \ / _ \  | | | \ \ / / _ \ '__|
    | |_| | (_| | | | | | |  __/  | |_| |\ V /  __/ |   
     \____|\__,_|_| |_| |_|\___|   \___/  \_/ \___|_|   """)

else:
    print("You've come to a lake.There is an island in the middle of the lake.")
    choice_2 = input('   Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if choice_2 == "swim":
        print("Attacked by trout.")
        print("""
          ____                         ___                
         / ___| __ _ _ __ ___   ___    / _ \__   _____ _ __ 
        | |  _ / _` | '_ ` _ \ / _ \  | | | \ \ / / _ \ '__|
        | |_| | (_| | | | | | |  __/  | |_| |\ V /  __/ |   
         \____|\__,_|_| |_| |_|\___|   \___/  \_/ \___|_|   """)

    else:
        print("You arrive at the island unharmed.There is a house with 3 doors.")
        choice_3 = input('One red, one yellow and one blue. Which colour do you choose?').lower()
        if choice_3 == 'red':
            print("Burned By Fire.")
            print("""
              ____                         ___                
             / ___| __ _ _ __ ___   ___    / _ \__   _____ _ __ 
            | |  _ / _` | '_ ` _ \ / _ \  | | | \ \ / / _ \ '__|
            | |_| | (_| | | | | | |  __/  | |_| |\ V /  __/ |   
             \____|\__,_|_| |_| |_|\___|   \___/  \_/ \___|_|  """)

        elif choice_3 == 'blue':
            print("Eaten by Beasts.")
            print("""
              ____                         ___                
             / ___| __ _ _ __ ___   ___    / _ \__   _____ _ __ 
            | |  _ / _` | '_ ` _ \ / _ \  | | | \ \ / / _ \ '__|
            | |_| | (_| | | | | | |  __/  | |_| |\ V /  __/ |   
             \____|\__,_|_| |_| |_|\___|   \___/  \_/ \___|_|   """)

        else:
            print("YOU WIN!!")
