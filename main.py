import socket
import time
import sys
import os
import pyautogui# pip install pyautogui
import getpass # pip install getpass
from http.server import BaseHTTPRequestHandler, HTTPServer
ip = open("IP.txt").read()

#ip = "10.0.0.7" #Set manual IP address.

class RequestHandler_httpd(BaseHTTPRequestHandler):
    pyautogui.FAILSAFE = False
    def do_GET(self):
        global MyRequest
        MyRequest = self.requestline
        MyRequest = MyRequest[5 : int(len(MyRequest) - 9)]
        messagetosend = bytes("Error 404", "utf-8")
        if MyRequest != "favicon.ico" and MyRequest != "":
            #print("You Received this request ", MyRequest, ", Formated data: ")

            MyRequest = MyRequest.replace("%20", " ")
            #print(MyRequest)
            MyRequest = MyRequest.split()
            if MyRequest[0] == "exit":
                messagetosend = bytes("EXITING!", "utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/plain")
                self.send_header("Content-Lenght", len(messagetosend))
                self.end_headers()
                self.wfile.write(messagetosend)
                print("Exiting!!")
                sys.exit()
            if MyRequest[0].lower() == "+v":
                if len(MyRequest) > 1:
                    for i in range(0,int(MyRequest[1])):
                        pyautogui.press("volumeup")
                    messagetosend = bytes("Done!", "utf-8")
                else:
                    pyautogui.press("volumeup")
                    messagetosend = bytes("Done!!!", "utf-8")
            if MyRequest[0].lower() == "-v":
                if len(MyRequest) > 1:
                    messagetosend = bytes("Done!!!", "utf-8")
                    for i in range(0,int(MyRequest[1])):
                        pyautogui.press("volumedown")
                else:
                    messagetosend = bytes("Done!!!", "utf-8")
                    pyautogui.press("volumedown")
            if MyRequest[0].lower() == "playpause":
                pyautogui.press("playpause")
                messagetosend = bytes("Played/Paused!", "utf-8")
            if MyRequest[0].lower() == "muteunmute":
                messagetosend = bytes("Muted!!", "utf-8")
                pyautogui.press("volumemute")
            if MyRequest[0].lower() == "forward":
                messagetosend = bytes("Done!!!", "utf-8")
                pyautogui.press("nexttrack")
            if MyRequest[0].lower() == "backward":
                messagetosend = bytes("Done!!!", "utf-8")
                pyautogui.press("prevtrack")
            if MyRequest[0].lower() == "test":
                username = getpass.getuser()
                print(username)
                messagetosend = bytes("Done!!!", "utf-8")
            if MyRequest[0].lower() == "start":
                if MyRequest[1].lower() == "discord":
                    os.system("start C:\\Users\\%s\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe" % getpass.getuser())
                    messagetosend = bytes("Done!!!", "utf-8")
                if MyRequest[1].lower() == "browser":
                    os.system('start C:\\Program""" """Files\\Google\\Chrome\\Application\\chrome.exe')
                    messagetosend = bytes("Done!!!", "utf-8")
                    
                
        
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Lenght", len(messagetosend))
        self.end_headers()
        self.wfile.write(messagetosend)
        return


server_address_httpd = (ip, 8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print("Starting Server:")
httpd.serve_forever()
