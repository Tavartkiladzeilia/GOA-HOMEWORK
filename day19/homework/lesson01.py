# ინდექსი არის მთელი რიცხვი, რომელიც მიუთითებს ელემენტის პოზიციას.ასევე ინდექსირება არის და მუშაობს რიცხვები მარცხნიდან მარჯვნივ და ასეევ მარჯვიდან მარცხვნივ.
# ეს არის 1 დავალება

numer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(numer[-3])
print(numer[-8])
print(numer[6])
print(numer[1])
# ეს არის 2 დავალება


user_input = input("enter numer 0, 10 :")


if user_input.isdigit():
    index = int(user_input)
    
    if 0 <= index <= 10:

        my_list = [f"element {i}" for i in range(11)]
        

        my_list[index] = "updated"


        print("updated list")
        print(my_list)
    else:
        print("The number is not in the range 0 to 10.")
else:
    print("Please enter only a number.")
        
# ეს არის 3 დავალება


my_list = ["ვაშლი", "ბანანი", "მსხალი", "ატამი", "კივი"]

for item in my_list:
    print(item)

# ეს არის 4 დავალება



my_list = ["element1", "element2", "element3", "element4", "element5", "element6", "element7", "element8"]


my_list[2] = "modified element 3"
my_list[6] = "modified elementი 7"


print(my_list)

# ეს არის 5 დავალება





