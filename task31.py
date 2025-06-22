from collections import Counter

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 90, 90, 90, 10, 10]

sana = Counter(my_list)
chqarish = sana.most_common(1)
if chqarish:
    print(chqarish)