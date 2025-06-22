sonlar = []
for i in range(10):
    user = int(input(f"{i+1}_sonni krtng: "))
    sonlar.append(user)

takrorsiz = []
for son in sonlar:
    if sonlar.count(son) == 1:
        takrorsiz.append(son)
print(f"takrorsiz sonlar: {takrorsiz}")

