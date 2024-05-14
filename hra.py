import random #importuje random modul na generování random čísel

delka = random.randint(1, 5) #generuje random čísla

pole = []

for x in range(delka): #určí kolikkrát se to má opakovat
    pole.append(random.randint(1, 5)) #přidá do pole random cislo mezi 1 a 88

print(pole)

delka = random.randint(1, 5)

pole = [random.randint(1, 5) for x in range (delka)]

print(f"Náhodná délka pole: {delka}")

print(f"Náhodné pole {pole}")

