import requests

if __name__=="__main__":
    while(True):
        print("Available commands:\n1) latest: latest change rate\n2) date: rate of a specific date\n3) history: historic exchange rates\n4) quit: exit")
        cmd = input("Insert a command: ")

        if cmd=="latest" or cmd=="1":
            base_currency = input("Specify the base currency: ")

            resp = requests.get(f"https://api.exchangeratesapi.io/latest?base={base_currency}")

            for rate in resp.json()["rates"]:
                print(rate + " : " + str(resp.json()["rates"][rate]))

        if cmd=="date" or cmd == "2":
            date = input("Specify the date in the YYYY-MM-GG format: ")

            resp = requests.get(f"https://api.exchangeratesapi.io/{date}")

            for rate in resp.json()["rates"]:
                print(rate + " : " + str(resp.json()["rates"][rate]))
        elif cmd=="history" or cmd=="3":
            start_date = input("Specify the starting date in the YYYY-MM-GG format: ")
            end_date = input("Specify the ending date in the YYYY-MM-GG format: ")

            resp = requests.get(f"https://api.exchangeratesapi.io/history?start_at={start_date}&end_at={end_date}")

            for timestamp in resp.json()["rates"]:
                print(timestamp + " : ")
                for rate in resp.json()["rates"][timestamp]:
                    print(rate + " : " + str(resp.json()["rates"][timestamp][rate]))
        elif cmd=="quit" or cmd=="4":
            break
        else:
            print("Command not valid, retry")

        