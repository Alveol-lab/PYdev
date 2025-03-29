# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.

# 2. Změň cenu jedné libovolné knihy. Vypiš list.

# 3. Odstraň nějakou knihu. Vypiš list.

# 4. Vypiš celkový počet knih v listu.

# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)

books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
    }
]
#1A: Založení titulu 2. knihy
book1 = {
    "name": "Honzíkova cesta",
    "price": 400,
    "author": "Marie Poledňáková",
    "publication_year": 1971,
}
 #1A: Založení titulu 3. knihy
book2 = {
    "name": "1984",
    "price": 300,
    "author": "George Orwell",
    "publication_year": 1948,
}
#1B: Přidání do listu
books.append(book1)
books.append(book2)
print("Aktualizovaný seznam listu: ", books)

#2: Změna ceny knihy "1984" na 800 Kč
books[2]["price"] = 800
print("Nová cena titulu George Orwela !!! ", books)

#3: Odstranění Honzíkovi cesty
zrusena_kniha = books.pop(1)
print("Zrušená kniha: ", zrusena_kniha)
print("Aktualizovaný seznam: ", books)

#4: Počet titulů v seznamu
pocet_titulu = len(books)
print("Pocet titulu v listu:" , pocet_titulu)

#5: Input - definování atributů
name = input("Název vkládané knihy: ")
price = float(input("Cena knihy: "))
author = input("Autor knihy: ")
publication_year = int(input("Rok publikace knihy: "))

# Vložení nového titulu
novy_titul = {
    "name": name,
    "price": price,
    "author": author,
    "publication_year": publication_year,
}

# Přidání nového titulu knihy do seznamu
books.append(novy_titul)

# Výpis seznamu a hláška o přidání titulu
print("Nový titul byl přidán!")
print(books)
