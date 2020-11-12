import cherrypy, json, os

class WebService(object):
    exposed = True

    def GET(self, *uri, **params):
        return open("index.html", "r")

    def POST(self, *uri, **params):
        cl = cherrypy.request.headers['Content-Length']
        body_request = json.loads(cherrypy.request.body.read(int(cl)))

        devices = json.load(open("devices.json", "r"))
        devices["devicesList"].append(body_request)

        json.dump(devices, open("devices.json", "w"))

        return (open("devices.json", "r"))

if __name__ == "__main__":
    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/css':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir':'./css'
        },
        '/js':{
            'tools.staticdir.on':True,
            'tools.staticdir.dir':'./js'
        }
    }   
    cherrypy.tree.mount(WebService(), '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()   