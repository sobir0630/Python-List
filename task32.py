user = int(input("nechta suz kirtmoqchsiz: "))

ruyhat = []
for i in range(user):
    enter = input(f"{i+1}-suzni kritng: ")
    if len(enter) >= 5:
        ruyhat.append(enter)

    else: 
        print("siz kritgan suz 5ta harfdan kam!!!")

print(f"siz kirtganlar: {ruyhat}")


