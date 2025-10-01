
my_word = input("enter your word: ")

reversed_word = my_word[::-1]

if my_word == reversed_word:
    print("this is palindrom")
else:
    print("this is ordinari word")

# ეს არის 1 დავალება.



words = ["cat", "dog", "bobr", "dino", "development", "grass", "sun", "tim"]

reversed_words = words[::-1]

index = 0

for word in reversed_words:
    if index % 2 == 0:
        print(word)
    index += 1


# ეს არის 2 დავალება


word = input("enter your word: ")


goa_word = word[::-1]

for age in goa_word:
    print(age)

# ეს არის 3 დავალება.


num = "ilia$^*$7tavartkiladze$3@#@@$%%^^&**$##"


print("პირველი 5 სიმბოლო:", num[:5])

print("ბოლო 4 სიმბოლო:", num[-4:])

print("მეოთხე-მეათე სიმბოლოები:", num[3:10])

print("შებრუნებული სტრინგი:", num[::-1])

print("ყოველი მეორე სიმბოლო:", num[::2])

# ეს არის 4 დავალება.

