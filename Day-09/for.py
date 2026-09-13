for i in range(5):
    print(i)
print("The n in the for loop means that it will take value from the range and then put in the variable i and then it will print the value of i in each iteration of the loop. The range function generates a sequence of numbers from 0 to 4 (5 is not included) and the for loop iterates over that sequence, assigning each number to the variable i in turn.")
list = ['John', 'Jane', 'Jack', 'Jill', 'Husnain']

for i in list:
    print(f"List data: {i}")

tuple = ('John', 'Jane', 'Jack', 'Jill', 'Husnain')
for i in tuple:
    print(f"Tuple data: {i}")
