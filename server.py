#!./virt_env/bin/python
import os
import cherrypy as http
import subprocess
import signal
import simplejson as json

class Serv:
   @http.expose
   def play(self, animation):
      global p
      global current
      if p:
         os.kill(p.pid, signal.SIGTERM)
      if animation == "Off":
         current = "Off"
         return "Turned off"
      animations  = os.listdir('./animations/')
      if animation in animations:
         p = subprocess.Popen(['env','PYTHONPATH=./osc:$PYTHONPATH','python','animations/%s/main.py'%animation])
         current = animation
         return "Animation %s started"%animation
      return "Unknown animation %s"%animation

   @http.expose
   def pull(self):
      p = os.popen('git pull origin master','r')
      output = ""
      while 1:
         line = p.readline()
         if not line: break
         output += line + '\n'
      animations  = os.listdir('./animations/')
      aData = []
      for a in animations:
         json_data=open('animations/%s/manifest.json'%a)
         data = json.load(json_data)
         aData.append(data)
         json_data.close()
      ret_data = {'output':output, "animations":aData}
      return json.dumps(ret_data)
         
      

if __name__ == "__main__":
   config = {
   }


   http.tree.mount(Serv(), '/', config = config)
   http.config.update( {'server.socket_host':"0.0.0.0", 'server.socket_port':8181 } )
   http.engine.signal_handler.subscribe()
   http.engine.start()
   http.engine.block()
