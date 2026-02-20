import json


def load_users():
    """Lädt die User-Daten und fängt Datei-Fehler ab."""
    try:
        with open("users.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: 'users.json' not found")
        return []

    except json.JSONDecodeError:
        print("Error: 'users.json' not written in the right way")
        return []


def filter_users_by_name(name):
    users = load_users()

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    if not filtered_users:
        print("No Users found with that name\n")
    else:
        for user in filtered_users:
            print(user)


def filter_users_by_age(age):
    users = load_users()

    filtered_users = [user for user in users if user["age"] == age]

    if not filtered_users:
        print("No Users found with that age\n")
    else:
        for user in filtered_users:
            print(user)


def filter_users_by_email(email):
    users = load_users()

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    if not filtered_users:
        print("No Users found with that email\n")
    else:
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    while True:
        filter_option = input("What would you like to filter by?"
                              "(Currently, only 'name', 'age' and 'email' is supported."
                              " Write 'exit' to leave): ").strip().lower()

        if filter_option == "name":
            name_to_search = input("Enter a name to filter users: ").strip()
            filter_users_by_name(name_to_search)

        elif filter_option == "age":
            try:
                age_to_search = int(input("Enter a age to filter users: ").strip())
                filter_users_by_age(age_to_search)
            except ValueError:
                print("We need a number\n")
                continue

        elif filter_option == "email":
            email_to_search = input("Enter a email to filter users: ").strip()
            filter_users_by_email(email_to_search)

        elif filter_option == "exit":
            print("goodbye")
            break

        else:
            print("Filtering by that option is not yet supported.\n")

