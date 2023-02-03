def phones():
    print("1-aplle\n2-samsung\n3-xiaomi")
    user = int(input("Enter number of your choice : "))
    info_dict = {"User_name" : "", "User_number" : "" ,"User_address" : "" , "payment" : "" , "Phone" : "" , "quantity" : "" , "vip" : ""}
    delivery = 12
    is_vip = f"{False}\n"
    info_dict["vip"] = is_vip
    if user == 1 :
        print("1-iphoneX \nprice = 1200\n2-iphone12 \nprice = 1400\n3-iphone6s \nprice = 500\n4-iphone14 \nprice = 2000".title())
        phone_choice = int(input("Enter number of phone you want : "))
        if phone_choice == 1 :
            phone = "IphoneX"
            how = int(input("Enetr quantity : "))
            price = 1200
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if phone_choice == 2 :
            phone = "iphone12"
            how = int(input("Enetr quantity : "))
            price = 1400
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if phone_choice == 3 :
            phone = "iphone6s"
            how = int(input("Enetr quantity : "))
            price = 500
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if phone_choice == 4 :
            phone = "iphone14"
            how = int(input("Enetr quantity : "))
            price = 2000
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
    if user == 2 :
        print("1-not10pro \nprice = 1700\n2-s21Ultra \nprice = 1900\n3-J7 \nprice = 300\n4-j5 \nprice = 200".title())
        phone_choice = int(input("Enter number of phone you want : "))
        delivery = 12
        if phone_choice == 1 :
            phone = "not10pro"
            how = int(input("Enetr quantity : "))
            price = 1700
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if phone_choice == 2 :
            phone = "s21Ultra"
            how = int(input("Enetr quantity : "))
            price = 1900
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if phone_choice == 3 :
            phone = "J7"
            how = int(input("Enetr quantity : "))
            price = 300
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if phone_choice == 4 :
            phone = "j5"
            how = int(input("Enetr quantity : "))
            price = 200
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
    if user == 3 :
        print("1-Note 10 lite \nprice = 1200\n2-poco X3 \nprice = 1400\n3-poco F3 \nprice = 500\n4-note 8pro \nprice = 2000".title())
        phone_choice = int(input("Enter number of phone you want : "))
        delivery = 12
        if phone_choice == 1 :
            phone = "Note 10lite"
            how = int(input("Enetr quantity : "))
            price = 1200
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if phone_choice == 2 :
            phone = "poco x3"
            how = int(input("Enetr quantity : "))
            price = 1400
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if phone_choice == 3 :
            phone = "poco f3"
            how = int(input("Enetr quantity : "))
            price = 500
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if phone_choice == 4 :
            phone = "note 8pro"
            how = int(input("Enetr quantity : "))
            price = 2000
            name = input("Enter yourname : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Phone"] = phone
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")





def laptops():
    print("1-HP\n2-Asus\n3-Lenovo")
    user = int(input("Enter number of your choice : "))
    info_dict = {"User_name" : "", "User_number" : "" ,"User_address" : "" , "payment" : "" , "Laotop" : "" , "quantity" : "" , "vip" : ""}
    delivery = 12
    is_vip = f"{False}\n"
    info_dict["vip"] = is_vip
    if user == 1:
        print("1-Zenbook \nprice = 3200\n2-Zedbook \nprice = 5400\n3-Notebook \nprice = 2500\n4-deltaBook \nprice = 4000".title())
        user_choice = int(input("Enter number of laptop you want : "))
        if user_choice == 1 :
            laptop = "Zen book"
            how = int(input("Enetr quantity : "))
            price = 3200
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 2 :
            laptop = "Zedbook"
            how = int(input("Enetr quantity : "))
            price = 5400
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 3 :
            laptop = "notebook"
            how = int(input("Enetr quantity : "))
            price = 2500
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 4 :
            laptop = "deltabook"
            how = int(input("Enetr quantity : "))
            price = 4000
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
    if user == 2:
        print("1-Xl555 \nprice = 3200\n2-babybook \nprice = 5400\n3-xl550 \nprice = 2500\n4-tuf fx15 \nprice = 4000".title())
        user_choice = int(input("Enter number of laptop you want : "))
        if user_choice == 1 :
            laptop = "xl555"
            how = int(input("Enetr quantity : "))
            price = 3200
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 2 :
            laptop = "babybook"
            how = int(input("Enetr quantity : "))
            price = 5400
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 3 :
            laptop = "xl550"
            how = int(input("Enetr quantity : "))
            price = 2500
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 4 :
            laptop = "tuf fx15"
            how = int(input("Enetr quantity : "))
            price = 4000
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
    if user == 3:
        print("1-lenovoX \nprice = 3200\n2-touch \nprice = 5400\n3-Xbook \nprice = 2500\n4-gaming \nprice = 4000".title())
        user_choice = int(input("Enter number of laptop you want : "))
        if user_choice == 1 :
            laptop = "lenovox"
            how = int(input("Enetr quantity : "))
            price = 3200
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 2 :
            laptop = "touch"
            how = int(input("Enetr quantity : "))
            price = 5400
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 3 :
            laptop = "Xbook"
            how = int(input("Enetr quantity : "))
            price = 2500
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 4 :
            laptop = "gaming"
            how = int(input("Enetr quantity : "))
            price = 4000
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["Laotop"] = laptop
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")




def foods():
    print("1-Break Fast\n2-lunch\n3-dinner")
    user = int(input("Enter number of your choice : "))
    info_dict = {"User_name" : "", "User_number" : "" ,"User_address" : "" , "payment" : "" , "foods" : "" , "quantity" : "","vip" : ""}
    delivery = 12
    is_vip = f"{False}\n"
    info_dict["vip"] = is_vip
    if user == 1:
        print("1-Egg \nprice = 20\n2-Bread \nprice = 10\n3-cereal \nprice = 30\n4-milk \nprice = 5".title())
        user_choice = int(input("Enter number of laptop you want : "))
        if user_choice == 1 :
            food = "egg"
            how = int(input("Enetr quantity : "))
            price = 20
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 2 :
            food = "bread"
            how = int(input("Enetr quantity : "))
            price = 10
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 3 :
            food = "cerel"
            how = int(input("Enetr quantity : "))
            price = 30
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 4 :
            food = "milk"
            how = int(input("Enetr quantity : "))
            price = 5
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
    if user == 2:
        print("1-fish \nprice = 200\n2-kebab \nprice = 90\n3-chicken \nprice = 50\n4-beef \nprice = 100".title())
        user_choice = int(input("Enter number of laptop you want : "))
        if user_choice == 1 :
            food = "fish"
            how = int(input("Enetr quantity : "))
            price = 200
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 2 :
            food = "kebab"
            how = int(input("Enetr quantity : "))
            price = 90
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 3 :
            food = "chicken"
            how = int(input("Enetr quantity : "))
            price = 50
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 4 :
            food = "beef"
            how = int(input("Enetr quantity : "))
            price = 100
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
    if user == 3:
        print("1-fish \nprice = 200\n2-kebab \nprice = 90\n3-chicken \nprice = 50\n4-beef \nprice = 100".title())
        user_choice = int(input("Enter number of laptop you want : "))
        if user_choice == 1 :
            food = "fish"
            how = int(input("Enetr quantity : "))
            price = 200
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 2 :
            food = "kebab"
            how = int(input("Enetr quantity : "))
            price = 90
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 3 :
            food = "chicken"
            how = int(input("Enetr quantity : "))
            price = 50
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 4 :
            food = "beef"
            how = int(input("Enetr quantity : "))
            price = 100
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["foods"] = food
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")




            
def clothes():
    print("1-Pants\n2- T-shirt\n3-pijames")
    user = int(input("Enter number of your choice : "))
    info_dict = {"User_name" : "", "User_number" : "" ,"User_address" : "" , "payment" : "" , "clothes" : "" , "quantity" : "","vip" : ""}
    delivery = 12
    is_vip = f"{False}\n"
    info_dict["vip"] = is_vip
    if user == 1:
        print("1-zara\nprice = 200\n2-gucci \nprice = 1000\n3-fendi \nprice = 300\n4-Trapstar \nprice = 5000".title())
        user_choice = int(input("Enter number of laptop you want : "))
        if user_choice == 1 :
            pants = "zara"
            how = int(input("Enetr quantity : "))
            price = 200
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 2 :
            pants = "gucci"
            how = int(input("Enetr quantity : "))
            price = 1000
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 3 :
            pants = "fendi"
            how = int(input("Enetr quantity : "))
            price = 300
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 4 :
            pants = "TrapStar"
            how = int(input("Enetr quantity : "))
            price = 5
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
    if user == 2:
        print("1-zara\nprice = 200\n2-gucci \nprice = 1000\n3-fendi \nprice = 300\n4-Trapstar \nprice = 5000".title())
        user_choice = int(input("Enter number of laptop you want : "))
        if user_choice == 1 :
            pants = "zara"
            how = int(input("Enetr quantity : "))
            price = 200
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 2 :
            pants = "gucci"
            how = int(input("Enetr quantity : "))
            price = 1000
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 3 :
            pants = "fendi"
            how = int(input("Enetr quantity : "))
            price = 300
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 4 :
            pants = "TrapStar"
            how = int(input("Enetr quantity : "))
            price = 5
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
    if user == 3:
        print("1-zara\nprice = 200\n2-gucci \nprice = 1000\n3-fendi \nprice = 300\n4-Trapstar \nprice = 5000".title())
        user_choice = int(input("Enter number of laptop you want : "))
        if user_choice == 1 :
            pants = "zara"
            how = int(input("Enetr quantity : "))
            price = 200
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 2 :
            pants = "gucci"
            how = int(input("Enetr quantity : "))
            price = 1000
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 3 :
            pants = "fendi"
            how = int(input("Enetr quantity : "))
            price = 300
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")
        if user_choice == 4 :
            pants = "TrapStar"
            how = int(input("Enetr quantity : "))
            price = 5
            name = input("Enter your Name : ")
            number = int(input("Enter your phone number : "))
            address = input("Enter your address : ")
            res = how * price + delivery
            info_dict["User_name"] = name
            info_dict["User_number"] = number
            info_dict["User_address"] = address
            info_dict["payment"] = res
            info_dict["clothes"] = pants
            info_dict["quantity"] = how
            with open(file="info.txt",mode="a") as file :
                for key,value in info_dict.items():
                    file.write(f"{key} : {value} \n")
            print(f"you should pay {res} dollars\nyour shopping is saccussfuly!")