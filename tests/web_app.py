import cherrypy, string, random

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return open("page.html")
    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))

if __name__=="__main__":
    cherrypy.quickstart(HelloWorld())        