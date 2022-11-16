#### Assignment 1 ####

## Exercise 1 ##

    # Write a simple program that asks the user to input a name and outputs a simple greeting, such as ‘Hi Name! Nice to meet
    # you!’and in the other line,‘Welcome to the Programing Course!’.
    
print("What is your name?")
name = input()
print("Hi " + name + "! Nice to meet you!")
print("Welcome to the Programing Course!")

## Exercise 2 ##

    # Write a program that reads in a word provided by the user and prints the word in a reversed order. For example, if the
    # input is hello, the output should be ‘olleh’.

print("Please, type in a word")
word = input()
# simple solution
print(word[::-1])

# more complex:

empty_list = []
i = len(word)
for i in range(i):
    single_list = (word[::-1])
    empty_list.append(single_list)
print(empty_list[1])

# or more elegant

empty_list = []
i = len(word)
for i in reversed(range(i)):
    single_list = (word[i])
    empty_list.append(single_list)

print("".join(empty_list))



## Task 03 ##

    # Write a program that reads in an upper bound (number) provided by the user and prints the sequence of Fibonacci numbers that are less or equal to the number given by the user. Use a while-loop for this task.
    # The Fibonacci sequence is defined as  𝐹𝑛=𝐹𝑛−1+𝐹𝑛−2 . Use  𝐹0=0  and  𝐹1=1  as seed values.
    # For example, if the user inputs 6, the output should be 0, 1, 1, 2, 3, 5.

# here I had several approaches but none of those worked

## Task 04 ##

    # Write a program that reads in an upper bound (number) provided by the user and prints all integer numbers that are less or equal to the upper bound except the integer numbers that are divisible by 3. Use the continue statement. For example, if the user enters 6 as the upper bound, the output should be 0, 1, 2, 4, 5.

number = int(input("give me a number"))
for x in range(0, number):
    if x % 3 == 0:
        continue
    else:
        print(x)

## Task 05 ##

test = False
while test == False:
    print(
        "Please, give me the length of the three sides of a triangle (a,b,c) which fullfill the triaqngle inequality")
    x = int(input("a:"))
    y = int(input("b:"))
    z = int(input("c:"))
    if x<(y+z) and y<(x+z) and z<(y+x):
        test=True
        if  x == z and y==z and y==x:
            print("equilateral")
        elif (x!=z or y!=x or z!=y) and (x==z or y==x or z==y):
            print("isosceles")
        else:
            print("scalene")
    else:
        print("the triangle inequality is not given, please give in new values!")


# task 06:

    # no idea, found solution of first step in internet and try to understand and adapt it

number = int(input("Give in a non negative number:"))
def DecimalToOctal(n):
    octal = 0
    count = 1
    deci = n

    while (deci != 0):
        remainder = deci % 8 # here the reminder is calculater
        octal += remainder * count # store the octal value
        count = count * 10
        deci = deci // 8

    return octal

print(f"The octal representation of "+ str(number) + " is: " f"{DecimalToOctal(number)}")

# more general

number = float(input("Give in a non negative number:"))
def DecimalToOctal(n):
    octal = 0
    count = 1
    deci = n

    while (deci != 0):
        remainder = deci % 8 # here the reminder is calculater
        octal += remainder * count # store the octal value
        count = count * 10
        deci = deci // 8

    return octal

print(f"The octal representation of "+ str(number) + " is: " f"{DecimalToOctal(number)}")



