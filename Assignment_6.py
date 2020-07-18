# You can use a nested for loop. Collect all these numbers into a list
# The desired output for n=100 :

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
# 61, 67, 71, 73, 79, 83, 89, 97]

number = int(input("Please enter the limit number: "))
mylist = list(range(number, 1, -1))
prime = []
for i in range(2, len(mylist) + 1):
    status = True
    for j in range(2, i):
        if i % j == 0:
            status = False
    if status:
        prime.append(i)
print(prime)
