from datetime import datetime

print("VÍTEJTE V KALKULAČCE DOPRAVNÍHO PODNIKU")

while True:
    # Vstup uživatele pro rok narození
    birth_year = input("Zadejte prosím váš rok narození (RRRR): ")

    # Kontrola délky a formátu
    if len(birth_year) != 4 or not birth_year.isdigit(): # funkcionalitou duplicitní vzhledem ke kontrole validity rozsahu věku, ale ukol zněl jasně :)
        print("Prosím zadejte platný rok narození ve formátu RRRR (např. 1990).")
    else:
        try:
            birth_year = int(birth_year)  # Převod na celé číslo
            current_year = datetime.now().year  # Získání aktuálního roku
            age = current_year - birth_year  # Výpočet věku

            # Kontrola rozsahu věku
            if age < 0 or age > 120:
                print("Věk není v platném rozsahu.")
            else:
                # Dotaz na zaměstnanecký status pouze pro uživatele starší než 18 let
                dp_employee = ""
                if age >= 18:
                    dp_employee = input("Pokud jste zaměstnancem dopravního podniku, napište A, pokud nikoliv, ponechte pole prázdné: ").strip().upper()

                # Určení ceny jízdenky
                ticket_price = 45  # Základní cena
                ticket_type = "základní"  # Typ jízdenky

                # Počítání ceny jízdenky
                if dp_employee == 'A':
                    # Zaměstnanec dopravního podniku
                    if age > 55:
                        price = 0  # Jízdenka zdarma pro zaměstnance nad 55
                        ticket_type = "DP55+"
                    else:
                        price = ticket_price * 0.2  # 80% sleva pro zaměstnance
                        ticket_type = "DP80%"
                else:
                    # Běžný cestující
                    if age < 12:
                        price = 0  # Zdarma pro děti do 12 let
                        ticket_type = "dětská zlevněná"
                    elif age < 18:
                        price = ticket_price * 0.5  # 50% sleva
                        ticket_type = "dorost"
                    elif age > 65:
                        price = ticket_price * 0.7  # 30% sleva
                        ticket_type = "senior"
                    else:
                        price = ticket_price  # Plná cena

                print(f"Váš věk je: {age} let a proto pro jízdenku typu '{ticket_type}' je cena: {price:.1f} Kč.")
                print("Díky že využíváte služeb dopravního podniku!")
                break  # Konec cyklického dotazu na věk v případě chybného zadání.

        except ValueError:
            print("Něco se pokazilo :(' )