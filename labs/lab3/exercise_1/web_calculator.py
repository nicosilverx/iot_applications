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
        if len(uri)!=0:
            cmd = uri.pop()
        else:
            return "<h1>No command specified, use [add/sub/mul/div]</h1>"
        #Check parameters
        if params!={}:
            valuesList=[params[key] for key in params.keys()]
        
        if cmd == "add":
            output = float(valuesList[0]) + float(valuesList[1])
            resp = append_to_data(cmd, [float(valuesList[0]), float(valuesList[1])], output)
            print(resp)
            return json.dumps(resp)
        elif cmd == "sub":
            output = float(valuesList[0]) - float(valuesList[1])
            resp = append_to_data(cmd, [float(valuesList[0]), float(valuesList[1])], output)
            print(resp)
            return json.dumps(resp)
        elif cmd == "mul":
            output = float(valuesList[0]) * float(valuesList[1])
            resp = append_to_data(cmd, [float(valuesList[0]), float(valuesList[1])], output)
            print(resp)
            return json.dumps(resp)
        elif cmd == "div":
            try:
                output = float(valuesList[0]) / float(valuesList[1])
                resp = append_to_data(cmd, [float(valuesList[0]), float(valuesList[1])], output)
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