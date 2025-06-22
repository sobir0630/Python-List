list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

listlar = []
for i in list1:
    if i in list2 and i not in listlar:
        listlar.append(i)
print("natija:", listlar)