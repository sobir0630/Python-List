names = []

while True:
    ism = input("Ism kiriting yoki (t) deb kiriting: ")
    if ism.lower() == 't':
        print("Dastur to'xtadi")
        break
    names.append(ism)

print("Natija:", len(names))
print("Ismlar ro'yxati:", names)