lastname = input("What's your lastname? ")
firstname = input("What's your first name? ")
middlename = input("What's your middle name? (leave if you dont have one) ")

print(lastname + " " + middlename + " " + firstname)
print(lastname, middlename, firstname)
print(lastname, middlename, firstname, sep=" ")
print(f'Omg, your name is {lastname} {middlename} {firstname} ?')