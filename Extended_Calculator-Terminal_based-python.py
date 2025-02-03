print("Select an operation to perform: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Percentage") 
print("7. Root") 
print("8. Power")
print("9. Odd numbers")
print("10. Even numbers")


operation = input("Enter choice (1/2/3/4/5/6/7/8/9/10): ")

if operation in ['1', '2', '3', '4', '5', '8', '9', '10']:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
elif operation == "6":
    num1 = float(input("Enter the percentage: "))
    num2 = float(input("Enter the number: "))
elif operation == "7":
    num1 = float(input("Enter the number: "))

if operation == "1":
    print("The result is:", num1 + num2)
elif operation == "2":
    print("The result is:", num1 - num2)
elif operation == "3":
    print("The result is:", num1 * num2)
elif operation == "4":
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        print("The result is:", num1 / num2)
elif operation == "5":
    print("The result is:", num1 % num2)
elif operation == "6":
    print("The result is:", num1 * (num2 / 100))
elif operation == "7":
    print("The result is:", num1 ** 0.5)
elif operation == "8":
    print("The result is:", num1 ** num2)
elif operation == "9":
    print("The odd numbers between", num1, "and", num2, "are:")
    while num1 < num2:
        if num1 % 2 != 0:
            print(num1)
        num1 += 1
elif operation == "10":
    print("The even numbers between", num1, "and", num2, "are:")
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(i)
else:
    print("Invalid input")