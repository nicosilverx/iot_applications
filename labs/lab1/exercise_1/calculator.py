import json

data_out = {
        "operations" : []
    }

def append_to_data(operation, operands, output):
    global data_out
    data_out["operations"].append({
                "operation" : cmd,
                "operand_1" : float(operands[0]),
                "operand_2" : float(operands[1]),
                "result" : f"{output:.2f}"
            })
    json.dump(data_out, open("output.json", "w"))
if __name__ == "__main__":
    
    while(1):
        output = 0
        input_list = (input("Select an operation [add/sub/mul/div/exit] and insert the two operands: ")).split()
        cmd = str(input_list[0])
        operands = input_list[1:3]
        if cmd == "add":
            output = float(operands[0]) + float(operands[1])
            append_to_data(cmd, operands, output)
            print(output)
        elif cmd == "sub":
            output = float(operands[0]) - float(operands[1])
            append_to_data(cmd, operands, output)
            print(output)
        elif cmd == "mul":
            output = float(operands[0]) * float(operands[1])
            append_to_data(cmd, operands, output)
            print(output)
        elif cmd == "div":
            try:
                output = float(operands[0]) / float(operands[1])
                append_to_data(cmd, operands, output)
                print(output)
            except:
                print("Division per 0 not allowed!")
        elif cmd == "exit":
            break

