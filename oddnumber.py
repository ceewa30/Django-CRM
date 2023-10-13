# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

num = int(input("Enter the range: "))
for i in range(1,num,2):
    print(i)
