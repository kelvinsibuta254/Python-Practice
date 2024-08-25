day = input("Enter a day of the week (monday- Sunday): ").lower()

match day:
    case "monday":
        print("Ugh, Mondays...")

    case "tuesday":
        print("Just another workday...")

    case "wednesday":
        print("Hump day!")
    
    case "thurday":
        print("Almost there...")

    case "friday":
        print("TGIF")

    case "saturday" | "sunday": #match multiple values with pipe (|)
        print("Weekend vibes!")

    case _:
        print("Invalid day entered.")