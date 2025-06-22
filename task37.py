list1 = list(map(int, input("1_ruyhatni kritng vergul bilan krtng: ").split(',')))
list2 = list(map(int, input("2_ruyhatni kritng vergul bilan krtng: ").split(',')))

if len(list1) != len(list2):
    print("elentlsr teng emas!")
else:
    for i in range(len(list1)):
        list1[i], list2[i] = list1[i], list2[i]
        
    print("Yanagi 1-ruyhat:", list1)
    print("Yanagi 2-ruyhat:", list2)