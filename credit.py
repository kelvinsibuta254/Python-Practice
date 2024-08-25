high_income = True
good_credit = False
student = False

#if high_income or good_credit and not student

if high_income and good_credit:
    print("Eligible")

elif not student:
    print("eligible")

else:
    print("Ineligible")