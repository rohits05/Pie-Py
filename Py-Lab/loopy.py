# In this, we're gonna learn about loops in Py
# ---------------- Starting with While Loops ---------------------
i = 1
while i <= 5:  # Condition
    print('^'*i)
    i = i+1  # Incrementing the val
print("Done!\n")


# Guess game_________________________________________
# Takes a number from user as guess and outputs desired msg
mystery = 14
guess_cnt = 0
limit = 3
while guess_cnt < limit:  # no. of guesses
    guess = int(input('Guess: '))
    guess_cnt += 1
    if guess == mystery:
        print('You Won!')
        break
else:
    print("Try Again..")

# Car game________________________________________________
# help -
#     start - to start the car
#     stop - to stop the car
#     quit - to exit
cmd = ""
started = False
while True:
    cmd = input("> ").lower()
    if cmd == "start":
        if started:
            print("Already started..")
        else:
            started = True
            print("Brumm Brumm__Car Started.....Udao Abb!")
    elif cmd == "stop":
        if not started:
            print("Already stopped..")
        else:
            started = False
            print("Tanki khaali__Car stopped!.....Petrol bharwane ka re Baba")
    elif cmd == "quit":
        break
    elif cmd == "help":
        print('''
        start - to start the car
        stop - to stop the cae
        quit - to exit
        ''')
    elif cmd == "quit":
        print("Bohot thakk gya re mai, ab jata hai..")
        break
    else:
        print("Theek se type kar re baba !!")


# ------------------- Starting with For Loops -------------------------------
for item in 'Rohit':
    print("\n", item)

for item in ['Rohit', 'Krish', 'Goduyii']:
    print(item, end=" ")
print()

for item in range(19):  # range fn. creates an object which we can iterate over
    print(item, end=" ")
print()

for i in range(1, 16, 2):  # Step jumping using range fn.
    print(i, end=" ")
print()

# Probie_1 ------------
prices = [25, 39, 88]
total = 0
for price in prices:
    total += price
print(f"Total is: {total} rs.")
print()


# --------------------- Starting with Nested Loops ---------------------------------------
# Having one or more loops inside one loop
# Displaying co-ordinates
print("Displaying co-ordinates:")
for x_line in range(3):
    for y_line in range(2):
        print(f"({x_line},{y_line})")
print()

# Displaying F using ^ symb
num = [5, 2, 5, 2, 2]
for i in num:
    console = ''
    for cnt in range(i):
        console += '^'
    print(console)

# _________________________________________________________(X)__________________________________________________________#
