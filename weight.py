weight = int(input("Weight: "))

unit = input("(K)g or (L) bs: ")
converted = weight / 0.45
if unit.upper() =="K":
    print("Weight in Lbs: " + str(converted))

else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))