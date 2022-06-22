# Here, we're gonna learn about decision making using some statements/conditions in Py

# --------- Scenraio ------------
# ''' If it's Holi
#         It's  Holi festival
#         Drink plenty of Thandayi
#    otherwise If it's Saavan
#         It's  Saavan Festival
#         Drink plenty of Bhaang
#    otherwise
#         It's a normal day '''
is_Holi = False
is_Saavan = True
if is_Holi:
    print("It's Holi Festival\nDrink plenty of Thandayi")
elif is_Saavan:
    print("It's Saavan Festival\nDrink plenty of Bhaang")
else:
    print("It's a normal day")
print("Enjoy your DaYy!\n")


# Probie_1 -----------------------------------------------------
# ''' Price of house is $1M
#     If buyer has good credit,
#       they need to put down 10%
#     Otherwisw
#       they need to put down 20%
#     print the down payment '''
house_price = 1000000
credit = True
if credit:
    down_payment = 0.1 * house_price
    print(f"Discount based on your credit is: ${down_payment}")
else:
    down_payment = 0.2 * house_price
    print(f"Discount based on your credit is: ${down_payment}")
print(f"Down Payment: ${down_payment}\n")

# Probie_2 ----------------------------------------------------------
# ''' If student has high CGPA AND good skills
#       Eligible for Job !!
# Logical and , or , not operator
high_score = True
good_skills = True
asleel = True
if high_score and good_skills:
    print("Most welcome to the company!")
elif high_score or good_skills:
    print("You need some training at first!")
elif good_skills and not asleel:
    print("Get the effin out of here!")
else:
    print("Try out next time!")

# Probie_3 --------------------------------------------------------------
# ''' If temp is
#         It's  Hotuyii
#         Drink plenty of Colaaa
#    otherwise If it's Cold
#         It's Colduyii
#         Eat Gajar ka halwa
#    otherwise
#         It's a normal one
# Conditional operator -> > , < , >= , <= , ==
temp = int(input("\nCurrent temp:"))
if temp > 30:
    print("It's  Hotuyii\nDrink plenty of Colaaa")
elif temp < 30:
    print("It's Colduyii\nEat Gajar ka halwa")
else:
    print("It's a normal one")

# Probie_4 --------------------------------------------------------------
# If name length less than 2 chars
#       name must be at least 2 chars
# Otherwise If name is 45 chars
#       name can be a max of 45 chars
# Otherwise
#       name looks good enough
name = input("\nEnter your name: ")
if len(name) < 2:
    print("Name must be at least of 2 characters..")
elif len(name) > 45:
    print("Name can be a max of 45 characters..")
else:
    print("Name looks good enough!")

# Probie_5 --------------------------------------------------------------
# Take weight as input
#   Specify the (L)bs or (K)gs
#       Print - You're __ pounds/kgs
weight = float(input("Weight: "))
unit = input("(L)bs or (K)gs: ")
if unit.lower() == "l":
    cvt = weight * 0.45
    print(f"You're {cvt} kgs.")
elif unit.lower() == 'k':
    cvt = weight / 0.45
    print(f"You're {cvt} pounds.")
else:
    print("Choose correct input(units)!!")
