from std_msgs.msg import String
import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
Request = None

reletemperatura = 0 #pin 12, rele1
relebombillo1 = 0   #pin 16, rele2 
relebombillo2 = 0   #pin 18, rele3
relebombillo3 = 0   #pin 22, rele4

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global reletemperatura
    global relebombillo1
    global relebombillo2
    global relebombillo3
    global Request
    messagetosend = bytes('Hi Andrexe',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    Request = self.requestline
    Request = Request[5 : int(len(Request)-9)]
    print(Request)
    if Request == '1':#temperatura
        GPIO.output(12,True)
        reletemperatura = 1
    if Request == '0':
        GPIO.output(12,False)
        reletemperatura = 0
    if Request == '2':#bombillo1
        GPIO.output(16,True)
        relebombillo1 = 1
    if Request == '3':
        GPIO.output(16,False)
        relebombillo1 = 0
    if Request == '4':#bombillo2
        GPIO.output(18,True)
        relebombillo2 = 1
    if Request == '5':
        GPIO.output(18,False)
        relebombillo2 = 0
    if Request == '6':#bombillo3
        GPIO.output(22,True)
        relebombillo3 = 1
    if Request == '7':
        GPIO.output(22,False)      
        relebombillo3 = 0
    return

server_address_httpd = ('192.168.0.104',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Iniciando Servidor')
httpd.serve_forever()
GPIO.cleanup()
