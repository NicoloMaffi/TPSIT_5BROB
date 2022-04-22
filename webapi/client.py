import requests

def main():
    cmd = input("API all (1) or API book (2)? ")

    if cmd == '1':
        req = requests.get("http://127.0.0.1:5000/api/v1/resources/books/all")
    elif cmd == '2':
        id = input("Enter numeric id: ")

        req = requests.get(f"http://127.0.0.1:5000/api/v1/resources/books?id={id}")

    print(req.text)

if __name__ == "__main__":
    main()