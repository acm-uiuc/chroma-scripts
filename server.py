import cherrypy as http
import os
import subprocess
import signal
import json

from mako.template import Template
from mako.lookup import TemplateLookup
lookup = TemplateLookup(directories=['templates'])
p = None
current = "Off"

class Serv:
   @http.expose
   def index(self):
      global current
      animations  = os.listdir('./animations/')
      aData = {}
      for a in animations:
         json_data=open('animations/%s/manifest.json'%a)
         data = json.load(json_data)
         aData[a] = data
         json_data.close()
      tmpl = lookup.get_template("index.html")
      return tmpl.render(animations=aData,current=current)

   @http.expose
   @http.tools.allow(methods=['POST'])
   def set(self, animation):
      global p
      global current
      if p:
         os.kill(p.pid, signal.SIGTERM)
      if animation == "Off":
         current = "Off"
         return "Turned off"
      animations  = os.listdir('./animations/')
      if animation in animations:
         p = subprocess.Popen(['python','animations/%s/main.py'%animation])
         current = animation
         return "Animation %s started"%animation
      return "Unknown animation %s"%animation

if __name__ == "__main__":
   config = {
             '/static':{
                    'tools.staticdir.on': True,
                    'tools.staticdir.dir': os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))
             }
   }
   
   
   http.tree.mount(Serv(), '/', config = config)
   http.config.update( {'server.socket_host':"0.0.0.0", 'server.socket_port':8181 } )
   http.engine.signal_handler.subscribe()
   http.engine.start()
   http.engine.block()
