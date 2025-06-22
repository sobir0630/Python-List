numbers = []
for i in range(6):
    numbers.append(int(input(f"{i+1}_sonni kritng: ")))

pairs = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == 10:
            pairs.append((numbers[i], numbers[j]))
print("Yigindi: ", pairs)