import cherrypy
import smtplib
from email.mime.text import MIMEText

class emailDEPT(object):
    def index(self,to,theMSG):
        recipients=to.split(",")
        s = smtplib.SMTP('mail.yourdomain.com')
       	sender="noreply@yourdomain.com"
        subj="Text Messaging System"
        msg = MIMEText(theMSG)
        msg['Subject'] = subj
        msg['From'] = sender
        msg['To'] = to
        s.sendmail(msg.get('From'), recipients, msg.as_string())
        return "Mail sent to: "+to        
    index.exposed = True

   


cherrypy.config.update(
   {'server.socket_host': '0.0.0.0','server.socket_port': 8088,} )
cherrypy.quickstart(emailDEPT())
