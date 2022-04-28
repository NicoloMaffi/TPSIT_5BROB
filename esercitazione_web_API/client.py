import math, requests

def main():
    clientId = input("Client id: ")
    url_graboperation = "http://127.0.0.1:5000/api/v1/graboperation?clientId={}"
    url_compute = "http://127.0.0.1:5000/api/v1/compute?operationId={}&result={}"

    while True:
        r = requests.get(url_graboperation.format(clientId)).json()

        if r["state"] == "ERROR":
            break

        operationId = r["operationId"]
        result = eval(r["operation"])

        r = requests.get(url_compute.format(operationId, result)).json()

        if r["state"] == "ERROR":
            print("Some errors occures during result trasmission!")

if __name__ == "__main__":
    main()