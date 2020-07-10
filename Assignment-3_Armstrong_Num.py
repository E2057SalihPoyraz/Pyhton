while True:
    number = input("Please enter a number or \
type 'q' to end the program: ")
    numberofdigits = len(number)
    sum = 0
    if number == "q":
        print("Good bye!")
        break
    elif number.isdigit() != True:
        print("It is an invalid entry. \
Don't use non-numeric, float \
or negative values!")
        continue
    for i in number:
        sum += int(i) ** numberofdigits
    if sum == int(number):
        print(number, "is an Armstrong number") 
    else:
        print(number, "is not an Armstrong number")
