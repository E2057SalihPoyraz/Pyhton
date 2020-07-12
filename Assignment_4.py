number = int(input("Please enter a number to learn \

if it is a prime number:"))



if number == 2:

    print(f"{number} is a prime number")

elif number%2==0 or number<0:

    print(f"{number} is NOT a prime number")

else:    

    for i in range(2,number):

        if number % i == 0 :

            print(f"{number} is NOT a prime number")

            break

    else:

        print(f"{number} is a prime number") 
