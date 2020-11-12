import json, requests

if __name__ == "__main__":
    while(1):
        cmd = input("Insert the operation to be performed: ")
        op1 = input("Insert the first operand: ")
        op2 = input("Insert the second operand: ")

        try:
            req = requests.get(f"http://localhost:8080/{cmd}?op1={op1}&op2={op2}")
        except:
            pass
        
        calc_res = ((req.json())["operations"].pop())["result"]
        print(f"Result: {calc_res}")
