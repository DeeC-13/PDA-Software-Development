import random

#creates animal list
animal_list = ["mouse", "rat", "badger", "cat", "donkey"]

#prints length of animal list
print(len(animal_list))

new_animal = input("Enter an animal name: ")

#adds animal to the end of animals list
animal_list.append(new_animal)

#prints each animal on a separate line
for item in animal_list:
    print(item)

print(animal_list[2])

#removes badger from animals list
animal_list.remove("badger")
print(animal_list)

#generates random number
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)
num4 = random.randint(1, 10)

#creates numbers list from random variables
nums = [num1, num2, num3, num4]

#prints numbers list
print(nums)

#prints first item in numbers list
print(nums[0])

#prints third item in numbers list
print(nums[2])

#asks user for a number
number = int(input("Enter a number: "))

#changes second number to inputted number from user and prints numbers list
nums[1] = number
print(nums)

#removes second number from numbers list
nums.pop(1)
print(nums)

#creates price list
price = [1.99, 2.56, 9.21, 6.35, 7.59]

#sorts price list in ascending order and prints
price.sort()
print(price)

#sorts price list in ascending order and prints each on a separate line
for items in price:
    print(items)

#sorts price list in descending order and prints
price.sort(reverse = True)
print(price)

#sorts price list in descending order and prints each on a separate line
for items in price:
    print(items)

#creates a dictionary of names and heights
heights = {
    "Sandra": 1.2,
    "Tom": 1.78,
    "Jim": 1.67,
    "Sally": 1.5,
    "Jonah": 1.78,
    "Frank": 1.8
}

#gets tallest person by height and prints name and height
for key, value in heights.items():
    if value == max(heights.values()):
        print("The tallest person is: ", key, "with height: ", value)

#gets smallest person by height and prints name and height
for key, value in heights.items():
    if value == min(heights.values()):
        print("The smallest person is: ", key, "with height: ", value)

#finds the average height of the heights vales and prints to two decimal places
total = 0
count = 0

for value in heights.values():
    total += value
    count += 1

average = total / count
print("The average height is:", round(average, 2))

#creates two lists a key list and a employee details values list
label = ['name', 'job title', 'pay grade', 'address']

data = [["David Smith", "Engineer", "Grade 3", "25 River Road, KY23 7GG"],
         ["Sandra Stalker", "Chief Engineer", "Grade 4", "76 Forest Lane, KY15 8TT"]]

#iterates through the lists to convert to a dictionary and prints the dictionary
employee = {i[0]: {k: v for k,v in zip(label,i)} for i in data}

print(employee)








