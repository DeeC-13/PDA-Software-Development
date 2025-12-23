#Greengrocer
#part 1 get 5 vegetables

veg_list = []

veg_l = 5

for i in range(veg_l):
    veg_l = str(input("Enter a vegetable: "))
    veg_list.append(veg_l)

print("Thank you. You have chosen: \n", veg_list)

#part 2 more veg
while veg_list:
    more_veg = str(input("Enter another vegetable or fruit, \n or type exit when you are done: "))

    if more_veg != "exit":
        veg_list.append(more_veg)

    elif more_veg == "exit":
        print("We have enough veg thank you!")
        print("We have ",len(veg_list), "fruit and veg in stock")
        print("\n".join(veg_list))
        break


#how much are the veg?

veg_dict = {}

for i in range(5):
    print("How much is the ", veg_list[i], "?")

    while True:
        try:
            price = float(input("The price is: £ "))
            veg_dict[str(veg_list[i])] = "{:.2f}".format(price)
            break
        except ValueError:
            print("Invalid price! Please enter a valid price.")

for veg_list, price in veg_dict.items():
    print("The price of " + veg_list + " is £ " + str(price))



