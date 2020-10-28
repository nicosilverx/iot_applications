import cherrypy

class ParamsLister():
    exposed=True

    def __init__(self):
        pass
    
    def PUT(self,**params):
        if params!={}:
            keysList=list(params.keys())
            valuesList=[params[key] for key in params.keys()]
        output=f" Keys :{keysList}, values :{valuesList}"
        return output

if __name__=="__main__":
    #Standard configuration to serve the url "localhost:8080"
    conf={
        '/':{
                'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on':True
        }
    }
    cherrypy.config.update({'server.socket_port':8080})
    cherrypy.quickstart(ParamsLister(),'/',conf)