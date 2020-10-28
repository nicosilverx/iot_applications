import string, cherrypy

class StringReverse(object):
    exposed = True

    def GET(self, *uri, **params):
        output=""
        uri=list(uri)
        if len(uri)!=0:
            output = uri.pop()[::-1]
        return output

if __name__=="__main__":
    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }   
    cherrypy.tree.mount(StringReverse(), '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()