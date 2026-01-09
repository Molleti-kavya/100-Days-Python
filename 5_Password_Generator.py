import random

print("Welcome to the Password Generator : ")

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')','~','_','-','?','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']

n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like in your password?\n"))
n_numbers = int(input("How many numbers would you like in your password?\n"))

password = []
for i in range(1,n_letters+1):
    password += random.choice(letters)
for i in range(1, n_symbols + 1):
    password += random.choice(symbols)
for i in range(1, n_numbers + 1):
    password += random.choice(numbers)
# print(f"Your Password is : {password}")

random.shuffle(password)
# print(f"YOur Password is : {password}")
pw = ""
for i in password:
    pw += i
print(f"Your Password is : {pw}")