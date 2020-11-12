import cherrypy, json

def append_to_data(operation, operands, output):
    data_out = {
        "operations" : []
    }
    data_out["operations"].append  ({
                "operation" : operation,
                "operand_1" : float(operands[0]),
                "operand_2" : float(operands[1]),
                "result" : f"{output:.2f}"
            })
    return data_out

class Calculator(object):
    exposed = True

    def GET(self, *uri, **params):
        cmd=""
        #Check URI
        uri=list(uri)
        if len(uri) != 3 :
            return "<h1>Command not recognized, use /cmd/op1/op2</h1>"
        cmd = uri[0]
        operator_1 = uri[1]
        operator_2 = uri[2]

        if cmd == "add":
            output = float(operator_1) + float(operator_2)
            resp = append_to_data(cmd, [float(operator_1), float(operator_2)], output)
            print(resp)
            return json.dumps(resp)
        elif cmd == "sub":
            output = float(operator_1) - float(operator_2)
            resp = append_to_data(cmd, [float(operator_1), float(operator_2)], output)
            print(resp)
            return json.dumps(resp)
        elif cmd == "mul":
            output = float(operator_1) * float(operator_2)
            resp = append_to_data(cmd, [float(operator_1), float(operator_2)], output)
            print(resp)
            return json.dumps(resp)
        elif cmd == "div":
            try:
                output = float(operator_1) / float(operator_2)
                resp = append_to_data(cmd, [float(operator_1), float(operator_2)], output)
                print(resp)
                return json.dumps(resp)
            except:
                return ("Division per 0 not allowed!")
        else:
            return "<h1>Command not recognized, use /cmd/op1/op2</h1>"

if __name__=="__main__":
    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }   
    cherrypy.tree.mount(Calculator(), '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()        