names = ["ilia", "vano", "gabriel", "nika", "gio"]
names.pop(0) 
names.pop(-1)  
print(names)

# es aris 1 davaleba


# .insert(index, value) - ამატებს ახალ ელემენტს კონკრეტულ ინდექსზე
# .append(value) - ამატებს ახალ ელემენტს სიის ბოლოში
# .pop(index) - შლის ელემენტს მითითებული ინდექსით (თუ არ მივუთითებთ, შლის ბოლოს)
# len(list) - აბრუნებს სიაში მყოფი ელემენტების რაოდენობას

# es aris 2 davaleba


names1 = ["ilia", "nika", "lika", "giorgi", "noe"]
names1.insert(2, "erekle")  # 2 ინდექსზე ჩასვამს ახალ სახელს
print(names1)
# es aris 3 davaleba


# .lower() - გადააქცევს მთელ ტექსტს პატარა ასოებად
# .upper() - გადააქცევს მთელ ტექსტს დიდ ასოებად
# .capitalize() - ტექსტის მხოლოდ პირველ ასოს გადააქცევს დიდ ასოდ
# .find("a") - მოძებნის ასო "a"-ს და დააბრუნებს მის ინდექსს (თუ ვერ იპოვა, დააბრუნებს -1)

# es aris 4 davaleba


surname = input("enter your surname: ")

if surname[0].isupper():  
    print("Hello")
else:
    print("Bye")


# es aris 5 davaleba



name = input("enter your name: ")
num = input("enter your num: ")

if num in name:
    print("found it", name.find(num)) 
else:
    print("Can't find character")


# es aris 6 davaleba


surname = input("enter your surname: ")
change = input("როგორ გინდა რომ შეიცვალოს? (upper/lower/capitalize): ")

if change == "upper":
    print(surname.upper())
elif change == "lower":
    print(surname.lower())
elif change == "capitalize":
    print(surname.capitalize())
else:
    print("enter is false!")


# es aris 7 davaleba




nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(nums)):
    if i % 2 != 0:    
        print(nums[i])


# es aris 8 davaleba


# მეცხრე და მეათე ვერ გავიგე


# def - ქმნის ფუნქციას რომელიც უნდა გამოვიყენოთ მაგალითად misalmebaში უნდა ჩასვა კოდი
# return და print თითქმის ერთნაირი ფუნქციაა ოღონდ print -ს აქვს ფრჩხილები და return -ს არა 

# ეს არის 11 დავალება



def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print("jami:", total)

sum([1, 2, 3, 4, 5])


# es aris 12 davaleba

