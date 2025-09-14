#  Immutable:
# - int
# - float
# - bool
# - str

# Mutable:
# - list

# ეს არის 1 დავალება


goa_list = list(range(1, 21))

goa_list[-11] = 453

goa_list[-4] = 150

print(goa_list)

# ეს არის 2 დავალება


surname = "tavartkiladze"

print( surname[3])
print(surname[5])

# ეს არის 3 დავალება


secret_password = 59325051501

guess = int(input(" გამოიცანი პაროლი: "))


while guess != secret_password:
    print("არასწორია თავიდან ცადე!!!")
    guess = int(input(" გამოიცანი პაროლი: "))

print("შენ გამოიცანი პაროლი!")


# ეს არის 4 დავალება



num = 40

while num >= 10:
    if num % 2 == 0:
        print(num)
    num -= 1

# ეს არის 5 დავალება




