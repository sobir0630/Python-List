ruyhatlar = []

nechta = int(input("nechta element kritmoqchisiz? "))
for i in range(nechta):
    user = input(f"{i+1}-Ruyhatni kritng: ")
    ruyhatlar.append(user)


group1 = []
group2 = []
group3 = []

for ruyhat in ruyhatlar:
    uzunlik = len(ruyhat)
    if uzunlik <= 3:
        group1.append(ruyhat)
    elif 4 <= uzunlik <= 6:
        group2.append(ruyhat)
    else:
        group3.append(ruyhat)
 
print("<=3 harfli:", group1)
print("4-6 harfli:", group2)
print(">6 harfli:", group3)