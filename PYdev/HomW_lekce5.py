numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]

# 1. pomocí cyklu for vypište čísla ze seznamu numbers, ale přeskočte záporná čísla.

# 2. pomocí cyklu while vypište všechna jména, pokud narazíš na jméno 'Alice' cyklus ukonči

# 3. pomocí list comprehension vytvoř nový list, který bude obsahovat pouze prvky z 'random_codes', které obsahují 0

# 4. Dobrovolny ukol pro pokrocile (nebude bodovan): Vypis všechny pod-seznamy s alespoň třemi po sobě jdoucími stejnými znaky v seznamu 'random_codes'



# 1. Kladné čísla
print("I. Výpis kladných prvků ze seznamu:")
for N in numbers:
    if N > 0:
        print(N)
print()

# 2. Alice
print("II.Výpis pomocí while s ukončením cyklu:")
n = 0
while n < len(names):
    name = names[n]
    if name == "Alice":
        break
    print(name)
    n += 1
print()

# 3. Zero element
print("III.Comprehension list pro prvky obsahující 0")
zero_element = [e for e in random_codes if "0" in e]
for zero in zero_element:
    print(zero)

# 4. Sublist 3e
print("IV. prvky se třemi po sobě jdoucími znaky v seznamu RC vypsané do samostatných sub-listů: ")
main_list = []
for x in random_codes:
    for e in range(len(x) - 2):
        if x[e] == x[e + 1] == x[e + 2]:
            main_list.append([ x ])
            break
print(main_list)