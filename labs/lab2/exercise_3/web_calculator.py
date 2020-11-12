import cherrypy, json

def append_to_data(operation, operands, output):
    data_out = {
        "operations" : []
    }
    data_out["operations"].append  ({
                "operation" : operation,
                "operands" : operands,
                "result" : f"{output:.2f}"
            })
    return data_out

class Calculator(object):
    exposed = True

    def PUT(self, *uri, **params):
        cl = cherrypy.request.headers['Content-Length']
        body_request = json.loads(cherrypy.request.body.read(int(cl)))
        
        cmd = body_request["command"]
        operands = body_request["operands"]
        original_operands = operands

        output = 0

        if(len(operands)>1):
            output = float(operands.pop(0))
        if cmd == "add":
            for op in operands:
                output += float(op)
            resp = append_to_data(cmd, original_operands, output)
            return json.dumps(resp)
        elif cmd == "sub":
            for op in operands:
                output -= float(op)
            resp = append_to_data(cmd, original_operands, output)
            return json.dumps(resp)
        elif cmd == "mul":
            for op in operands:
                output *= float(op)
            resp = append_to_data(cmd, original_operands, output)
            return json.dumps(resp)
        elif cmd == "div":
            try:
                for op in operands:
                    output /= float(op)
                resp = append_to_data(cmd, original_operands, output)
                return json.dumps(resp)
            except:
                return "<h1>Division per 0 not allowed!</h1>"
        else:
            print("Command not recognized")

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