#name = "Diyor"

#city = "tashkent"
#math = "I bought a new 🚙"

#name = 'diyor'
#print("my name is " + name)

#name = 'diyor'
#surname = 'abdunaimov'
#name_surname = f"name {surname}"
#print(name_surname)
x = 10

name = 'Amin'
surname = 'Aminov'
print(f"hello, my name is {name}. {name} {surname}!")

name = input("What is your name? ")
print()
print("hello,",name)


#== Multiple line comments and statements
r"""
fafafafasfafda
\\\\\\



"""





a = input("Whats your last name? ")
print("nice to meet you, ",name, a)

b = input("What do you want to order? \nMenu \nWater \nJuice \nCofe \nTea: ")
print("Your order is accepted")

# Gets input and uses methods to remove all newspaces 
#and leading and trailing spaces and 
#lowers all chars
c = input("Do you want anything else?" ).strip().lower()

# Bool check
if c == "yes":
    print("What else do you want to order? ")
else:
    print("Your order will be ready in 5 min")



