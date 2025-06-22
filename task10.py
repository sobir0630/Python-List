my_list = [10, 20, 30, 40, 50]

index = int(input("Qaysi indeksdagi qiymatni o'zgartirmoqchisiz? (0-4): "))
new_value = input("Yangi qiymatni kiriting: ")

if 0 <= index < len(my_list):
    my_list[index] = new_value
    print("Yangilangan ro'yxat:", my_list)
else:
    print("Noto'g'ri indeks kiritildi.")