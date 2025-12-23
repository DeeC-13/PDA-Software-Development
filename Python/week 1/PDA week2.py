
#Excercise 1

num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))
calc = input("would you like to add, subtract, multiply or divide? press +, -, *, /")
add = (num1 + num2)
subtract = int(num1 - num2)
multiply = int(num1 * num2)
divide = int(num1 / num2)

if calc == '+':
    print("the sum of: ", num1, "and", num2, "is", int(add))
elif calc == '-':
    print(num1, "minus", num2, "is:  ", int(subtract))
elif calc == '*':
    print(num1, "multiplied by", num2, "is: ", int(multiply))
elif calc == '/':
    print(num1, "divided by", num2, "is: ", int(divide))
else:
    print("sorry invalid input")

#Excercise 2
grade = int(input("Enter students score between 1-100: "))

if 0 <= grade <= 100:
    if grade > 90:
        print("The student has been graded an A.")
    elif grade > 80:
        print("The student has been graded an B.")
    elif grade > 70:
        print("The student has been graded an C.")
    elif  grade > 60:
        print("The student has been graded an D.")
    else:
        print("The student has been graded an F.")
else:
    print("invalid input enter score between 1-100")

#Excercise 3
price = int(input("Please enter the item price: £ "))
discount = int(input("Please enter the discount amount: "))
#discount1 = 1 + (discount/100)
discount1 = price / (100 / discount)
d_price = price - discount1

print("Your discounted is: £", f"{discount1:.2f}")

print("Your new discounted price is: £ ", f"{d_price:.2f}")




