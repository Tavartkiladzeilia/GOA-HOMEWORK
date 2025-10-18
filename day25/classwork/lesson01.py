
name = "ilia"
age = 25
height = 1.68
is_student = True      

print(name, "- type:", type(name))
print(age, "- type:", type(age))
print(height, "- type:", type(height))
print(is_student, "- type:", type(is_student))

# ეს არის 1 დავალება


user_name = input("enteer your name: ")
user_age = input("enter your age: ")
fav_number = input("enter your word: ")

print("name:", user_name, "- type:", type(user_name))
print("age:", user_age, "- type:", type(user_age))
print("word:", fav_number, "- type:", type(fav_number))

user_age = int(user_age)
fav_number = float(fav_number)

total = user_age + fav_number
print("ასაკისა და საყვარელი რიცხვის ჯამი:", total)


# ეს არის 2 დავალება


for number in range(5, 101):
    if number % 2 == 0:
        even_or_odd = "ლუწი"
    else:
        even_or_odd = "კენტი"
    print(number, "-", even_or_odd, "- ტიპი:", type(number))

# ეს არის 3 დავალება



# ფუნქციები გამოიყენება კოდის გასამარტივებლად და მრავალჯერ გამოსაყენებლად.
# ისინი საშუალებას გვაძლევს დავარქვათ სახელი კონკრეტულ მოქმედებას და როცა გვჭირდება, უბრალოდ გამოვიძახოთ ეს სახელი.

# ნასწავლი ფუნქციები და მათი დანიშნულება:
# print() - ბეჭდავს ეკრანზე ინფორმაციას.
# input() - მომხმარებლისგან იღებს მონაცემს.
# type() - აბრუნებს ცვლადის ტიპს.
# int() - გარდაქმნის მნიშვნელობას მთელ რიცხვად.
# float() - გარდაქმნის მნიშვნელობას ათწილადად.
# str() - გარდაქმნის მნიშვნელობას სტრინგად (ტექსტად).
# range() - ქმნის რიცხვების მიმდევრობას.
# ეს არის 4 დავალება


# ფუნქციის არგუმენტი არის მონაცემი, რომელსაც ვაწვდით ფუნქციას მის მუშაობაში გამოსაყენებლად.
# მაგალითად, print("გამარჯობა") - აქ "გამარჯობა" არის არგუმენტი, რომელიც ფუნქციამ უნდა დაბეჭდოს.
# ასევე input("შეიყვანე სახელი: ") - აქ ტექსტი ეკრანზე გამოჩნდება როგორც მოწოდება და ეს არის არგუმენტი input ფუნქციისთვის.
# ეს არის 5 დავალება



