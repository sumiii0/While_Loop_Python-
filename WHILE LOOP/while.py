#FIRST SUGGESTION:
print("Car Suggestion System")
print("=====================")

valid_size = ['small', 'large']
valid_act = ['slow', 'fast']
valid_color = ['grey', 'black']
valid_seat = ['2 seater', '4 seater']

while True:
    size = input(
        "Enter the size of the car you want (small/large):").strip().lower()
    color = input(
        "Enter the color of the car (grey/black):").strip().lower()
    seat = input("Enter the seating capacity (2 seater/4 seater):").strip().lower()
    act = input(
        "Enter the activity of the car (slow/fast):").strip().lower()

    if (
        size in valid_size and
        color in valid_color and
        seat in valid_seat and
        act in valid_act):
        if (
            size == "small" and
            act == "slow" and
            color == "grey" and
            seat == "2 seater"):
            print("A Porsche for you!")
        elif (
            size == "large" and
            act == "fast" and
            color == "black" and
            seat == "4 seater"):
            print("A BMW for you!")
        elif ( 
            size == "small" and
            act == "fast" and 
            color == "grey" and 
            seat == "4 seater"):
            print("A Rolls Royce for you!")
        elif ( 
            size == "large" and
            act == "slow" and 
            color == "black" and 
            seat == "2 seater"):
            print("A Mercedes for you!")
        elif ( 
            size == "large" and
            act == "fast" and 
            color == "grey" and 
            seat == "4 seater"):
            print("A Toyota for you!")
        elif ( 
            size == "small" and
            act == "slow" and 
            color == "grey" and 
            seat == "4 seater"):
            print("A Corolla for you!")
            
        else:
            print("Sorry, no suggestions available for this combination.")
    else:
        print("Invalid input, please try again!")

    rerun = input(
        "Are you satisfied with the suggestion? (y/n): ").strip().lower()
    if rerun == "y":
        print("Thank you!")
        break
    else:
        print("Okay, let's try again!")
        continue

#SECOND SUGGESTION:
print("Travel destination suggestion system")
print("===================================")

while True:
    budget = input(
        "What is your budget? (Low/Medium/High): "
    ).strip().lower()

    if budget == "low":
        activity = input(
            "Do you prefer Nature or History? "
        ).strip().lower()
        if activity == "nature":
            print(
                "How about visiting the Northern Areas of Pakistan or "
                "a nearby hill station?"
            )
        elif activity == "history":
            print(
                "Visit Lahore for its rich historical sites "
                "like Badshahi Mosque."
            )
        else:
            print("Sorry, no suggestions available for this preference.")
    elif budget == "medium":
        print("Consider a trip to Hunza Valley or Skardu.")
    elif budget == "high":
        print(
            "You can travel to Europe or explore exotic beaches "
            "in the Maldives."
        )
    else:
        print("Invalid input, please try again!")

    response = input(
        "Want another suggestion? (yes/no): "
    ).strip().lower()
    if response != "yes":
        print("Safe travels!")
        break
    else:
        print("Okay, let's try again!")
        continue


#THIRD SUGGESTION:
print("Movie suggestion")
print("================")

while True:
    which_type = input(
        "Which type of movie do you wanna watch? (Romantic/Historical/Horror): "
    ).strip().lower()

    if which_type == "horror":
        activity = input(
            "Do you prefer Zombies or Conjuring? "
        ).strip().lower()
        if activity == "zombies":
            print(
                "How about watching the 'ALL OF US ARE DEAD'?"
            )
        elif activity == "conjuring":
            print(
                "How about watching the 'THE CONJURING'?"
            )
        else:
            print("Sorry, no suggestions available for this preference.")
    elif which_type  == "historical":
        print("Consider a Book 'THE DEVIL IN THE WHITE CITY'.")
    elif which_type == "romantic":
        print(
            "You can watch BLUE VALENTINE, 365 DAYS or FIFTY SHADES OF GREY."
        )
    else:
        print("Invalid input, please try again!")

    response = input(
        "Want another suggestion? (yes/no): "
    ).strip().lower()
    if response != "yes":
        print("Enjoy Movie!")
        break
    else:
        print("Okay, let's try again!")
        continue

#FOURTH SUGGESTION:
print("Book suggestion")
print("================")

while True:
    which_type = input(
        "What is your interest? (Romantic/Historical/Horror): "
    ).strip().lower()

    if which_type == "romantic":
        activity = input(
            "Do you prefer romantic fantasy or new adult romance? "
        ).strip().lower()
        if activity == "romantic fantasy":
            print(
                "How about reading the 'FOURTH WINGS or IRON FLAME'?"
            )
        elif activity == "new adult romance":
            print(
                "How about reading the 'LOVE UNWRITTEN or WILD LOVE'?"
            )
        else:
            print("Sorry, no suggestions available for this preference.")
    elif which_type  == "historical":
        print("Consider a Book 'THE DEVIL IN THE WHITE CITY'.")
    elif which_type == "horror":
        print(
            "You can read 'THE RUINS or GHOST STORY'"
        )
    else:
        print("Invalid input, please try again!")

    response = input(
        "Want another suggestion? (yes/no): "
    ).strip().lower()
    if response != "yes":
        print("Have a great time!")
        break
    else:
        print("Okay, let's try again!")
        continue

#FIFTH SUGGESTION:
print("Music Playlist suggestion")
print("=========================")

while True:
    which_type = input(
        "What is your interest? (Pop/Sad/Hip Hop): "
    ).strip().lower()

    if which_type == "sad":
        activity = input(
            "Do you prefer sad or lof? "
        ).strip().lower()
        if activity == "sad":
            print(
                "How about listening the 'AGAR TUM SAATH HO or HAMARI ADHURI KAHANI'"
            )
        elif activity == "lofi":
            print(
                "How about listening the 'RANJHAAN or VE KAMLEYAA'"
            )
        else:
            print("Sorry, no suggestions available for this preference.")
    elif which_type  == "hip hop":
        print("You can listen 'Heartless by KANYE WEST, FALL BACK by LITHEE or Die trying by key glock'")
    elif which_type == "pop":
        print(
            "You can listen 'Justin Bieber, Falling from daniel trevor, Middle of the night by ELLE DUHE or Unforgettable'"
        )
    else:
        print("Invalid input, please try again!")

    response = input(
        "Want another suggestion? (yes/no): "
    ).strip().lower()
    if response != "yes":
        print("Have fun!")
        break
    else:
        print("Okay, let's try again!")
        continue