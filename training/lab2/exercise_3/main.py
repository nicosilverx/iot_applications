import cherrypy, os

class Example(object):
    exposed=True
    def __init__(self):
        self.id=1
    def GET(self):
        return open("index.html")

if __name__=="__main__":
    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.staticdir.root':os.path.abspath(os.getcwd()),
        },
        '/css':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir':'./css'
        },
        '/js':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir':'./js'
        },
    }
    cherrypy.quickstart(Example(),'/',conf)