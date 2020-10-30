import json

data_out = {
        "operations" : []
    }

def append_to_data(operation, operands, output):
    global data_out
    data_out["operations"].append({
                "operation" : cmd,
                "operators" : operands,
                "result" : f"{output:.2f}"
            })
    json.dump(data_out, open("output.json", "w"))
if __name__ == "__main__":
    
    while(1):
        output = 0
        input_list = (input("Select an operation [add/sub/mul/div/exit] and insert the list of operands operands: ")).split()
        cmd = str(input_list[0])
        operands = input_list[1:len(input_list)]
        if(len(input_list)>1):
            output = float(operands.pop(0))
        if cmd == "add":
            for op in operands:
                output += float(op)
            append_to_data(cmd, operands, output)
            print(output)
        elif cmd == "sub":
            for op in operands:
                output -= float(op)
            append_to_data(cmd, operands, output)
            print(output)
        elif cmd == "mul":
            for op in operands:
                output *= float(op)
            append_to_data(cmd, operands, output)
            print(output)
        elif cmd == "div":
            try:
                for op in operands:
                    output /= float(op)
                append_to_data(cmd, operands, output)
                print(output)
            except:
                print("Division per 0 not allowed!")
        elif cmd == "exit":
            break

