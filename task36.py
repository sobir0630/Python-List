ruyhat = []
user = int(input("nechta suz kritasiz? "))
for i in range(user):
    entry = input(f"{i+1}_suzni kritng: ")
    ruyhat.append(entry)

max_ruyhat = []
for uzun in ruyhat:
    if not max_ruyhat or len(uzun) > len(max_ruyhat[0]):
        max_ruyhat = [uzun]
print("Eng uzun so'z:", max_ruyhat)


