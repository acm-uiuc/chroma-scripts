import cherrypy as http
import os
import subprocess
import signal
from mako.template import Template
from mako.lookup import TemplateLookup
lookup = TemplateLookup(directories=['static'])
p = None

class rest:
   @http.expose
   def index(self):
      animations  = os.listdir('./animations/')
      tmpl = lookup.get_template("index.html")
      return tmpl.render(animations=animations)

   @http.expose
   def set(self, animation):
      global p
      if p:
         os.kill(p.pid, signal.SIGTERM)
      if animation == "Off":
         return "Turned off"
      animations  = os.listdir('./animations/')
      if animation in animations:
         p = subprocess.Popen(['python','animations/%s/main.py'%animation])
      return "Animation %s started"%animation

if __name__ == "__main__":
   http.config.update( {'server.socket_host':"0.0.0.0", 'server.socket_port':8181 } )
   http.quickstart( rest() )
