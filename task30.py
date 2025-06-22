sozlar = []
for i in range(5):
    soz = input(f"{i+1}-suzni kirirtng: ")
    sozlar.append(soz)

palindroms = []
for soz in sozlar:
    if soz == soz[::-1]:
        palindroms.append(soz)
print("Palindromlar: ",palindroms)