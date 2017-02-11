days = int(input("Enter days:"))
years = days / 360
months = (n % 360) / 30
days = (n % 360) % 30
print ("Years :", years, "Months :", months, "Days :", days)
