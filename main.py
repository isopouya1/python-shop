from handler import *
print("------------- Welcome to py shop -------------")
print("1-phones\n2-laptops\n3-foods\n4-clothes\n5-exit".title())

user_choice = int(input("Enter number what you want : "))

if user_choice == 1:
    phones()
    choice = input("do want get back y/n? ")
    if choice == "y":
        print("1-phones\n2-laptops\n3-foods\n4-clothes\n5-exit".title())
        user_option = int(input("Enter number what you want : "))
        if user_option == 1:
            phones()
    elif choice == "n" :
        print("Thanks for your shoping")



if user_choice == 2:
    laptops()
    choice = input("do want get back y/n? ")
    if choice == "y":
        print("1-phones\n2-laptops\n3-foods\n4-clothes\n5-exit".title())
        user_option = int(input("Enter number what you want : "))
        if user_option == 2:
            laptops()
    elif choice == "n" :
        print("Thanks for your shoping")



if user_choice == 3:
    foods()
    choice = input("do want get back y/n? ")
    if choice == "y":
        print("1-phones\n2-laptops\n3-foods\n4-clothes\n5-exit".title())
        user_option = int(input("Enter number what you want : "))
        if user_option == 3:
            foods()
    elif choice == "n" :
        print("Thanks for your shoping")



if user_choice == 4:
    clothes()
    choice = input("do want get back y/n? ")
    if choice == "y":
        print("1-phones\n2-laptops\n3-foods\n4-clothes\n5-exit".title())
        user_option = int(input("Enter number what you want : "))
        if user_option == 4:
            laptops()
    elif choice == "n" :
        print("Thanks for your shoping")