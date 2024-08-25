age = int(input("Enter your age: "))
has_id = True

match age:
    case 18 | 19: #Match multiple values with pipe (|)
        if age >= 18 and has_id:
            print("You are eligible to vote. ")
        
        else:
            print("You need a valid ID to vote.")

    case _:
        print("You are not yet eligible to vote.")
