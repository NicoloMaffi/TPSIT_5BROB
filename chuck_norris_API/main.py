import requests, os

def main():
    while True:
        os.system("cls")

        print("\n\
            \t******************************************************\n\
            \t* 1 - Random chuck norris joke from a given category *\n\
            \t* 2 - List of available categories                   *\n\
            \t* 3 - Free text search                               *\n\
            \t* 4 - Exit                                           *\n\
            \t******************************************************\n\
        ")

        choice = input("Choice> ")
        print()

        match choice:
            case "1":
                category = input("Random_joke\Category> ")
                print()

                r = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}")

                try:
                    print(r.json()["value"])
                except:
                    print(f"Error: The category '{category}' does not exists!")

            case "2":
                r = requests.get("https://api.chucknorris.io/jokes/categories")
                data = r.json()

                for i, d in enumerate(data):
                    print(f"{i + 1}) {d}")

            case "3":
                query = input("Free_text\Query> ")
                print()

                r = requests.get(f"https://api.chucknorris.io/jokes/search?query={query}")
                data = r.json()

                if data["result"] == []:
                    print(f"Error: No match for '{query}'!")
                else:
                    for i, d in enumerate(data["result"]):
                        print(f"{i + 1}) {d['value']}")

            case "4":
                break

            case _:
                print(f"Error: Choice '{choice}' not found!")

        input("\n")

    os.system("cls")

if __name__ == "__main__":
    main()