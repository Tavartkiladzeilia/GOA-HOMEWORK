numbers = [2, 3, 4, 5]
product = 1
for num in numbers:
    product *= num
print("ნამრავლი არის:", product)

# ეს არის 1 დავალება



my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_nums[0:9])

# ეს არის 2 დავალება


numbers = [2, 7, 3, 9, 1]
for my_num in numbers:
    if my_num < 5:
        print(my_num)

# ეს არის 3 დავალება


my_name = input("enter your name: ")
my_name = my_name.lower()
print(my_name)

# ეს არის 4 დავალება


ilia_name = "ilia"
ilia_name = ilia_name.upper()
print(ilia_name)

# ეს არის 5 დავალება


my_word = "zhuzhu and koko."
my_word = my_word.capitalize()
print(my_word)

# ეს არის 6 დავალება



def sum_numbers(a, b):
    print( a + b)

sum_numbers(5, 7)

# ეს არის 7 დავალება



def even_or_odd(num):
    if num % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"

print(even_or_odd(4))
print(even_or_odd(7))

# ეს არის 8 დავალება



def check_sign(num):
    if num > 0:
        return "დადებითია"
    elif num < 0:
        return "უარყოფითია"
    else:
        return "ნულია"

print(check_sign(-3))
print(check_sign(7))

# ეს არის 9 დავალება



def greet(name):
    print("Hello", name)

greet("Giorgi")
greet("Nino")

# ეს არის 10 დავალება

