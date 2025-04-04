#   Napiš program, který bude pracovat s informacemi o uživatelském účtu: username, age, email
#   Vytvoř následující funkce:
#
#   is_adult: Funkce ověří zda je uživatel dospělý
#
#   is_name_valid: Funkce ověří zda uživatelské jméno je alespoň 4 znaky dlouhé
#
#   create_user:
#   Funkce vytvoří slovník reprezentujícího uživatele.
#   Uvnitř funkce zkontroluj, zda je uživatel dospělý a jeho jméno je validní.
#   Pokud je vše v pořádku, create_user vrátí následující slovník:
#   {
#   "success": True,
#   "user": {"username": "...", "age": ..., "email": "..."}
#   }
#   Pokud validace selže, create_user vrátí:
#   {
#   "success": False,
#   "error": "Chybová zpráva..."
#   }
#
#   print_user_info: Funkce vytiskne uživatele do konzole s libovolným formátováním, případně vytiskne chybovou zprávu při neúspěšném vytvoření
#   Pomocí metody create_user vytvoř alespoň 4 různé uživatele. Hodnoty si zvol podle sebe přímo v programu. ???
#   Nakonec vytvořené uživatele vytiskni pomocí cyklu a metody print_user_info.

from datetime import datetime

def is_adult(year_of_birth):
    current_year = datetime.now().year
    age = current_year - year_of_birth
    return age >= 18

def is_name_valid(username):
    return bool(username) and len(username) >= 4

def create_user(username, year_of_birth, email):
    if not is_name_valid(username):
        return {
            "success": False,
            "error": "Uživatelské jméno nesmí být prázdné a musí mít alespoň 4 znaky."
        }

    if not is_adult(year_of_birth):
        return {
            "success": False,
            "error": "Uživatel musí být plnoletý."
        }


    age = datetime.now().year - year_of_birth
    return {
        "success": True,
        "user": {
            "username": username,
            "age": age,
            "email": email
        }
    }


def print_user_info(user_info):
    if user_info["success"]:
        user = user_info["user"]
        print(f"Uživatelské jméno: {user['username']}, Věk: {user['age']}, Email: {user['email']}")
    else:
        print("Chyba:", user_info["error"])

# Engine uložení / uložených uživatelů
def main():
    created_users = []

    while True:
        username = input("Zadejte uživatelské jméno: ")

        if not is_name_valid(username):
            print("Chyba: Uživatelské jméno nesmí být prázdné a musí mít alespoň 4 znaky.")
            continue

        year_of_birth = input("Zadejte rok narození RRRR: ")

        try:
            year_of_birth = int(year_of_birth)
        except ValueError:
            print("Chyba: Rok narození musí být číslo.")
            continue

        email = input("Zadejte emailovou adresu: ")

        user_info = create_user(username, year_of_birth, email)

# Proces uložení uživatele
        if user_info["success"]:
            create_confirmation = input("Přejete si vytvořit uživatele? (A/N): ").strip().upper()
            if create_confirmation == "A":
                created_users.append(user_info["user"])
                print(f"Uživatel \"{username}\" úspěšně vytvořen!")

                want_to_print = input("Přejete si vypsat všechny dosud vytvořené uživatele? (A/N): ").strip().upper()
                if want_to_print == "A":
                    print("Seznam všech uložených uživatelů:")
                    for user in created_users:
                        print_user_info(create_user(user['username'], datetime.now().year - user['age'], user['email']))
                continue

            elif create_confirmation == "N":
                print("Údaje byly smazány.")
                continue
            else:
                print("Neplatná volba, uživatel nebyl vytvořen.")
        else:
            print("Údaje nebyly uloženy vzhledem k chybě.")
            print_user_info(user_info)
            continue

if __name__ == "__main__":
    main() #start formulaře

