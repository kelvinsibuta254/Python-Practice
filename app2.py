successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

else:
    print("Attempted 3 times and failed")
    #only executed if the loop doesn't undergo an early termination