year = int(input("Please enter year in 4-digits: "))
leap_year = ((year % 4 == 0) and (year % 100 !=0)) or (year % 400 == 0)
print(leap_year * f"{year} is a leap_year")
print((not leap_year) * f"{year} is not a leap_year")
