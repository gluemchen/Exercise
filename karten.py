untergrenze = int(input("Geben Sie eine Untergrenze ein: "))
obergrenze = int(input("Geben Sie eine Obergrenze ein: "))
bereich = range(untergrenze, obergrenze)
for i in bereich:
print(step + i)
    if i < obergrenze:
        step = +i
    continue

