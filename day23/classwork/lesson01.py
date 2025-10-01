
surname = input("enter your surname: ")


goa_surname = surname[::-1]

for age in goa_surname:
    print(age)

# ეს არის 1 დავალება.


# sliseing = არის იგივე ტაც ინდექსინგი  step რაც არის რომელიმე ასოს გადახტომა.
# indexing = არის რომ არ მოგვიწიოს ბევრი ცვლადში დაწერა რომელიმე ასოსი მაშინ [] ამაში ვწერთ რასაც ვინხავთ ცვლადში

# ეს არის 2 დავალება.


my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


evenmy_index_elements = my_list[::2]


print("ლუწ ინდექსებზე მყოფი ელემენტები:")
for item in evenmy_index_elements:
    print(item)

# ეს არის 3 დავალება.



names = ["ანა", "სანდრო", "ვანო", "დავითი", "ელენე", "მარი", "ნოე", "ლუკა", "მაქსი", "ლაშა"]

start = int(input("შეიყვანე სიის დასაწყისი ინდექსი (0-დან 9-მდე): "))
end = int(input("შეიყვანე სიის დასასრული ინდექსი (1-დან 10-მდე): "))

my_names = names[start:end]

print("შერჩეული სახელები  მონაკვეთშია:")
for name in my_names:
    print(name)


# ეს არის 4 დავალება.



surname = input("enter your surname: ")

if surname.shvili("shvili"):
    print("Hello")
else:
    print("Byee")

# ეს არის 6 დავალება.