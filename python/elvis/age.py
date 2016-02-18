
def age_calculator(age):
    years = int(age / 365)
    months = int((age - (years * 365)) / 30)
    weeks = int((age - (years * 365) - (months * 30)) / 7)
    days = age - (years * 365) - (months * 30) - (weeks * 7)

    print(years, " years")
    print(months, " months")
    print(weeks, " weeks")
    print(days, " days")


ageInDays = raw_input("Enter your age in days:")

try:
    intAgeInDays = int(ageInDays)
    age_calculator(intAgeInDays)
except:
    print("Invalid input")
